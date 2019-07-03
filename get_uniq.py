import sys
from collections import defaultdict

par = sys.argv

hld = defaultdict(list)
dup = defaultdict(list)

with open(par[1]) as IN:
	for line in IN:
		fld = line.strip().split()
		if fld[0] in hld:
			dup[fld[0]] = fld[1]
		else:
			hld[fld[0]] = fld[1]

for k, v in dup.items():
	del hld[k]

for k,v in hld.items():
	print(k,v)
	
