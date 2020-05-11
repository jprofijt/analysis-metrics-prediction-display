#! /bin/bash
helpFunction()
{
        echo ""
        echo "Gets the quality metrics for each project"
        echo ""
        echo "Usage: $0 -d directory -a summary -o output"
        echo -e "\t-d Path to directory to search"
        echo -e "\t-a Path to Summary application"
        echo -e "\t-o Path to sqlite db file"
        exit 1 # Exit script after printing help
}


directory="/home/jouke/Documents/Projects/Analysis-Metrics-Prediction/data/interop"
output="/home/jouke/Documents/Projects/Analysis-Metrics-Prediction/data/SQLITE/test.db"
application="/home/jouke/.Apps/InterOp/bin/summary"
# Print helpFunction in case parameters are empty
if [ -z "$directory" ] || [ -z "$output" ] || [ -z "$application"]
then
        echo "input: ${directory}"
        echo "output: ${output}"
        echo "summary app: ${application}"
        echo "Missing one or more parameters";
        helpFunction
fi

HERE=$PWD
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
counter=0
cd "$directory" || exit # go to interop directory
# shellcheck disable=SC2010
total=$(ls -l | grep -c ^d)
tmpdir="${HERE}/.tmpMetricsGatherDir/"

if [[ -d $tmpdir ]]; then
    rm -r "$tmpdir"
fi

mkdir "${tmpdir}"

while IFS= read -r -d '' run
  do
      runid=$(basename "$run")
      progress=$((counter*100/total))
      echo -ne " ${progress}% of directories searched (${counter}/${total}) Interop Run: ${runid}\r" # Progress indicator
      (( counter++ )) # Progress counter
      info="${run}/Info"
      python2 "/home/jouke/Documents/Projects/Analysis-Metrics-Prediction/src/scripts/python/ExecutableScripts/parseRunInfo.py" -r "${info}/RunInfo.xml" -i "${info}" -d "${output}" -e "${application}"
  done < <(find . -maxdepth 1 -mindepth 1 -type d -print0)


