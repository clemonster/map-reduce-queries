#!/usr/bin/python


#SELECT O.cid, SUM(total), COUNT(DISTINCT total) FROM Order O GROUP BY O.cid
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    if line is None:
        break
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words

    cid, total = line.split(',', 1)

    print(cid + ',' + total)
