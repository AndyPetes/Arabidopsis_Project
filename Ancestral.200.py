#Info: This file generates data in the required format compatible with 
#the EST package for Ancestral Allele inference from the model species
#Arabidopsis thaliana

#However this script allows for only a total of 200 alleles be included
#which is only what the EST package can handle

#Usage: python Ancestral.200.py Updated1001.txt > EST.Lyrata.txt

import sys

with open(sys.argv[1],"r") as IN:
        for line in IN:
                if line.startswith("#"):
                        continue
                fields = line.strip("\n").split(" ")
                Chromosome = fields[0]
                Position = str(fields[1])
                Reference = fields[2]
                Alternative = fields[3]
                new_fields = fields[4].split(";")
                AC=new_fields[3][3:]
                AN=new_fields[1][3:]
                if len(Reference) == 1 and len(Alternative) == 1:
                    Ref_Allele = int(AN) - int(AC)
                    if int(AN) < 200:
                        if Reference == "A" and Alternative == "C":
                                 print("%s,%s,0,0"%(Ref_Allele,AC))
                        if Reference == "A" and Alternative == "G":
                                 print("%s,0,%s,0"%(Ref_Allele,AC))
                        if Reference == "A" and Alternative == "T":
                                 print("%s,0,0,%s"%(Ref_Allele,AC))
                        if Reference == "C" and Alternative == "A":
                                 print("%s,%s,0,0"%(AC,Ref_Allele))
                        if Reference == "C" and Alternative == "G":
                                 print("0,%s,%s,0"%(Ref_Allele,AC))
                        if Reference == "C" and Alternative == "T":
                                 print("0,%s,0,%s"%(Ref_Allele,AC))
                        if Reference == "G" and Alternative == "A":
                                 print("%s,0,%s,0"%(AC,Ref_Allele))
                        if Reference == "G" and Alternative == "C":
                                 print("0,%s,%s,0"%(AC,Ref_Allele))
                        if Reference == "G" and Alternative == "T":
                                 print("0,0,%s,%s"%(Ref_Allele,AC))
                        if Reference == "T" and Alternative == "A":
                                 print("%s,0,0,%s"%(AC,Ref_Allele))
                        if Reference == "T" and Alternative == "C":
                                 print("0,%s,0,%s"%(AC,Ref_Allele))
                        if Reference == "T" and Alternative == "G":
                                 print("0,0,%s,%s"%(AC,Ref_Allele))
