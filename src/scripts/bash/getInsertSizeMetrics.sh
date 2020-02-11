#!/bin/bash
helpFunction()
{
   echo ""
   echo "Gets the insertsize metrics contained in each project"
   echo ""
   echo "Usage: $0 -d directory -o output"
   echo -e "\t-d Path to directory to search"
   echo -e "\t-o Path to output file"
   exit 1 # Exit script after printing help
}

while getopts "d:o:" opt
do
   case "$opt" in
      d ) directory="$OPTARG" ;;
      o ) output="$OPTARG" ;;
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
if [[ -f $output ]]; then
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

touch $output
HERE=$PWD
counter=0
cd $directory
total=`ls -l | grep -c ^d`
tmp="${HERE}/.insertSizeTmpStorage"
touch $tmp
echo "PROJECT_ID,SAMPLE_ID,MEDIAN_INSERT_SIZE,MEDIAN_ABSOLUTE_DEVIATION,MIN_INSERT_SIZE,MAX_INSERT_SIZE,MEAN_INSERT_SIZE,STANDARD_DEVIATION,READ_PAIRS,PAIR_ORIENTATION,WIDTH_OF_10_PERCENT,WIDTH_OF_20_PERCENT,WIDTH_OF_30_PERCENT,WIDTH_OF_40_PERCENT,WIDTH_OF_50_PERCENT,WIDTH_OF_60_PERCENT,WIDTH_OF_70_PERCENT,WIDTH_OF_80_PERCENT,WIDTH_OF_90_PERCENT,WIDTH_OF_99_PERCENT,SAMPLE,LIBRARY,READ_GROUP" > $tmp
for project in `find . -maxdepth 1 -mindepth 1 -type d`
  do
    let "counter++"
    if [[ -d "${project}/run01/results/qc/statistics/" ]]; then
      for D in `find $project/run01/results/qc/statistics/ -name "*.insert_size_metrics" -type f`
        do
          ROW=`head -n 8 "${D}" | tail -1 | tr '\t' ','`
          ID=`echo "${D}" | cut -d '/' -f 7 | cut -d '.' -f 1`
          PROJECTID=`echo "${D}" | cut -d '/' -f 2`
          RowToInsert=`echo "${PROJECTID},${ID},${ROW}"` 
          NumberOfCollumns=`echo "${RowToInsert}" | awk '{print gsub(/,/,"")}'`
          if [[ $NumberOfCollumns == 22 ]]; then
            echo "${RowToInsert}" >> $tmp
          fi
        done
    fi
    progress=$(($counter*100/$total))
    echo -ne "${progress}% of directories searched\r"
  done
  
cd $HERE
mv $tmp $output
echo -ne '\n'



