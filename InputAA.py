#Usage:  python Outgroup.py Updated1001.txt AllThLyHaPe.txt EST.Loc.Thal.Lyr.Hall.Per.txt 3 > AlleleInference.output
#Exact Usage: python Outgroup2.py ../../Thaliana/Updated1001.txt ../Pvalue/ThLyHaPe/AllLocThLyHaPe.txt ../EST.Loc.Thal.Lyr.Hall.Per.txt 
# 3 > ThLyHaPe.Allele.Output
#Input Files:
#sys.argv[1] = Updated1001.txt
#sys.argv[2] = AllLocThLyHaPe.txt
#sys.argv[3] = EST.Loc.Thal.Lyr.Hall.Per.txt
#sys.argv[4] = Number of Outgroups (i.e. 2 or 3)
import sys

Ancestral = {}
Derived = {}

with open("/data4/apeters/Arabidopsis/EST_Output/Python_Script/AllSnps.01_99.Ancestral.Outgroup.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[1]
                Nucleotide = fields[3][0]
                State = str(fields[3][2:])
                Ancestral[Location] = Nucleotide  


with open(sys.argv[1],"r") as IN:
        for line in IN:
            if line.startswith("#"):
                continue
            fields = line.strip("\n").split("\t")
            Chromosome = fields[0]
            Position = fields[1]
            Location = Chromosome + "_" + Position
            Reference = fields[3]
            Alternative = fields[4]
            if len(Reference) == 1 and len(Alternative) == 1: 
                 New_Fields = fields[7].split(";")
                 Alt_Freq = float(New_Fields[2][3:])
                 #In this Case the Reference Allele is the most frequent Allele
                 if Alt_Freq < 0.5:
                      if Location in Ancestral:
                           if Reference == Ancestral[Location]:
                                print(str(Location) + "\t" + str(fields[7]) + ";AA=%s|||"%(Reference))
                      else:
                           print(str(Location) + "\t" + str(fields[7]) + ";AA=|||Unknown")

                 #In this Case the Alternate Allele is the most frequent Allele
                 if Alt_Freq >= 0.5: 
                      if Location in Ancestral:
                           if Alternative == Ancestral[Location]:
                                print(str(Location) + "\t" + str(fields[7]) + ";AA=%s|||"%(Alternative))
                      else:
                           print(str(Location) + "\t" + str(fields[7]) + ";AA=|||Unknown")

