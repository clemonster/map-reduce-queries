#!/usr/bin/python


#SELECT C.cid, O.total FROM Customer C, Order O WHERE C.cid=O.cid
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    if line is None:
        break
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words

    print(line)