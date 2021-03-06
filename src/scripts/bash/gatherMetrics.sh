#! /bin/bash
helpFunction()
{
        echo ""
        echo "Gets the quality metrics for each project"
        echo ""
        echo "Usage: $0 -d directory -o output"
        echo -e "\t-d Path to directory to search"
        echo -e "\t-o Path to output file"
        echo -e "\t-F Force overwrites"
        exit 1 # Exit script after printing help
}

force=0

while getopts "d:o:F" opt
do
        case "$opt" in
                d ) directory="$OPTARG" ;;
                o ) output="$OPTARG" ;;
                F ) force=1 ;;
                ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
        esac
done

if [[ ! -f "gatherMetricsConfig.sh" ]]; then
  {
  echo "  # Config file for gatherMetrics.sh
  # Metrics with value '1' are enabled and '0' are disabled
  
  ISMETRICS=0  # Insert Size Metrics
  HSMETRICS=0  # Hs Metrics
  ASMETRICS=0  # Alignment Summary Metrics
  FLMETRICS=0  # Flagstat metrics
  GCBMETRICS=0 # gc Bias metrics
  QBCMETRICS=0 # Quality by cycle metrics
  QDMETRICS=0  # Quality distribution metrics, Slow due to formatting
  BIMETRICS=0  # Bam index stats metrics
  INDEXSAMPLES=0 # Sample sheet index"
  } > "gatherMetricsConfig.sh"
  
  echo "Created Config file in gatherMetricsConfig.sh , exiting..."
  exit 1 # exit after generating a default config
fi

# Print helpFunction in case parameters are empty
if [ -z "$directory" ] || [ -z "$output" ]
then
        echo "Missing one or more parameters";
        helpFunction
fi

if [[ ! -d "$directory" ]]; then 
  echo "Input directory doesn't exist"
  exit 1
fi

# if output already exists

checkconfig() 
{
  enabled=""
  if [[ "$HSMETRICS" -eq "1" ]]; then
      enabled="$enabled HSmetrics,"
  fi
  if [[ "$ISMETRICS" -eq "1" ]]; then
    enabled="$enabled insertSizeMetrics,"
  fi
  if [[ "$ASMETRICS" -eq "1" ]]; then
    enabled="$enabled AlignmentSummaryMetrics,"
  fi
  if [[ "$FLMETRICS" -eq "1" ]]; then
    enabled="$enabled FlagstatMetrics,"
  fi
  if [[ "$GCBMETRICS" -eq "1" ]]; then
    enabled="$enabled gcBiasMetrics,"
  fi
  if [[ "$QBCMETRICS" -eq "1" ]]; then
    enabled="$enabled QualityByCycleMetrics,"
  fi
  if [[ "$QDMETRICS" -eq "1" ]]; then
    enabled="$enabled QualityDistributionMetrics,"
  fi
  if [[ "$INDEXSAMPLES" -eq "1" ]]; then
    enabled="$enabled SampleIndex"
  fi
  if [[ $enabled == "" ]]; then
    echo "No files enabled, exiting..."
    exit 1
  fi
  echo "gathering: ${enabled}"
}
# shellcheck disable=SC1091
source "gatherMetricsConfig.sh"
checkconfig


HERE=$PWD
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
counter=0
cd "$directory" || exit # go to projects directory
# shellcheck disable=SC2010
total=$(ls -l | grep -c ^d)
tmpdir="${HERE}/.tmpMetricsGatherDir/"

if [[ -d $tmpdir ]]; then
    rm -r "$tmpdir"
fi

mkdir "${tmpdir}"

setupFiles()
{
  # Function to add headers and prefixes to the enabled files
  if [[ "$HSMETRICS" -eq "1" ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,BAIT_SET,GENOME_SIZE,BAIT_TERRITORY,TARGET_TERRITORY,BAIT_DESIGN_EFFICIENCY,TOTAL_READS,PF_READS,PF_UNIQUE_READS,PCT_PF_READS,PCT_PF_UQ_READS,PF_UQ_READS_ALIGNED,PCT_PF_UQ_READS_ALIGNED,PF_BASES_ALIGNED,PF_UQ_BASES_ALIGNED,ON_BAIT_BASES,NEAR_BAIT_BASES,OFF_BAIT_BASES,ON_TARGET_BASES,PCT_SELECTED_BASES,PCT_OFF_BAIT,ON_BAIT_VS_SELECTED,MEAN_BAIT_COVERAGE,MEAN_TARGET_COVERAGE,MEDIAN_TARGET_COVERAGE,PCT_USABLE_BASES_ON_BAIT,PCT_USABLE_BASES_ON_TARGET,FOLD_ENRICHMENT,ZERO_CVG_TARGETS_PCT,PCT_EXC_DUPE,PCT_EXC_MAPQ,PCT_EXC_BASEQ,PCT_EXC_OVERLAP,PCT_EXC_OFF_TARGET,FOLD_80_BASE_PENALTY,PCT_TARGET_BASES_1X,PCT_TARGET_BASES_2X,PCT_TARGET_BASES_10X,PCT_TARGET_BASES_20X,PCT_TARGET_BASES_30X,PCT_TARGET_BASES_40X,PCT_TARGET_BASES_50X,PCT_TARGET_BASES_100X,HS_LIBRARY_SIZE,HS_PENALTY_10X,HS_PENALTY_20X,HS_PENALTY_30X,HS_PENALTY_40X,HS_PENALTY_50X,HS_PENALTY_100X,AT_DROPOUT,GC_DROPOUT,HET_SNP_SENSITIVITY,HET_SNP_Q,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/hsMetrics.csv"
  fi
  if [[ "$ISMETRICS" -eq "1" ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,MEDIAN_INSERT_SIZE,MEDIAN_ABSOLUTE_DEVIATION,MIN_INSERT_SIZE,MAX_INSERT_SIZE,MEAN_INSERT_SIZE,STANDARD_DEVIATION,READ_PAIRS,PAIR_ORIENTATION,WIDTH_OF_10_PERCENT,WIDTH_OF_20_PERCENT,WIDTH_OF_30_PERCENT,WIDTH_OF_40_PERCENT,WIDTH_OF_50_PERCENT,WIDTH_OF_60_PERCENT,WIDTH_OF_70_PERCENT,WIDTH_OF_80_PERCENT,WIDTH_OF_90_PERCENT,WIDTH_OF_99_PERCENT,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/insertSizeMetrics.csv"
  fi
  if [[ "$ASMETRICS" -eq "1" ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,CATEGORY,TOTAL_READS,PF_READS,PCT_PF_READS,PF_NOISE_READS,PF_READS_ALIGNED,PCT_PF_READS_ALIGNED,PF_ALIGNED_BASES,PF_HQ_ALIGNED_READS,PF_HQ_ALIGNED_BASES,PF_HQ_ALIGNED_Q20_BASES,PF_HQ_MEDIAN_MISMATCHES,PF_MISMATCH_RATE,PF_HQ_ERROR_RATE,PF_INDEL_RATE,MEAN_READ_LENGTH,READS_ALIGNED_IN_PAIRS,PCT_READS_ALIGNED_IN_PAIRS,BAD_CYCLES,STRAND_BALANCE,PCT_CHIMERAS,PCT_ADAPTER,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/AlignmentSummaryMetrics.csv"
  fi
  if [[ "$FLMETRICS" -eq "1" ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,TOTAL_PASS,TOTAL_FAIL,SECONDARY_PASS,SECONDARY_FAIL,SUPPLEMENTARY_PASS,SUPPLEMENTARY_FAIL,DUPLICATE_PASS,DUPLICATE_FAIL,MAPPED_PASS,MAPPED_FAIL,MAPPED_PCT,PAIRED_SEQ_PASS,PAIRED_SEQ_FAIL,R1_PASS,R1_FAIL,R2_PASS,R2_FAIL,PROPER_PAIR_PASS,PROPER_PAIR_FAIL,BOTH_MAPPED_PASS,BOTH_MAPPED_FAIL,SINGLETONS_PASS,SINGLETONS_FAIL,SINGLETONS_PCT,MATE_ON_DIFF_CHR_LOW_PASS,MATE_ON_DIFF_CHR_LOW_FAIL,MATE_ON_DIFF_CHR_HIGHQ_PASS,MATE_ON_DIFF_CHR_HIGHQ_FAIL,DATE" > "${tmpdir}/FlagstatMetrics.csv"
  fi
  if [[ "$GCBMETRICS" -eq "1" ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,ACCUMULATION_LEVEL,READS_USED,GC,WINDOWS,READ_STARTS,MEAN_BASE_QUALITY,NORMALIZED_COVERAGE,ERROR_BAR_WIDTH,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/gcBiasMetrics.csv"
  fi
  if [[ "$QBCMETRICS" -eq "1" ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,DATE,#" > "${tmpdir}/QualityByCycleMetrics.csv"
    MaxCycles=0
  fi
}

getDate() {
  # Function that gets the date from the sample entry
  DATE=$(echo "${SampleEntry}" | grep -oP '(?<=,)(([1-2][0-9])((0[1-9])|(1[0-2]))((0[1-9])|(1[1-9])|(2[1-9])|(3[0-1])))(?=,)' | head -1)
}

storeSampleSheet()
{
  # parses samplesheet using IndexSamples python script
  # outputs to samples.csv
  python "${SCRIPTDIR}/../python/IndexSamples.py" -i "results/${PROJECTID}.csv" -o "${tmpdir}samples.csv" -f "${tmpdir}errorSamples/"
}
hsMetrics()
{
  # Function to parse hsMetrics file
  # Adds entries to hsMetrics.csv
  cd "results/qc/statistics" || return
  while IFS= read -r -d '' D
    do
      ROW=$(head -n 8 "${D}" | tail -1 | tr '\t' ',') # get the hs metrics
      ID=$(echo "${D}" | awk -F'.merged.dedup.bam.hs_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }') # get the sample ID
      SampleEntry=$(grep "${ID}" "../../${PROJECTID}.csv")
      getDate
      RowToInsert="${PROJECTID},${currentRunID},${ID},${ROW},${DATE}"
      NumberOfCollumns=$(echo "${RowToInsert}" | awk '{print gsub(/,/,"")}')
      if [[ $NumberOfCollumns == 59 ]]; then # if colums are complete insert data in tmp file
        echo "${RowToInsert}" >> "${tmpdir}/hsMetrics.csv"
      fi
    done < <(find . -name "*.merged.dedup.bam.hs_metrics" -type f -print0)
  cd ../../../
}

isMetrics()
{
  # Function to parse insert size metrics file
  # Adds entries to insertSizeMetrics.csv
  cd "results/qc/statistics" || return
  while IFS= read -r -d '' D
    do
      ROW=$(head -n 8 "${D}" | tail -1 | tr '\t' ',') # get the insert size metrics
      ID=$(echo "${D}" | awk -F'.merged.dedup.bam.insert_size_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }') # get the sample ID
      SampleEntry=$(grep "${ID}" "../../${PROJECTID}.csv")
      getDate
      RowToInsert="${PROJECTID},${currentRunID},${ID},${ROW},${DATE}"
      NumberOfCollumns=$(echo "${RowToInsert}" | awk '{print gsub(/,/,"")}')
      if [[ "$NumberOfCollumns" == "24" ]]; then # if colums are complete insert data in tmp file
        echo "${RowToInsert}" >> "${tmpdir}/insertSizeMetrics.csv"
      fi
    done < <(find . -name "*.merged.dedup.bam.insert_size_metrics" -type f -print0)
  cd ../../../
}

asMetrics()
{
  # Function to parse alignment summary metrics file
  # Adds entries to alignment summary metrics.csv
  # each asm file contains 3 rows, first of pair, second of pair and pair.
  cd "results/qc/statistics" || return
  while IFS= read -r -d '' D
    do
      ID=$(echo "${D}" | awk -F'.merged.dedup.bam.alignment_summary_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }')
      FIRST=$(grep "^FIRST_OF_PAIR" "${D}" | tr '\t' ',')
      SECOND=$(grep "^SECOND_OF_PAIR" "${D}" | tr '\t' ',')
      PAIR=$(grep "^PAIR" "${D}" | tr '\t' ',')
      SampleEntry=$(grep "${ID}" "../../${PROJECTID}.csv")
      getDate
      RowToInsertFirst="${PROJECTID},${currentRunID},${ID},${FIRST},${DATE}"
      RowToInsertSecond="${PROJECTID},${currentRunID},${ID},${SECOND},${DATE}"
      RowToInsertPair="${PROJECTID},${currentRunID},${ID},${PAIR},${DATE}"
      
      NumberOfCollumnsFirst=$(echo "${RowToInsertFirst}" | awk '{print gsub(/,/,"")}')
      NumberOfCollumnsSecond=$(echo "${RowToInsertSecond}" | awk '{print gsub(/,/,"")}')
      NumberOfCollumnsPair=$(echo "${RowToInsertPair}" | awk '{print gsub(/,/,"")}')
      
      if [[ $NumberOfCollumnsFirst == 28 ]] && [[ $NumberOfCollumnsSecond == 28 ]] &&  [[ $NumberOfCollumnsPair == 28 ]]; then
        {
         echo "$RowToInsertFirst
         $RowToInsertSecond
         $RowToInsertPair"
        } >> "${tmpdir}/AlignmentSummaryMetrics.csv"
      fi
    done < <(find . -name "*.merged.dedup.bam.alignment_summary_metrics" -type f -print0)
  cd ../../../
}
parseFlagStatFile()
{
  grep -oP '([0-9]+\s\+\s[0-9]+)|(?<=\()[0-9][0-9]\.[0-9][0-9](?=\%)' "$FlagstatFile" | tr "\n" "," | sed "s/[[:space:]]+[[:space:]]/,/g" | sed "s/[[:space:]]/,/g"
}

flMetrics()
{
  # Function to parse and store flagstat metrics
  # the flagstat metrics file has many entries in a little complex format
  
  cd "results/qc/statistics" || return
  while IFS= read -r -d '' D
    do
      ID=$(echo "${D}" | awk -F'.merged.dedup.bam.flagstat' '{ print $1 }' | awk -F'./' '{ print $2 }')
      FlagstatFile="$D"
      SampleEntry=$(grep "${ID}" "../../${PROJECTID}.csv")
      
      getDate
      parsedRow=$(parseFlagStatFile)
      
      ROW="${PROJECTID},${currentRunID},${ID},${parsedRow}${DATE}"
      NumberOfCollumns=$(echo "${ROW}" | awk '{print gsub(/,/,"")}')
      if [[ $NumberOfCollumns == 31 ]]; then
        echo "${ROW}" >> "${tmpdir}/FlagstatMetrics.csv"
      fi
    done < <(find . -name "*.merged.dedup.bam.flagstat" -type f -print0)
  cd ../../../
}

gcbMetrics() 
{
  # gc Bias Metrics parser. For each Gc bias file a table is parsed, which contains the info about the gc bins for said sample
  cd "results/qc/statistics" || return
  while IFS= read -r -d '' D
    do
      ID=$(echo "${D}" | awk -F'.merged.dedup.bam.gc_bias_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }')
      prefix="${PROJECTID},${currentRunID},${ID},"
      SampleEntry=$(grep "${ID}" "../../${PROJECTID}.csv")
      getDate
      suffix=",${DATE}#"

      Table=$(tail -n +8 "$D" | tr "\t" "," | grep . | awk -v prefix="$prefix" -v suffix="$suffix" '{print prefix $0 suffix}')
      
      NumberOfCollumnsCheck=$(echo "${Table}" | awk '{print gsub(/,/,"")}' | grep -v "14")
      
      if [[ $NumberOfCollumnsCheck == "" ]]; then
        echo "${Table//# /\n}" >> "${tmpdir}/gcBiasMetrics.csv"
      fi
  done < <(find . -name "*.merged.dedup.bam.gc_bias_metrics" -type f -print0)
  cd ../../../
}

qbcMetrics()
{
  # Function to parse Quality by cycle metrics
  cd "results/qc/statistics" || return
  while IFS= read -r -d '' D
    do
      ID=$(echo "${D}" | awk -F'.merged.dedup.bam.quality_by_cycle_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }')
      SampleEntry=$(grep "${ID}" "../../${PROJECTID}.csv")
      getDate
      ROW="${PROJECTID},${currentRunID},${ID},${DATE},"
      DATA=$(tail -n +9 "$D" | sed 's/[[:digit:]]\+\t//g')
      NumberOfCycles=$(echo "$DATA" | grep -c . )
      if [[ $NumberOfCycles -gt $MaxCycles ]]; then
        MaxCycles=$NumberOfCycles
      fi
      Cycles=$(echo "$DATA" | tr '\n' ',')
      ROW="${ROW},${Cycles}"

      NumberOfCollumns=$(echo "${ROW}" | awk '{print gsub(/,/,"")}')
      if [[ ! $NumberOfCollumns ]]; then
        continue
      else
        echo "$ROW" >> "${tmpdir}/QualityByCycleMetrics.csv"
      fi
  done < <(find . -name "*.merged.dedup.bam.quality_by_cycle_metrics" -type f -print0)
  cd ../../../
}

qdMetrics()
{
  # Function to parse Quality distribution metrics to json
  cd "results/qc/statistics" || return
  while IFS= read -r -d '' D
    do
      ID=$(echo "${D}" | awk -F'.merged.dedup.bam.quality_distribution_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }')
      python "${SCRIPTDIR}/../python/ParseQualityDistributionMetrics.py" -i "$D" -o "${tmpdir}QualityDistributions.csv" -s "$ID" -r "$currentRunID"
  done < <(find . -name "*.merged.dedup.bam.quality_distribution_metrics" -type f -print0)
  cd ../../../
}

finishOff()
{
  # Function to finish off files and compress results
  if [[ "$QBCMETRICS" -eq "1" ]]; then
    cycleRange=$(seq -s , "$MaxCycles")
    appendableHeader="PROJECT_ID,RUN,SAMPLE_ID,${cycleRange},DATE"
    sed -i "1s/#/$appendableHeader/" "${tmpdir}/QualityByCycleMetrics.csv"
  fi
  cd "$HERE" || exit
  echo -ne '\n'
  echo "Completed gathering metrics from ${total} directories"
  echo ""
  echo "Compressing results to ${output}"
  mv "$tmpdir" "gatheredMetrics"
  zip -r "$output" "gatheredMetrics"
  echo "Removing temporary files..."
  rm -r "gatheredMetrics"
  echo "Finished"

  exit 1
}




# shellcheck disable=SC2094
while IFS= read -r -d '' project
  do
      PROJECTID=$(basename "$project")
      progress=$((counter*100/total))
      echo -ne " ${progress}% of directories searched (${counter}/${total}) Project: ${PROJECTID}\r" # Progress indicator
      (( counter++ )) # Progress counter
      python "${HERE}/src/scripts/python/ExecutableScripts/indexProject.py" -p "$project" -d "$output" -i "$PROJECTID"
  done < <(find . -maxdepth 1 -mindepth 1 -type d -print0)

