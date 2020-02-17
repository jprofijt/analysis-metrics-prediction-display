#! /bin/bash

helpFunction()
{
        echo ""
        echo "Gets the HS metrics contained in each project"
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

getSampleSheetDate() {
        # $1: Sample sheet csv
        # $2: Sample ID
        # $3: Column number
        echo  `cat $1 | grep $2 | cut -d',' -f $3`
}

checkDate() {
        if [[ $1 =~ ^[0-9]+$ ]]; then
                return 1
        else
                return 0
        fi
}



HERE=$PWD
counter=0
cd $directory # go to projects directory
total=`ls -l | grep -c ^d`
tmp="${HERE}/.hsmetricsTmpStorage"
touch $tmp
echo "PROJECT_ID, SAMPLE_ID,BAIT_SET,GENOME_SIZE,BAIT_TERRITORY,TARGET_TERRITORY,BAIT_DESIGN_EFFICIENCY,TOTAL_READS,PF_READS,PF_UNIQUE_READS,PCT_PF_READS,PCT_PF_UQ_READS,PF_UQ_READS_ALIGNED,PCT_PF_UQ_READS_ALIGNED,PF_BASES_ALIGNED,PF_UQ_BASES_ALIGNED,ON_BAIT_BASES,NEAR_BAIT_BASES,OFF_BAIT_BASES,ON_TARGET_BASES,PCT_SELECTED_BASES,PCT_OFF_BAIT,ON_BAIT_VS_SELECTED,MEAN_BAIT_COVERAGE,MEAN_TARGET_COVERAGE,MEDIAN_TARGET_COVERAGE,PCT_USABLE_BASES_ON_BAIT,PCT_USABLE_BASES_ON_TARGET,FOLD_ENRICHMENT,ZERO_CVG_TARGETS_PCT,PCT_EXC_DUPE,PCT_EXC_MAPQ,PCT_EXC_BASEQ,PCT_EXC_OVERLAP,PCT_EXC_OFF_TARGET,FOLD_80_BASE_PENALTY,PCT_TARGET_BASES_1X,PCT_TARGET_BASES_2X,PCT_TARGET_BASES_10X,PCT_TARGET_BASES_20X,PCT_TARGET_BASES_30X,PCT_TARGET_BASES_40X,PCT_TARGET_BASES_50X,PCT_TARGET_BASES_100X,HS_LIBRARY_SIZE,HS_PENALTY_10X,HS_PENALTY_20X,HS_PENALTY_30X,HS_PENALTY_40X,HS_PENALTY_50X,HS_PENALTY_100X,AT_DROPOUT,GC_DROPOUT,HET_SNP_SENSITIVITY,HET_SNP_Q,SAMPLE,LIBRARY,READ_GROUP,DATE" > $tmp

for project in `find . -maxdepth 1 -mindepth 1 -type d`
do

        PROJECTID=`echo "${project}" | cut -c 3-` # remove root folder './'
        progress=$(($counter*100/$total))
        echo -ne " ${progress}% of directories searched (${counter}/${total}) Project: ${PROJECTID}\r" # Progress indicator
        let "counter++" # Progress counter

    
    if [[ -d "${project}/run01/results/qc/statistics/" ]] && [[ -f "${project}/run01/results/${PROJECTID}.csv" ]]; then # if project has a results file, and a sample sheet start retrieving hs metrics 
      for D in `find $project/run01/results/qc/statistics/ -name "*.hs_metrics" -type f` # for metrics file in statistics folder
        do
          ROW=`head -n 8 "${D}" | tail -1 | tr '\t' ','` # get the hs metrics
          ID=`echo "${D}" | cut -d '/' -f 7 | cut -d '.' -f 1` # get the sample ID
          sampleSheet=`echo "${project}/run01/results/${PROJECTID}.csv"`
          
          DATE=$(getSampleSheetDate $sampleSheet $ID 18) # get the sequencing start date from samplesheet
          
          if [[ ! $(checkDate $DATE) ]]; then # if date is not numeric, try previous column
            DATE=$(getSampleSheetDate $sampleSheet $ID 17)
            if [[ ! $(checkDate $DATE) ]]; then # if date is still not numeric, try next column
              DATE=$(getSampleSheetDate $sampleSheet $ID 19)
              if [[ ! $(checkDate $DATE) ]]; then # finally skip this file if no date can be parsed
                continue
              fi
            fi
          fi
          
          RowToInsert=`echo "${PROJECTID},${ID},${ROW},${DATE}"` # create the new row
          NumberOfCollumns=`echo "${RowToInsert}" | awk '{print gsub(/,/,"")}'` # count the collums
          if [[ $NumberOfCollumns == 58 ]]; then # if colums are complete insert data in tmp file
            echo "${RowToInsert}" >> $tmp
          fi
        done 
    fi
  done
  
cd $HERE
echo -ne '\n'
if [[ $counter == $total ]]; then 
    mv $tmp $output # mv tmp file to output file
    echo "Completed gathering hs metrics from ${total} directories"
else
    mv $tmp $output # mv tmp file to output file
    echo "Failed gathering hs metrics ${counter}/${total}, moved successfull projects to output"
fi

exit 1



