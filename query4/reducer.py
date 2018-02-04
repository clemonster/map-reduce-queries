#!/usr/bin/python

#SELECT C.cid, O.total FROM Customer C, Order O WHERE C.cid=O.cid
import sys

#Initialize stuff
totals = []
OisMet = False
AisMet = False
current_cid = None
cid = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    line_split = line.split(',')
    cid = line_split[0]
    source = line_split[-1]

      
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: cid) before it is passed to the reducer

    #Check if we're still dealing with the same cid
    #If not, print the totals for the previous cid
    if current_cid != cid and current_cid is not None:
    	#Print if A and B are met
    	if CisMet and OisMet:
    		for t in totals:
    			print('%s,%s' % (current_cid, t))

    	#Reset everything
    	totals = []
    	current_cid = cid 
    	#We only need to change one isMet value to False
    	if source == 'C':
    		OisMet = False
    	if source == 'O':
    		CisMet = False

    #For the first line, we need to initialize current_cid
	if current_cid is None:
		current_cid = cid

    if source == 'C':
    	CisMet = True
    if source == 'O':
    	OisMet = True
    	totals.append(line_split[1])
        
# do not forget to output the last totals if needed!

if cid == current_cid:
	#print("I'm printing the last !")
	for t in totals:
		print("%s,%s" % (current_cid, t))


