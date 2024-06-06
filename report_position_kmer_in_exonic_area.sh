#!/bin/bash

# Define the kmer to search for
kmer="$1"
# Define the number of matches to report
num_matches=${2:-1}

# Read the file into an array
mapfile -t lines < all_exons_sequences.fa

# Initialize a flag to indicate if any match was found
match_found=false
match_count=0

# Iterate over the array
for ((i = 0; i < ${#lines[@]}; i++)); do
  # Check if the current line contains the kmer
  if [[ "${lines[$i]}" == *"$kmer"* ]]; then
    # Find all occurrences of the kmer in the current line
    while IFS=: read -r position match; do
      # Print the kmer
      echo "${kmer}"

      # Print the previous line (header line)
      if (( i > 0 )); then
        prev_line="${lines[$i-1]}"
        echo "$prev_line"

        # Extract the chromosome and starting position of the exon
        chr_exon=$(echo "$prev_line" | awk -F':|-' '{print $1}')
        start_position_exon=$(echo "$prev_line" | awk -F':|-' '{print $2}')

        # Calculate the starting position of the kmer in the genome
        start_position_kmer_in_genome=$((position + start_position_exon + 1))
        end_position_kmer_in_genome=$((start_position_kmer_in_genome + ${#match} - 1))

        # Print the match with its position in red
        tput setaf 1
        echo "$chr_exon:$start_position_kmer_in_genome-$end_position_kmer_in_genome:$match"
        tput sgr0

        # Set the flag to indicate that at least one match was found
        match_found=true
        match_count=$((match_count + 1))

        # Check if the number of matches reported has reached the specified limit
        if [ "$match_count" -ge "$num_matches" ]; then
          break 2
        fi
      fi
    done < <(grep -o -b "$kmer" <<< "${lines[$i]}")
  fi
done

# If no match was found, print a message in blue
blue=$(tput setaf 4)      # Blue color
reset=$(tput sgr0)        # Reset color
if [ "$match_found" = false ]; then
  echo "${blue}The kmer '$kmer' was not found in the file${reset}"
fi

# Print the separator line after all matches are processed
echo "---------------------------------------------"
