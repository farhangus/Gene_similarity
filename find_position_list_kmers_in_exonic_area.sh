#!/bin/bash

# Set the default number of matches to 1
num_matches=1

# Check if the number of matches is provided as an argument
if [ $# -ge 1 ]; then
  num_matches=$1
fi

# Read the kmers from tmp.txt and call the helper script with the specified number of matches
while IFS= read -r line; do
  set -- $line
  bash report_position_kmer_in_exonic_area.sh "$2" "$num_matches"
done < tmp.txt
