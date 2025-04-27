#!/usr/bin/env python3

import sys
from Bio import SeqIO

def find_motif_sites(fasta_path, bed_path, motif):
    """Find all occurrences of a motif in a FASTA file and create BED entries (3 columns only)."""
    motif = motif.upper()
    motif_len = len(motif)

    with open(bed_path, 'w') as bed_file:
        for record in SeqIO.parse(fasta_path, "fasta"):
            chrom = record.id
            seq = str(record.seq).upper()
            for i in range(len(seq) - motif_len + 1):
                if seq[i:i+motif_len] == motif:
                    bed_entry = (chrom, i, i + motif_len)
                    bed_file.write("\t".join(map(str, bed_entry)) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python find_motif_sites.py <input.fasta> <output.bed> <motif>")
        sys.exit(1)
    fasta_path = sys.argv[1]
    bed_path = sys.argv[2]
    motif = sys.argv[3]
    find_motif_sites(fasta_path, bed_path, motif)

