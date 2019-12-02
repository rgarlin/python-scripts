#!/usr/bin/python3.6


## Opens up files as sets and then wites the 
## differences between the total and each 
## individual file 
#######################

import argparse

parser = argparse.ArgumentParser(description='Input file names: file1.csv, file2.csv, and total.csv')
parser.add_argument('file1')
parser.add_argument('file2')
parser.add_argument('total')

args = parser.parse_args()


def file_write(set_name, letter):
    for hosts3 in set_name:
        hosts3 = hosts3.rstrip()
        letter.write(hosts3 + '\n')

def lower_case(file_name, empty_list):
    for hosts in file_name:
        hosts = hosts.lower()
        empty_list.append(hosts)
    return(empty_list)


print('\n')
print('The output files will be output1.csv, output2.csv and total.csv')
print('\n')

## Convert to Lower Case as a list 
file1list = []
file2list = []
totallist = []

lower_file1 = open(args.file1, 'r')
lower_file2 = open(args.file2, 'r')
lower_total = open(args.total, 'r')

lower_case(lower_file1, file1list)
lower_case(lower_file2, file2list)
lower_case(lower_total, totallist)



## Files for writing 
e = open('output1.csv', 'w')
f = open('output2.csv', 'w')
h = open('totaloutput.csv', 'w')

## Files to open to create set 
set1 = set(file1list)
set2 = set(file2list)
settotal = set(totallist)

## Diff of total - file
diff1 = (settotal - set1)
diff2 = (settotal - set2)

file_write(diff1, e)
file_write(diff2, f)
file_write(settotal, h)

e.close()
f.close()
h.close()
