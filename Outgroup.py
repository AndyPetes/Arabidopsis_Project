#Usage:  python Outgroup.py Updated1001.txt AllThLyHaPe.txt EST.Loc.Thal.Lyr.Hall.Per.txt 3 > AlleleInference.output
#Exact Usage: python Outgroup2.py ../../Thaliana/Updated1001.txt ../Pvalue/ThLyHaPe/AllLocThLyHaPe.txt ../EST.Loc.Thal.Lyr.Hall.Per.txt
# 3 > ThLyHaPe.Allele.Output
#Input Files:
#sys.argv[1] = Updated1001.txt
#sys.argv[2] = AllLocThLyHaPe.txt
#sys.argv[3] = EST.Loc.Thal.Lyr.Hall.Per.txt
#sys.argv[4] = Number of Outgroups (i.e. 2 or 3)
import sys

Dic_Ref = {}
Dic_Alt = {}


#Create Dictionary from 1001.vcf file
with open(sys.argv[1],"r") as IN:
       	for line in IN:
               	if line.startswith("#"):
                       	continue
               	fields = line.strip("\n").split(" ")
               	Chromosome = fields[0]
               	Position = str(fields[1])
               	Reference = fields[2]
               	Alternative = fields[3]
               	if len(Reference) == 1 and len(Alternative) == 1:
                    Dic_Ref[Chromosome + "_" + Position] = Reference
                    Dic_Alt[Chromosome + "_" + Position] = Alternative

#Create Dictionary of Locations with Probabilities that the allele is ancestral
Allele_Prob = {}
with open(sys.argv[2],"r") as IN:
       	for line in IN:
               	fields = line.strip("\n").split(" ")
               	new_fields = fields[0]
               	Location = new_fields.split("\t")[0]
               	Probability = fields[-6]
               	Allele_Prob[Location] = Probability

#Create Output for Ancestral Allele States
with open(sys.argv[3],"r") as IN:
        for line in IN:
                if sys.argv[4] == "2":
                     fields = line.strip("\n").split("\t")
                     Outgroup1 = fields[-2]
                     Outgroup2 = fields[-1]
                     Loc = fields[0]
                     Prob = Allele_Prob[Loc]
                     if Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0":
                          print(Loc + "\t" + "NA")
                     elif float(Prob) >= 0.5:
                          print(Loc + "\t" + Dic_Ref[Loc] + "\t" + "Ancestral")
                     else:
                          print(Loc + "\t" + Dic_Alt[Loc] + "\t" + "Derived")
                if sys.argv[4] == "3":
                     fields = line.strip("\n").split("\t")
                     Outgroup1 = fields[-3]
                     Outgroup2 = fields[-2]
                     Outgroup3 = fields[-1]
                     Loc = fields[0]
                     Prob = Allele_Prob[Loc]
                     if Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0" and Outgroup3 == "0,0,0,0":
                          print(Loc + "\t" + "NA")
                     elif float(Prob) >= 0.5:
                          print(Loc + "\t" + Dic_Ref[Loc] + "\t" + "Ancestral")
                     else:
                          print(Loc + "\t" + Dic_Alt[Loc] + "\t" + "Derived")
