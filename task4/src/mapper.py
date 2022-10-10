#!/usr/bin/python3

import os
import sys

# Get current file name
path = os.getenv("mapreduce_map_input_file")
fname = os.path.split(path)[1]

sys.stderr.write(f'Current input file: {fname}\n')

m = int(os.getenv("M"))
n = int(os.getenv("N"))
k = int(os.getenv("K"))

for line in sys.stdin:
    sys.stderr.write('reporter:counter:Custom Counter,My Super INT Counter,1\n')

    elems = line.split()
    row = int(elems[0])
    if fname == 'A.txt':
        for i in range(1, len(elems)):
            elem = float(elems[i])
            for j in range(k):
                print('%d %d\t%s %d %.5f' % (row, j, 'A', i-1, elem))
    elif fname == 'B.txt':
        for k in range(1, len(elems)):
            elem = float(elems[k])
            for j in range(n):
                print('%d %d\t%s %d %.5f' % (j, k-1, 'B', row, elem))
