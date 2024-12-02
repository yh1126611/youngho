# This code calculates occurrences, lengths, CG content and mod. prob. of all statistics related to an element and its species-specific sites.
# Required files are explained in: https://docs.google.com/document/d/12fe9fkPvKYbrNfBPu1DjIuI3yLl5GsFMmJdO_J4xzyw/edit

import re
import subprocess
import pandas as pd

chromosomes = []
for line in open("chromosomes.genome"):
    chromosomes.append(re.sub("chr", "", re.split("\s+", line.strip())[0]))
elemental_stats = pd.DataFrame(columns = chromosomes)

code = open("code.txt")

temp_list=[]
for line in code:
    print(line)
    line=line.strip()
    result = subprocess.run(line, shell=True, executable='/bin/bash')
