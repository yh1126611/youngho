# Takes as input the "sequence_report" file from NCBI for reference genome assemblies and fixes chromosome names from the GenBank/RefSeq names to simple number format (e.g. 1, 2... X, Y)
# The sequence_report file must have simple number format chr. names on column 4 and GenBank format chr. names on column 7 / RefSeq format chr. names on column 10
# The sequence_report file must specify if the chromosome is an assembled molecule (by having the value 'assembled-molecule') in a column
import re
import subprocess

file_name = input("Enter name of file to fix chromosome names for (incl. extension): ")
sequence_report_name = input("Enter sequence report file name (incl. extension): ")
current_format = input("Which column contains the current chromosome names:(col. no.):")
new_format = input("Which column contains the chromosome naming format you want to change into(col. no.):")
assembled_molecule = input("Which column tells you if the sequence is an assembled molecule (col. no.):")

current_format = int(current_format)
current_format_magic_no = current_format - 1
new_format = int(new_format)
new_format_magic_no = new_format - 1
assembled_molecule = int(assembled_molecule)
assembled_molecule_magic_no = assembled_molecule - 1

file = open(file_name, "r")
sequence_report = open(sequence_report_name, "r")
fixed_file = ".".join(re.split("\.", file_name)[:-1]) + "_chrNameFixed." + re.split("\.", file_name)[-1]

command = "sed"
count = 0

for sequence_report_line in sequence_report:
    current_name = re.split("\t", sequence_report_line)[current_format_magic_no]
    new_name = re.split("\t", sequence_report_line)[new_format_magic_no]
    if len(re.split("\t", sequence_report_line)) > assembled_molecule_magic_no:
        if re.split("\t|\n", sequence_report_line)[assembled_molecule_magic_no]=="assembled-molecule":
            if count == 0:
                command = ''.join([command, " '"])
            command = ''.join([command, "s/", current_name, "/", new_name, "/g;"])
            count+=1
command = command[:-1] + "'"
command = ' '.join([command, file_name])
command = ' '.join([command, '>', fixed_file])
print(command)

subprocess.run(command, shell=True)
