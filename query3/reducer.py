#!/usr/bin/python

#SELECT O.cid, SUM(total), COUNT(DISTINCT total) FROM Order O GROUP BY O.cid
import sys

cid = None
current_cid = None
current_sum = 0
current_count = 0
total = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    cid, total = line.split(',', 1)

    # convert count (currently a string) to int
    try:
        total = int(total)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # Check if we're still dealing with the same cid    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_cid == cid:
        current_sum += total
        current_count += 1
    else:
        if current_cid:
            # write result to STDOUT
            #print("I'm printing a current !")
            print("%s\t%s\t%s" % (current_cid, current_sum ,current_count))
        current_cid = cid
        current_sum = total
        current_count = 1
        

# do not forget to output the last word if needed!
if current_cid == cid:
	#print("I'm printing the last !")
    print("%s\t%s\t%s" % (current_cid, current_sum ,current_count))