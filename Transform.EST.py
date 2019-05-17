import sys

#sort -k 1 Species.txt > Species.sort.txt
#Species Data = Output from MAF.Arabidopsis.py

#sort -k 1 Thaliana.txt > Thaliana.sort.txt
#Thaliana Data = Output from Loc_Ancestral.py

#sys.argv[1] = Sorted Species Data
#sys.argv[2] = Sorted Thaliana Data

Species_Dict = {}

with open(sys.argv[1],"r") as IN:
       	for line in IN:
               	fields = line.strip("\n").split(",")
               	Position = fields[0]
               	Species_Dict[Position] = line.strip("\n")

with open(sys.argv[2],"r") as IN:
       	for line in IN:
            fields = line.strip("\n").split(",")
            Position = fields[0]
            if Position not in Species_Dict:
               	print("%s,0,0,0,0"%(Position))
            else:
               	print(Species_Dict[Position])
