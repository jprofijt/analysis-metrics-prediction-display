#!/bin/bash
#
# This File locates all runs with an Info folder. meaning they have usable illumnia InterOp data.
#


helpFunction()
{
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

# for each directory with an Info subdirectory log their locations
echo "Searching directories for Info folders..."
for D in `find $directory -mindepth 2 -maxdepth 2 -type d`
do
  if [[ $D =~ Info$ ]]; then
    echo $D >> $output
  fi
done