#python reformat.py unique.txt > unique.updated.txt
#sys.argv[1] = unique.txt

import sys
from collections import defaultdict
Location_Dic = defaultdict(list)


with open(sys.argv[1],"r") as IN:
        for line in IN:
            fields = line.strip("\n").split(" ")
            print(fields[0] + "\t" + fields[1])

