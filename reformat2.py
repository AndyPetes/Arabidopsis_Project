#python reformat2.py unique.txt EST.All.$species.sort.txt > nonunique.txt
#sys.argv[1] = unique.updated.txt
#sys.argv[2] = EST.All.$species.sort.txt

import sys

Unique_Dict = {}

with open(sys.argv[1],"r") as IN:
       	for line in IN:
            fields = line.strip("\n").split("\t")
            Position = fields[0]
            Unique_Dict[Position] = "Unique"


with open(sys.argv[2],"r") as IN:
        for line in IN:
            fields = line.strip("\n").split("\t")
            Position = fields[0]
            if Position not in Unique_Dict:
                print(line.strip("\n"))
