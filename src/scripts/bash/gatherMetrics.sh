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
config=".gMetricsConfig.sh"

while getopts "d:o:F" opt
do
        case "$opt" in
                d ) directory="$OPTARG" ;;
                o ) output="$OPTARG" ;;
                F ) force=1 ;;
                c ) config="$OPTARG" ;;
                ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
        esac
done

if [[ ! -f "$config" ]]; then
  echo "# Config file for gatherMetrics.sh" > $config
  echo "# Metrics with value '1' are enabled and '0' are disabled" >> $config
  echo "" >> $config
  echo "InsertSizeMetrics=0" >> $config
  echo "HSMetrics=0" >> $config
  echo "AlignmentSummaryMetrics=0" >> $config
  echo "FlagstatMetrics=0" >> $config
  echo "gcBiasMetrics=0" >> $config
  echo "QualityByCycleMetrics=0" >> $config
  echo "QualityDistributionMetrics=0" >> $config
  echo "BamIndexMetrics=0" >> $config
  
  echo "Created Config file at ${config} , exiting..."
  exit 1 # exit after generating a default config
fi

# Print helpFunction in case parameters are empty
if [ -z "$directory" ] || [ -z "$output" ]
then
        echo "Missing one or more parameters";
        helpFunction
fi

# if output already exists
if [[ $force == 0 ]] &&  [[ -f $output ]]; then
        echo "$output already exists, overwrite? [y/n]:"
        read answer
        if [[ $answer == "n" ]]; then
                echo "exiting..."
                exit 1
        elif [[ $answer == "y" ]]; then
                echo "overwriting..."
                rm $output
        else
                echo "please give y or n, exiting..."
                exit 1
        fi
fi

checkconfig() 
{
  enabled=""
  if [[ $HSMetrics ]]; then
      enabled="$enabled HSmetrics,"
  fi
  if [[ $InsertSizeMetrics ]]; then
    enabled="$enabled insertSizeMetrics,"
  fi
  if [[ $AlignmentSummaryMetrics ]]; then
    enabled="$enabled AlignmentSummaryMetrics,"
  fi
  if [[ $FlagstatMetrics ]]; then
    enabled="$enabled FlagstatMetrics,"
  fi
  if [[ $gcBiasMetrics ]]; then
    enabled="$enabled gcBiasMetrics,"
  fi
  if [[ $QualityByCycleMetrics ]]; then
    enabled="$enabled QualityByCycleMetrics,"
  fi
  if [[ $QualityDistributionMetircs ]]; then
    enabled="$enabled QualityDistributionMetrics"
  fi
  if [[ $enabled == "" ]]; then
    echo "No files enabled, exiting..."
    exit 1
  fi
  echo "gathering: ${enabled}"
}
source $config
checkconfig

HERE=$PWD
counter=0
cd $directory # go to projects directory
total=`ls -l | grep -c ^d`
tmpdir=`echo "${HERE}/.tmpMetricsGatherDir/"`
rm -r "${tmpdir}"
mkdir "${tmpdir}"

setupFiles()
{
  if [[ $HSMetrics ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,BAIT_SET,GENOME_SIZE,BAIT_TERRITORY,TARGET_TERRITORY,BAIT_DESIGN_EFFICIENCY,TOTAL_READS,PF_READS,PF_UNIQUE_READS,PCT_PF_READS,PCT_PF_UQ_READS,PF_UQ_READS_ALIGNED,PCT_PF_UQ_READS_ALIGNED,PF_BASES_ALIGNED,PF_UQ_BASES_ALIGNED,ON_BAIT_BASES,NEAR_BAIT_BASES,OFF_BAIT_BASES,ON_TARGET_BASES,PCT_SELECTED_BASES,PCT_OFF_BAIT,ON_BAIT_VS_SELECTED,MEAN_BAIT_COVERAGE,MEAN_TARGET_COVERAGE,MEDIAN_TARGET_COVERAGE,PCT_USABLE_BASES_ON_BAIT,PCT_USABLE_BASES_ON_TARGET,FOLD_ENRICHMENT,ZERO_CVG_TARGETS_PCT,PCT_EXC_DUPE,PCT_EXC_MAPQ,PCT_EXC_BASEQ,PCT_EXC_OVERLAP,PCT_EXC_OFF_TARGET,FOLD_80_BASE_PENALTY,PCT_TARGET_BASES_1X,PCT_TARGET_BASES_2X,PCT_TARGET_BASES_10X,PCT_TARGET_BASES_20X,PCT_TARGET_BASES_30X,PCT_TARGET_BASES_40X,PCT_TARGET_BASES_50X,PCT_TARGET_BASES_100X,HS_LIBRARY_SIZE,HS_PENALTY_10X,HS_PENALTY_20X,HS_PENALTY_30X,HS_PENALTY_40X,HS_PENALTY_50X,HS_PENALTY_100X,AT_DROPOUT,GC_DROPOUT,HET_SNP_SENSITIVITY,HET_SNP_Q,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/hsMetrics.csv"
  fi
  if [[ $InsertSizeMetrics ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,MEDIAN_INSERT_SIZE,MEDIAN_ABSOLUTE_DEVIATION,MIN_INSERT_SIZE,MAX_INSERT_SIZE,MEAN_INSERT_SIZE,STANDARD_DEVIATION,READ_PAIRS,PAIR_ORIENTATION,WIDTH_OF_10_PERCENT,WIDTH_OF_20_PERCENT,WIDTH_OF_30_PERCENT,WIDTH_OF_40_PERCENT,WIDTH_OF_50_PERCENT,WIDTH_OF_60_PERCENT,WIDTH_OF_70_PERCENT,WIDTH_OF_80_PERCENT,WIDTH_OF_90_PERCENT,WIDTH_OF_99_PERCENT,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/insertSizeMetrics.csv"
  fi
  if [[ $AlignmentSummaryMetrics ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,CATEGORY,TOTAL_READS,PF_READS,PCT_PF_READS,PF_NOISE_READS,PF_READS_ALIGNED,PCT_PF_READS_ALIGNED,PF_ALIGNED_BASES,PF_HQ_ALIGNED_READS,PF_HQ_ALIGNED_BASES,PF_HQ_ALIGNED_Q20_BASES,PF_HQ_MEDIAN_MISMATCHES,PF_MISMATCH_RATE,PF_HQ_ERROR_RATE,PF_INDEL_RATE,MEAN_READ_LENGTH,READS_ALIGNED_IN_PAIRS,PCT_READS_ALIGNED_IN_PAIRS,BAD_CYCLES,STRAND_BALANCE,PCT_CHIMERAS,PCT_ADAPTER,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/AlignmentSummaryMetrics.csv"
  fi
  if [[ $FlagstatMetrics ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,TOTAL_PASS,TOTAL_FAIL,SECONDARY_PASS,SECONDARY_FAIL,SUPPLEMENTARY_PASS,SUPPLEMENTARY_FAIL,DUPLICATE_PASS,DUPLICATE_FAIL,MAPPED_PASS,MAPPED_FAIL,MAPPED_PCT,PAIRED_SEQ_PASS,PAIRED_SEQ_FAIL,R1_PASS,R1_FAIL,R2_PASS,R2_FAIL,PROPER_PAIR_PASS,PROPER_PAIR_FAIL,BOTH_MAPPED_PASS,BOTH_MAPPED_FAIL,SINGLETONS_PASS,SINGLETONS_FAIL,SINGLETONS_PCT,MATE_ON_DIFF_CHR_LOW_PASS,MATE_ON_DIFF_CHR_LOW_FAIL,MATE_ON_DIFF_CHR_HIGHQ_PASS,MATE_ON_DIFF_CHR_HIGHQ_FAIL,DATE" > "${tmpdir}/FlagstatMetrics.csv"
  fi
  if [[ $gcBiasMetrics ]]; then
    echo "PROJECT_ID,RUN,SAMPLE_ID,ACCUMULATION_LEVEL,READS_USED,GC,WINDOWS,READ_STARTS,MEAN_BASE_QUALITY,NORMALIZED_COVERAGE,ERROR_BAR_WIDTH,SAMPLE,LIBRARY,READ_GROUP,DATE" > "${tmpdir}/gcBiasMetrics.csv"
  fi
  if [[ $QualityByCycleMetrics ]]; then
    echo "tmpheader" > "${tmpdir}/QualityByCycleMetrics.csv"
  fi
  if [[ $QualityDistributionMetircs ]]; then
    echo "tmpheader" > "${tmpdir}/QualityDistributionMetrics.csv"
  fi
}

getDate() {
  DATE=`echo "${SampleEntry}" | grep -oP '(?<=,)(([1-2][0-9])((0[1-9])|(1[0-2]))((0[1-9])|(1[1-9])|(2[1-9])|(3[0-1])))(?=,)'`
}

hsMetrics()
{
  # Function to parse hsMetrics file
  # Adds entries to hsMetrics.csv
  cd "results/qc/statistics"
  for D in `find . -name "*.merged.dedup.bam.hs_metrics" -type f`
    do
      ROW=`head -n 8 "${D}" | tail -1 | tr '\t' ','` # get the hs metrics
      ID=`echo "${D}" | awk -F'.merged.dedup.bam.hs_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }'` # get the sample ID
      SampleEntry=`cat "../../${PROJECTID}.csv" | grep "${ID}"`
      getDate
      RowToInsert=`echo "${PROJECTID},${currentRunID},${ID},${ROW},${DATE}"`
      NumberOfCollumns=`echo "${RowToInsert}" | awk '{print gsub(/,/,"")}'`
      if [[ $NumberOfCollumns == 59 ]]; then # if colums are complete insert data in tmp file
        echo "${RowToInsert}" >> "${tmpdir}/hsMetrics.csv"
      fi
    done
  cd ../../../
}

isMetrics()
{
  # Function to parse insert size metrics file
  # Adds entries to insertSizeMetrics.csv
  cd "results/qc/statistics"
  for D in `find . -name "*.merged.dedup.bam.insert_size_metrics" -type f`
    do
      ROW=`head -n 8 "${D}" | tail -1 | tr '\t' ','` # get the insert size metrics
      ID=`echo "${D}" | awk -F'.merged.dedup.bam.insert_size_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }'` # get the sample ID
      SampleEntry=`cat "../../${PROJECTID}.csv" | grep "${ID}"`
      getDate
      RowToInsert=`echo "${PROJECTID},${currentRunID},${ID},${ROW},${DATE}"`
      NumberOfCollumns=`echo "${RowToInsert}" | awk '{print gsub(/,/,"")}'`
      if [[ $NumberOfCollumns == 24 ]]; then # if colums are complete insert data in tmp file
        echo "${RowToInsert}" >> "${tmpdir}/insertSizeMetrics.csv"
      fi
    done
  cd ../../../
}

asMetrics()
{
  # Function to parse alignment summary metrics file
  # Adds entries to alignment summary metrics.csv
  # each asm file contains 3 rows, first of pair, second of pair and pair.
  cd "results/qc/statistics"
  for D in `find . -name "*.merged.dedup.bam.alignment_summary_metrics" -type f`
    do
      ID=`echo "${D}" | awk -F'.merged.dedup.bam.alignment_summary_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }'`
      FIRST=`cat "${D}" | grep "^FIRST_OF_PAIR" | tr '\t' ','`
      SECOND=`cat "${D}" | grep "^SECOND_OF_PAIR" | tr '\t' ','`
      PAIR=`cat "${D}" | grep "^PAIR" | tr '\t' ','`
      SampleEntry=`cat "../../${PROJECTID}.csv" | grep "${ID}"`
      getDate
      RowToInsertFirst=`echo "${PROJECTID},${currentRunID},${ID},${FIRST},${DATE}"`
      RowToInsertSecond=`echo "${PROJECTID},${currentRunID},${ID},${SECOND},${DATE}"`
      RowToInsertPair=`echo "${PROJECTID},${currentRunID},${ID},${PAIR},${DATE}"`
      
      NumberOfCollumnsFirst=`echo "${RowToInsertFirst}" | awk '{print gsub(/,/,"")}'`
      NumberOfCollumnsSecond=`echo "${RowToInsertSecond}" | awk '{print gsub(/,/,"")}'`
      NumberOfCollumnsPair=`echo "${RowToInsertPair}" | awk '{print gsub(/,/,"")}'`
      
      if [[ $NumberOfCollumnsFirst == 28 ]] && [[ $NumberOfCollumnsSecond == 28 ]] &&  [[ $NumberOfCollumnsPair == 28 ]]; then
         echo $RowToInsertFirst >> "${tmpdir}/AlignmentSummaryMetrics.csv"
         echo $RowToInsertSecond >> "${tmpdir}/AlignmentSummaryMetrics.csv"
         echo $RowToInsertPair >> "${tmpdir}/AlignmentSummaryMetrics.csv"
      fi
    done
  cd ../../../
}

flMetrics()
{
  # Function to parse and store flagstat metrics
  # the flagstat metrics file has many entries in a little complex format
  # PROJECT_ID,RUN,SAMPLE_ID,TOTAL_PASS,TOTAL_FAIL,SECONDARY_PASS,SECONDARY_FAIL,SUPPLEMENTARY_PASS,SUPPLEMENTARY_FAIL,DUPLICATE_PASS,DUPLICATE_FAIL,MAPPED_PASS,MAPPED_FAIL,MAPPED_PCT,PAIRED_SEQ_PASS,PAIRED_SEQ_FAIL,R1_PASS,R1_FAIL,R2_PASS,R2_FAIL,PROPER_PAIR_PASS,PROPER_PAIR_FAIL,BOTH_MAPPED_PASS,BOTH_MAPPED_FAIL,SINGLETONS_PASS,SINGLETONS_FAIL,SINGLETONS_PCT,MATE_ON_DIFF_CHR_LOW_PASS,MATE_ON_DIFF_CHR_LOW_FAIL,MATE_ON_DIFF_CHR_HIGHQ_PASS,MATE_ON_DIFF_CHR_HIGHQ_FAIL,DATE
  cd "results/qc/statistics"
  for D in `find . -name "*.merged.dedup.bam.flagstat" -type f`
    do
      ID=`echo "${D}" | awk -F'.merged.dedup.bam.flagstat' '{ print $1 }' | awk -F'./' '{ print $2 }'`
      lineIndex=0
      ROW="${PROJECTID},${currentRunID},${ID}"
      while IFS='' read -r line; do
        let "lineIndex++"
        if [[ $lineIndex == 5 ]] || [[ $lineIndex == 9 ]] || [[ $lineIndex == 11 ]]; then
          PassFail=`echo $line | grep -oP '[0-9]+\s\+\s[0-9]+'`
          PCT=`echo $line | grep -oP '(?<=\()[0-9][0-9]\.[0-9][0-9](?=\%)'`
          ROW="${ROW},${PassFail/ + /,},${PCT}"
        else
          PassFail=`echo $line | grep -oP '[0-9]+\s\+\s[0-9]+'`
          ROW="${ROW},${PassFail/ + /,}"
        fi
      done < "$D"
      SampleEntry=`cat "../../${PROJECTID}.csv" | grep "${ID}"`
      getDate
      ROW="${ROW},${DATE}"
      echo "$ROW" >> "${tmpdir}/FlagstatMetrics.csv"
    done
  cd ../../../
}

gcbMetrics() 
{
  # gc Bias Metrics tail -n +7 20101533_6090566_DNA127819_579467_QXTR952_S07604514.merged.dedup.bam.gc_bias_metrics
  # not implemented
  cd "results/qc/statistics"
  for D in `find . -name "*.merged.dedup.bam.gc_bias_metrics" -type f`
    do
      ID=`echo "${D}" | awk -F'.merged.dedup.bam.gc_bias_metrics' '{ print $1 }' | awk -F'./' '{ print $2 }'`
      prefix="${PROJECTID},${currentRunID},${ID},"
      SampleEntry=`cat "../../${PROJECTID}.csv" | grep "${ID}"`
      getDate
      suffix=",${DATE}"
      tail -n +8 $D | tr "\t" "," | grep . | awk -v prefix="$prefix" -v suffix="$suffix" '{print prefix $0 suffix}' >> "${tmpdir}/gcBiasMetrics.csv"
  done
}

qbcMetrics()
{
  # Quality by cycle metrics
  # not implemented
  echo "test" >> "${tmpdir}/QualityByCycleMetrics.csv"
}

qdMetrics()
{
  # Quality distribution metrics
  # not implemented
  echo "test" >> "${tmpdir}/QualityDistributionMetrics.csv"
}


setupFiles # Generate empty files with headers

for project in `find . -maxdepth 1 -mindepth 1 -type d`
  do
      cd $project
      PROJECTID=`basename "$PWD"`
      progress=$(($counter*100/$total))
      echo -ne " ${progress}% of directories searched (${counter}/${total}) Project: ${PROJECTID}\r" # Progress indicator
      let "counter++" # Progress counter
      
      # for run in project
      for run in `find . -maxdepth 1 -mindepth 1 -type d`
        do
          cd $run
          if [[ -d "results/qc/statistics/" ]] && [[ -f "results/${PROJECTID}.csv" ]]; then
            currentRunID=`basename "$PWD"`
            
            if [[ $HSMetrics ]]; then
              hsMetrics
            fi
            if [[ $InsertSizeMetrics ]]; then
              isMetrics
            fi
            if [[ $AlignmentSummaryMetrics ]]; then
              asMetrics
            fi
            if [[ $FlagstatMetrics ]]; then
              flMetrics
            fi
            if [[ $gcBiasMetrics ]]; then
              gcbMetrics
            fi
            if [[ $QualityByCycleMetrics ]]; then
              qbcMetrics
            fi
            if [[ $QualityDistributionMetircs ]]; then
              qdMetrics
            fi
          fi
          cd ..
        done
      cd ..
  done

cd $HERE
echo -ne '\n'
echo "Completed gathering metrics from ${total} directories"
echo ""
echo "Compressing results to ${output}"
mv $tmpdir "gatheredMetrics"
zip -r $output "gatheredMetrics"
echo "Removing temporary files...."
rm -r "gatheredMetrics"
echo "Finished"

exit 1
