#Usage:  python Outgroup.py Updated1001.txt AllThLyHaPe.txt EST.Loc.Thal.Lyr.Hall.Per.txt 3 > AlleleInference.output
#Exact Usage: python Outgroup2.py ../../Thaliana/Updated1001.txt ../Pvalue/ThLyHaPe/AllLocThLyHaPe.txt ../EST.Loc.Thal.Lyr.Hall.Per.txt 
# 3 > ThLyHaPe.Allele.Output
#Input Files:
#sys.argv[1] = Updated1001.txt
#sys.argv[2] = AllLocThLyHaPe.txt
#sys.argv[3] = EST.Loc.Thal.Lyr.Hall.Per.txt
#sys.argv[4] = Number of Outgroups (i.e. 2 or 3)
import sys

Dic_Minor = {}
Dic_Major = {}

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
                    New_Fields = fields[4].split(";")
                    Alt_Freq = float(New_Fields[2][3:])
                    if Alt_Freq < 0.5:
                        Dic_Minor[Chromosome + "_" + Position] = Alternative
                        Dic_Major[Chromosome + "_" + Position] = Reference 
                    else:
                        Dic_Minor[Chromosome + "_" + Position] = Reference
                        Dic_Major[Chromosome + "_" + Position] = Alternative

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
                     Alt_Prob = 1 - float(Allele_Prob[Loc])
                     if Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0" and float(Prob) >= 0.525:
                         print(Loc + "\t" + Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Ancestral" + "\t" + "No_Outgroup" + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Derived")
                     elif Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0" and float(Prob) <= 0.475:
                         print(Loc + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Ancestral" + "\t" + "No_Outgroup" + "\t" + Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Derived")
                     elif float(Prob) >= 0.525:
                         print(Loc + "\t" + Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Ancestral" + "\t" + "Yes_Outgroup" + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Derived")
                     elif float(Prob) <= 0.475:
                         print(Loc + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Ancestral" + "\t" + "Yes_Outgroup" +	"\t" +Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Derived")
                if sys.argv[4] == "3":
                     fields = line.strip("\n").split("\t")
                     Outgroup1 = fields[-3]
                     Outgroup2 = fields[-2]
                     Outgroup3 = fields[-1]
                     Loc = fields[0]
                     Prob = Allele_Prob[Loc]
                     Alt_Prob = 1 - float(Allele_Prob[Loc])
                     if Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0" and Outgroup3 == "0,0,0,0" and float(Prob) >= 0.525:
                         print(Loc + "\t" + Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Ancestral" + "\t" + "No_Outgroup" + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Derived")
                     elif Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0" and Outgroup3 == "0,0,0,0" and float(Prob) <= 0.475:
                         print(Loc + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Ancestral" + "\t" + "No_Outgroup" + "\t" + Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Derived")
                     elif float(Prob) >= 0.525:
                         print(Loc + "\t" + Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Ancestral" + "\t" + "Yes_Outgroup" + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Derived")
                     elif float(Prob) <= 0.475:
                         print(Loc + "\t" + Dic_Minor[Loc] + "\t" + str(Alt_Prob) + "\t" + "Ancestral" + "\t" + "Yes_Outgroup" + "\t" + Dic_Major[Loc] + "\t" + str(Prob) + "\t" + "Derived")
