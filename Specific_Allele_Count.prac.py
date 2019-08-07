#Divide 2 inegers to give a float:
from __future__ import division

#Input Files:
#sys.argv[1] = Strain.vcf

import sys

Derived = {}
Ancestral = {}


with open("AllSnps.1_9.Derived.Outgroup.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[1]
                Major_Allele = fields[3][0]
                Derived[Location] = Major_Allele

                
with open("AllSnps.1_9.Ancestral.Outgroup.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[1]
                Major_Allele = fields[3][0]
                Ancestral[Location] = Major_Allele

Individual_Strain = {}

with open(sys.argv[1],"r") as IN:
        for line in IN:
            if line.startswith("#"):
                continue
            fields = line.strip("\n").split("\t")
            Chromosome = fields[0]
            Position = fields[1]
            Co_ords = Chromosome + "_" + Position
            Reference = fields[3]
            Alternative = fields[4]
            if len(Reference) == 1 and len(Alternative) == 1:
                New_Fields = fields[7].split(";")
                Alt_Freq = float(New_Fields[2][3:])
                Genotype = fields[9][:3]
                if Genotype == "1|1" or Genotype == "1/1":
                    Individual_Strain[Co_ords] = Alternative + Alternative
                if Genotype == "0|1" or Genotype == "0/1":
                    Individual_Strain[Co_ords] = Reference + Alternative
                if Genotype == "1|0" or Genotype == "1/0":
                    Individual_Strain[Co_ords] = Alternative + Reference
                if Genotype == "0|0" or Genotype == "0/0":
                    Individual_Strain[Co_ords] = Reference + Reference


Derived_Count = 0
Ancestral_Count = 0

with open(sys.argv[1],"r") as IN:
        for line in IN:
            if line.startswith("#"):
                continue
            fields = line.strip("\n").split("\t")
            Chromosome = fields[0]
            Position = fields[1]
            Co_ords = Chromosome + "_" + Position
            Reference = fields[3]
            Alternative = fields[4]
            if len(Reference) == 1 and len(Alternative) == 1:
                New_Fields = fields[7].split(";")
                Alt_Freq = float(New_Fields[2][3:])
                Genotype = fields[9][:3]
                if Genotype == "./.":
                    continue
                Allele1 = Individual_Strain[Co_ords][0]
                Allele2 = Individual_Strain[Co_ords][1]
                if Allele1 == Reference:
                    if Co_ords in Derived:
                        if Derived[Co_ords] == Reference:
                            Derived_Count = Derived_Count + 1
                    if Co_ords in Ancestral:    
                        if Ancestral[Co_ords] == Reference:
                            Ancestral_Count = Ancestral_Count + 1
                if Allele1 == Alternative:
                    if Co_ords in Derived:
                        if Derived[Co_ords] == Alternative:
                            Derived_Count = Derived_Count + 1
                    if Co_ords in Ancestral:    
                        if Ancestral[Co_ords] == Alternative:
                            Ancestral_Count = Ancestral_Count + 1
                if Allele2 == Reference:
                    if Co_ords in Derived:
                        if Derived[Co_ords] == Reference:
                            Derived_Count = Derived_Count + 1
                    if Co_ords in Ancestral:    
                        if Ancestral[Co_ords] == Reference:
                            Ancestral_Count = Ancestral_Count + 1
                if Allele2 == Alternative:
                    if Co_ords in Derived:
                        if Derived[Co_ords] == Alternative:
                            Derived_Count = Derived_Count + 1
                    if Co_ords in Ancestral:    
                        if Ancestral[Co_ords] == Alternative:
                            Ancestral_Count = Ancestral_Count + 1


Total_Count = Ancestral_Count + Derived_Count
Ancestral_Fraction = float(Ancestral_Count/Total_Count) 
Derived_Fraction = float(Derived_Count/Total_Count)
print(str(sys.argv[1]) + "\t" + str(Ancestral_Count) + "\t" + str(Derived_Count) + "\t" + str(Total_Count) + "\t" + str(Ancestral_Fraction) + "\t" + str(Derived_Fraction))
