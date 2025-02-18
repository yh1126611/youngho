#!/bin/bash

# Input files
INPUT_FILE="your_file.txt"   # Tab-delimited input with chr, coord, strand
GENOME_FILE="your_genome.fa"
OUTPUT_FILE="gc_content.tsv"

# Step 1: Generate 100 bp windows from -10,000 to +10,000
awk -v OFS="\t" '{
    chrom = $1;
    pos = $2;
    strand = $3;
    for (i = -10000; i < 10000; i += 100) {
        start = pos + i;
        end = start + 100;
        print chrom, start, end, pos, strand, i;
    }
}' "$INPUT_FILE" > temp_windows.bed

# Step 2: Extract sequences using bedtools
bedtools getfasta -fi "$GENOME_FILE" -bed temp_windows.bed -fo temp_sequences.fa

# Step 3: Compute GC content and format output
awk '
    BEGIN { print "Chromosome_Coordinate\tGC_Content\tDistance\tStrand" }
    NR % 2 == 0 {
        seq = toupper($0);
        gc = gsub(/[GC]/, "", seq);
        print chrom_coord, gc / length(seq), dist, strand;
    }
    NR % 2 == 1 {
        split(substr($0, 2), arr, ":|-");
        chrom_coord = arr[1] "&" arr[2];
        dist = arr[3];
        strand = arr[4];
    }
' temp_sequences.fa > "$OUTPUT_FILE"

# Cleanup
rm temp_windows.bed temp_sequences.fa

echo "GC content computed and saved in $OUTPUT_FILE"
