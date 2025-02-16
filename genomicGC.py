# Creates a BED format file (GC.bed) with entries in coordinates of the input genome where the base is either G (g) or C (c).
# To be used in downstream analyses in which GC ratio of certain set of regions would be found by calculating its number of overlaps with the output of this script using other tools (e.g. bedtools intersect)
# Midfile created in the process (GC_midfile.bed) can be deleted after the script has finished running.
# By Young Ho Lee (yh1126@snu.ac.kr, https://github.com/yh1126611)

from Bio import SeqIO

genome = input("What is the name of your genome assembly file? (incl. ext.): ")

with open("GC_midfile.bed", "w") as out_file:
    for record in SeqIO.parse(genome, "fasta"):
        chrom = record.id
        for i, base in enumerate(record.seq):
            if base in {"G", "C", "g", "c"}:
                out_file.write(f"{chrom}\t{i}\t{i+1}\n")

import subprocess
command = "bedtools merge -i GC_midfile.bed > GC.bed" 
subprocess.run(command, shell=True)

