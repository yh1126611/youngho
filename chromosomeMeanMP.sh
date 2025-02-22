#!/bin/bash
# This code takes an input file from user (CG.mp) which has 4 columns where the 1st three columns are genomic coordinates (chromosome - start - end) and the 4th column is the modification probability.
# It returns the average modification probability of each chromosome.

# Prompt the user for the input file
read -p "Enter the input file name: " input_file

# Check if the file exists
if [ ! -f "$input_file" ]; then
    echo "Error: File '$input_file' not found."
    exit 1
fi

# Process the input file and store unique values
unique_values=$(mawk -v FS="\t" -v OFS="\t" '{print $1}' "$input_file" | sort | uniq)

# Process each unique value
while IFS= read -r line; do
    result=$(mawk -v FS="\t" -v OFS="\t" -v val="$line" '$1==val{sum+=$4; n++}END{print sum/n}' "$input_file")
    echo -e "$line\t$result"
done <<< "$unique_values"
