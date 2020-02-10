#!/bin/bash
touch ~/.tmpGISM
echo "PROJECT_ID SAMPLE_ID MEDIAN_INSERT_SIZE	MEDIAN_ABSOLUTE_DEVIATION	MIN_INSERT_SIZE	MAX_INSERT_SIZE	MEAN_INSERT_SIZE	STANDARD_DEVIATION	READ_PAIRS	PAIR_ORIENTATION	WIDTH_OF_10_PERCENT	WIDTH_OF_20_PERCENT	WIDTH_OF_30_PERCENT	WIDTH_OF_40_PERCENT	WIDTH_OF_50_PERCENT	WIDTH_OF_60_PERCENT	WIDTH_OF_70_PERCENT	WIDTH_OF_80_PERCENT	WIDTH_OF_90_PERCENT	WIDTH_OF_99_PERCENT	SAMPLE	LIBRARY	READ_GROUP" > ~/.tmpGISM

for project in `find . -maxdepth 1 -mindepth 1 -type d`
  do
    for D in `find $project/run01/results/qc/statistics/ -name "*.insert_size_metrics" -type f`
      do
        ROW=`head -n 8 "${D}" | tail -1`
        ID=`echo "${D}" | cut -d '/' -f 7 | cut -d '.' -f 1`
        PROJECTID=`echo "${D}" | cut -d '/' -f 2`
        echo $ID
        echo ${PROJECTID} ${ID} ${ROW} >> ~/.tmpGISM
      done
  done



