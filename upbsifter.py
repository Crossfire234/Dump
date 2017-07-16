import csv
import numpy as np
import numbers
import re
h = [[]]
name = raw_input('What csv file would you like to open (give name without .csv at the end)? ')
date = raw_input('Give the date of the Sunday before the workweek (format: xx/xx/xxxx) ')
d = list(name)
o = list(date) #o[i], i in 0,9
print o
p = str(int(o[3] + o[4]) + 7)
list(p)
o[3] = p[0]
o[4] = p[1]
print d
print o
e = np.concatenate((d,['.','c','s','v']))
f = "".join(e)
print f
with open(f, 'rb') as a:
	b = csv.reader(a)
	for row in b:
		q = len(row)
		row_count = sum(1 for row in b) 
	c=[[None for x in np.arange(1,q)] for y in range(row_count)]
	print c[0][0]
	for row in b:
		x=[row]
		y = np.reshape(x,(q,1))
		for i in np.arange(1,q):
			c[
	print c[0][0]
print c
for i in np.arange(1,len(c),1):
	n = re.search("[0-" + o[0] + "][1-" + o[1] + "]/[0-" + o[3] + "][1-" + o[4] + "]/201[0-" + o[9] + "]",c[i])
	if n:
		h = np.concatenate((h,[c[i]]))
		for j in np.arange(i,len(c),1):
			m = re.search("\d*\.\d\d$",c[j])
			if m:
				h = np.concatenate((h,[c[j]]))
				break
print h
