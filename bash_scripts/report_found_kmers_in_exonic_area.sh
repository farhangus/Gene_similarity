#!/bin/bash

# Set the default number of matches to 1
num_matches=1
kmer_frequency_file=$1
tmp_file=$(mktemp)
total_kmers_in_the_file=$(awk 'END {print NR}' $kmer_frequency_file)

# Check if the number of matches is provided as an argument
if [ $# -ge 1 ]; then
  num_matches=$2
fi

# Read the kmers from tmp.txt and call the helper script with the specified number of matches
while IFS= read -r line; do
  set -- $line
  bash report_position_kmer_in_exonic_area.sh "$2" "$num_matches" | tee -a $tmp_file
done < $kmer_frequency_file

total_number_not_found_kmers=$(grep -c -F "was not found in the file" $tmp_file)
printf "number of all given kmers: %d\n" $total_kmers_in_the_file
printf "number of not found kmers in exonic area: %d\n" $total_number_not_found_kmers
