#!/usr/bin/python3

import os
import sys
import numpy as np

n = int(os.getenv("N"))

prev_key = None
list_a = np.empty(n)
list_b = np.empty(n)
for line in sys.stdin:
    key, val = line.split('\t')
    key = key.split()
    val = val.split()

    i, k = int(key[0]), int(key[1])
    matr = val[0]
    j = int(val[1])
    elem = float(val[2])

    if (key != prev_key) and (prev_key is not None):
        print ('%s,%s\t%.5f' % (prev_key[0], prev_key[1], np.dot(list_a, list_b)))
    
    if matr == 'A':
        list_a[j] = elem
    elif matr == 'B':
        list_b[j] = elem

    prev_key = key
if prev_key is not None:
    print ('%s,%s\t%.5f' % (prev_key[0], prev_key[1], np.dot(list_a, list_b)))
