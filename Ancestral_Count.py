#Divide 2 inegers to give a float:
from __future__ import division

#Input Files:
#sys.argv[1] = ThLyHaNa.Allele.Derived.Output
#sys.argv[2] = ThLyHaNa.Allele.Ancestral.Output
#sys.argv[3] = Strain.vcf

import sys

Derived = {}
with open(sys.argv[1],"r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Nucleotide = fields[1]
                Derived[Location] = Nucleotide
Ancestral = {}
with open(sys.argv[2],"r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Nucleotide = fields[1]
                Ancestral[Location] = Nucleotide

Derived_Count = 0
Ancestral_Count = 0
with open(sys.argv[3],"r") as IN:
        for line in IN:
            if line.startswith("#"):
                continue
            fields = line.strip("\n").split("\t")
            Chromosome = fields[0]
            Position = fields[1]
            Co_ords = Chromosome + "_" + Position
            Reference = fields[3]
            Alternative = fields[4]
            New_Fields = fields[7].split(";")
            Alt_Freq = float(New_Fields[2][3:])
            #In this Case the Reference Allele is the most frequent Allele
            if Alt_Freq < 0.5:
                if Co_ords in Derived:
                    if Reference == Derived[Co_ords]:
                        Derived_Count = Derived_Count + 1
                if Co_ords in Ancestral:
                    if Reference == Ancestral[Co_ords]:
                        Ancestral_Count = Ancestral_Count + 1
            #In this case the Alternative Allele is the most frequent allele
            elif Alt_Freq >= 0.5:
                if Co_ords in Derived:
                    if Alternative == Derived[Co_ords]:
                        Derived_Count = Derived_Count + 1
                if Co_ords in Ancestral:
                    if Alternative == Ancestral[Co_ords]:
                        Ancestral_Count = Ancestral_Count + 1


Total_Count = Ancestral_Count + Derived_Count
Ancestral_Fraction = float(Ancestral_Count/Total_Count) 
Derived_Fraction = float(Derived_Count/Total_Count)
print(str(Ancestral_Count) + "\t" + str(Derived_Count) + "\t" + str(Total_Count) + "\t" + str(Ancestral_Fraction) + "\t" + str(Derived_Fraction))
