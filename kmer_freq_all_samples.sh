#!/bin/bash

# Input file
input_file="$1"
# Output file
output_file="$2"

# Use awk to count frequencies of values in the 4th column
# and store them in an associative array
declare -A frequencies
while IFS=, read -r _ _ _ value _; do
    (( frequencies[$value]++ ))
done < "$input_file"

# Process input file and append frequency as an extra column
while IFS=, read -r col1 col2 col3 value col5; do
    # Get frequency from the associative array
    frequency=${frequencies[$value]}
    # Append frequency as an extra column to the current line
    echo "$col1,$col2,$col3,$value,$col5,$frequency"
done < "$input_file" > "$output_file"

echo "Output written to $output_file"

