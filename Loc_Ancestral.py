#Description: This takes Arabidopsis VCF Data and outputs it in a readable
#format by the EST program. However, the maximum number of alleles the 
#program can handle is 200, and therefore when alleles exceed a n=198
#then the allele counts are counted as fractions of 198. n=198 was chosen
#because this is the largest number by which the total allele count does
#not exceed 200 after rounding

#Usage:  python Loc_Ancestral.py Updated1001.txt > EST_Input/EST.198.Thaliana.txt
###USE PYTHON 3 OR ABOVE

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
                if len(Reference) == 1 and len(Alternative) == 1:
                    new_fields = fields[4].split(";")
                    AC=int(new_fields[3][3:])
                    AN=int(new_fields[1][3:])
                    if int(AN) < 198:
                        Ref_Allele = int(AN) - int(AC)
                        if Reference == "A" and Alternative == "C":
                                print("%s_%s,%s,%s,0,0"%(Chromosome,Position,Ref_Allele,AC))
                        if Reference == "A" and Alternative == "G":
                                 print("%s_%s,%s,0,%s,0"%(Chromosome,Position,Ref_Allele,AC))
                        if Reference == "A" and Alternative == "T":
                                print("%s_%s,%s,0,0,%s"%(Chromosome,Position,Ref_Allele,AC))
                        if Reference == "C" and Alternative == "A":
                                print("%s_%s,%s,%s,0,0"%(Chromosome,Position,AC,Ref_Allele))
                        if Reference == "C" and Alternative == "G":
                                print("%s_%s,0,%s,%s,0"%(Chromosome,Position,Ref_Allele,AC))
                        if Reference == "C" and Alternative == "T":
                                print("%s_%s,0,%s,0,%s"%(Chromosome,Position,Ref_Allele,AC))
                        if Reference == "G" and Alternative == "A":
                                print("%s_%s,%s,0,%s,0"%(Chromosome,Position,AC,Ref_Allele))
                        if Reference == "G" and Alternative == "C":
                                print("%s_%s,0,%s,%s,0"%(Chromosome,Position,AC,Ref_Allele))
                        if Reference == "G" and Alternative == "T":
                                print("%s_%s,0,0,%s,%s"%(Chromosome,Position,Ref_Allele,AC))
                        if Reference == "T" and Alternative == "A":
                                print("%s_%s,%s,0,0,%s"%(Chromosome,Position,AC,Ref_Allele))
                        if Reference == "T" and Alternative == "C":
                                print("%s_%s,0,%s,0,%s"%(Chromosome,Position,AC,Ref_Allele))
                        if Reference == "T" and Alternative == "G":
                                print("%s_%s,0,0,%s,%s"%(Chromosome,Position,AC,Ref_Allele))
                    else:
                        New_Allele = int(AN) - int(AC)
                        Ref_Allele = round((int(New_Allele)/int(AN))*198)
                        New_AC = round((int(AC)/int(AN))*198)
                        if Reference == "A" and Alternative == "C":
                                print("%s_%s,%d,%d,0,0"%(Chromosome,Position,Ref_Allele,New_AC))
                        if Reference == "A" and Alternative == "G":
                                print("%s_%s,%d,0,%d,0"%(Chromosome,Position,Ref_Allele,New_AC))
                        if Reference == "A" and Alternative == "T":
                                print("%s_%s,%d,0,0,%d"%(Chromosome,Position,Ref_Allele,New_AC))
                        if Reference == "C" and Alternative == "A":
                                print("%s_%s,%d,%d,0,0"%(Chromosome,Position,New_AC,Ref_Allele))
                        if Reference == "C" and Alternative == "G":
                                print("%s_%s,0,%d,%d,0"%(Chromosome,Position,Ref_Allele,New_AC))
                        if Reference == "C" and Alternative == "T":
                                print("%s_%s,0,%d,0,%d"%(Chromosome,Position,Ref_Allele,New_AC))
                        if Reference == "G" and Alternative == "A":
                                print("%s_%s,%d,0,%d,0"%(Chromosome,Position,New_AC,Ref_Allele))
                        if Reference == "G" and Alternative == "C":
                                print("%s_%s,0,%d,%d,0"%(Chromosome,Position,New_AC,Ref_Allele))
                        if Reference == "G" and Alternative == "T":
                                print("%s_%s,0,0,%d,%d"%(Chromosome,Position,Ref_Allele,New_AC))
                        if Reference == "T" and Alternative == "A":
                                print("%s_%s,%d,0,0,%d"%(Chromosome,Position,New_AC,Ref_Allele))
                        if Reference == "T" and Alternative == "C":
                                print("%s_%s,0,%d,0,%d"%(Chromosome,Position,New_AC,Ref_Allele))
                        if Reference == "T" and Alternative == "G":
                                print("%s_%s,0,0,%d,%d"%(Chromosome,Position,New_AC,Ref_Allele))
                    
