# check each common kmers in all samples
while IFS= read -r line; do   res=$(grep -m 1 "$line" all_exons_sequences.fa);   res1=$(grep -B 1 -m 1 "$line" all_exons_sequences.fa | head -n 1);   if [ -n "$res" ]; then     echo "$line";     echo "$res1";   fi; done < first_4890_most_frequent_sequences.txt



cut -d , -f 6 Final.log  |sort |  uniq -c | sort -k2n

sort -t ',' -k6nr Final.log | more

# find the lines before papern 
grep -n "GGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCC" merged_genes.fa | awk -F: '{print $1 - 1}' | xargs -I {} sed -n '{}p' merged_genes.fa
# found the pattern shared among all patterns 
awk -F',' '{print $4}' example.log | sort | uniq -c | sort -n

# report only nam eof genes inclusing pattern
awk '/GCCCGGCTAATTTTTTGTATTTTTAGTAGAGACGGGGTTTCAC/ {if (NR>1) print prev} {prev=$0}' merged_genes.fa

# report more frqeuend kmers in all smaples
awk -F',' '{print $4}' example.log | sort | uniq -c | sort -nr | more
