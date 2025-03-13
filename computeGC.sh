#!/bin/bash

# Check if required arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <genome.fasta> <coordinates.txt> <output.tsv>"
    exit 1
fi

genome_file=$1
coord_file=$2
output_file=$3

# Function to calculate GC content
calculate_gc() {
    local seq=$1
    local gc_count=$(echo $seq | tr -cd 'GCgc' | wc -c)
    local total_count=${#seq}
    echo "scale=4; $gc_count / $total_count" | bc
}

# Create header for output file
echo -e "Chromosome_Coordinate\tDistance\tGC_Ratio\tStrand" > $output_file

# Process each entry in the coordinate file
while IFS=$'\t' read -r chrom coord strand; do
    for distance in $(seq -10000 100 10000); do
        start=$((coord + distance))
        
        # Extract 100bp sequence
        seq=$(samtools faidx $genome_file ${chrom}:${start}-$((start+99)) | tail -n +2 | tr -d '\n')
        
        # Calculate GC content
        gc_ratio=$(calculate_gc $seq)
        
        # Output results
        echo -e "${chrom}_${coord}\t${distance}\t${gc_ratio}\t${strand}" >> $output_file
    done
done < $coord_file

echo "GC content analysis complete. Results saved in $output_file"
