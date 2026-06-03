# Generates a diced (i.e. every BED entry divided into lines of 1 bp with 4th column content preserved) version of a bedgraph file.

import re

bedfilename = input("Name of bedgraph file providing regional estimated MP?:")
bedfile = open(bedfilename, "r")
outfilename_array = re.split(r"\.", bedfilename)
outfilename_array.pop(-1)
outfilename = ".".join(outfilename_array)
outfilename = "".join([outfilename, "_perbase.mp"])
outfile = open(outfilename, "w")

for line in bedfile:
	items = re.split("\t", line)
	for i in range(int(items[1]), int(items[2])+1):
		outfile.write("\t".join([items[0], str(i), str(i+1), items[3]]))
outfile.write("\n")
