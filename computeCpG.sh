# Check if required arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <genome.fasta> <coordinates.txt> <output.tsv>"
    exit 1
fi

genome_file=$1
coord_file=$2
output_file=$3

# Function to calculate CpG ratio
calculate_cpg() {
    local seq=$(echo $1 | tr '[:lower:]' '[:upper:]')  # Convert to uppercase
    local cpg_count=$(echo $seq | grep -o 'CG' | wc -l)
    local total_count=${#seq}  # Total number of letters in the sequence
    echo "scale=4; ($cpg_count * 2) / $total_count" | bc
}

# Create header for output file
echo -e "Chromosome_Coordinate\tDistance\tCpG_Ratio\tStrand" > $output_file

# Process each entry in the coordinate file
while IFS=$'\t' read -r chrom coord strand; do
    for distance in $(seq -10000 100 10000); do
        start=$((coord + distance))
        
        # Extract 100bp sequence
        seq=$(samtools faidx $genome_file ${chrom}:${start}-$((start+99)) | tail -n +2 | tr -d '\n')
        
        # Calculate CpG ratio
        cpg_ratio=$(calculate_cpg $seq)
        
        # Output results
        echo -e "${chrom}_${coord}\t${distance}\t${cpg_ratio}\t${strand}" >> $output_file
    done
done < $coord_file

echo "CpG ratio analysis complete. Results saved in $output_file"
