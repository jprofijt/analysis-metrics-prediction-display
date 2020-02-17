#! /bin/bash

helpFunction()
{
   echo ""
   echo "Gets the insertsize metrics contained in each project"
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
  return `cat $1 | grep $2 | cut -d',' -f $3`
}

checkDate() {
  if [[ ! $1 =~ ^[0-9]+$ ]]; then
    return 0
  else
    return 1
  fi
}



HERE=$PWD
counter=0
cd $directory # go to projects directory
total=`ls -l | grep -c ^d`
tmp="${HERE}/.insertSizeTmpStorage"
touch $tmp
echo "PROJECT_ID,SAMPLE_ID,MEDIAN_INSERT_SIZE,MEDIAN_ABSOLUTE_DEVIATION,MIN_INSERT_SIZE,MAX_INSERT_SIZE,MEAN_INSERT_SIZE,STANDARD_DEVIATION,READ_PAIRS,PAIR_ORIENTATION,WIDTH_OF_10_PERCENT,WIDTH_OF_20_PERCENT,WIDTH_OF_30_PERCENT,WIDTH_OF_40_PERCENT,WIDTH_OF_50_PERCENT,WIDTH_OF_60_PERCENT,WIDTH_OF_70_PERCENT,WIDTH_OF_80_PERCENT,WIDTH_OF_90_PERCENT,WIDTH_OF_99_PERCENT,SAMPLE,LIBRARY,READ_GROUP,DATE" > $tmp # File header
for project in `find . -maxdepth 1 -mindepth 1 -type d`
  do
    
    PROJECTID=`echo "${project}" | cut -c 3-` # remove root folder './'
    progress=$(($counter*100/$total))
    echo -ne " ${progress}% of directories searched (${counter}/${total}) Project: ${PROJECTID}\r" # Progress indicator
    let "counter++" # Progress counter
    
    
    if [[ -d "${project}/run01/results/qc/statistics/" ]] && [[ -f "${project}/run01/results/${PROJECTID}.csv" ]]; then # if project has a results file, and a sample sheet start retrieving insertsizes
      for D in `find $project/run01/results/qc/statistics/ -name "*.insert_size_metrics" -type f` # for insert size metrics file
        do
          ROW=`head -n 8 "${D}" | tail -1 | tr '\t' ','` # get the distribution metrics
          ID=`echo "${D}" | cut -d '/' -f 7 | cut -d '.' -f 1` # get the sample ID
          sampleSheet= "${project}/run01/results/${PROJECTID}.csv"
          
          DATE=$(getSampleSheetDate() $sampleSheet $ID 18) # get the sequencing start date from samplesheet
          
          if [[ checkDate() $DATE ]]; then # if date is not numeric, try previous column
            DATE=$(getSampleSheetDate() $sampleSheet $ID 17)
            if [[ checkDate() $DATE ]]; then # if date is still not numeric, try next column
              DATE=$(getSampleSheetDate() $sampleSheet $ID 19)
              if [[ checkDate() $DATE ]]; then # finally skip this file if no date can be parsed
                continue
              fi
            fi
          fi
          
          RowToInsert=`echo "${PROJECTID},${ID},${ROW},${DATE}"` # create the new row
          NumberOfCollumns=`echo "${RowToInsert}" | awk '{print gsub(/,/,"")}'` # count the collums
          
          if [[ $NumberOfCollumns == 23 ]]; then # if colums are complete insert data in tmp file
            echo "${RowToInsert}" >> $tmp
          fi
        done 
    fi
  done
  
cd $HERE
mv $tmp $output # mv tmp file to output file
echo -ne '\n'
echo "Completed gathering insertsize metrics from ${total} directories"

exit 1



