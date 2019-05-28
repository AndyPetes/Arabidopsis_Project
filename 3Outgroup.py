#Usage:  python 3Outgroup.py Updated1001.txt AllThLyHaPe.txt EST.Loc.Thal.Lyr.Hall.Per.txt 3 > AlleleInference.output
#Inpur Files:
#sys.argv[1] = Updated1001.txt
#sys.argv[2] = AllThLyHaPe.txt
#sys.argv[3] = AllThLyHaPe.txt EST.Loc.Thal.Lyr.Hall.Per.txt
#sys.argv[4] = Number of Outgroups (i.e. 3 or 2)


#import sys
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
                    
#Create dictopnary of the allele probailities
Allele_Prob = {}
with open(sys.argv[2],"r") as IN:
        for line in IN:
                fields = line.strip("\n").split(" ")
                Location = fields[0]
                Probability = fields[8]
                Allele_Prob[Location] = Probability

#Create output of Ancestral Alleles
with open(sys.argv[3],"r") as IN:
        for line in IN:
                #Outgroups = 3
                if sys.argv[4] == "3"
                        fields = line.strip("\n").split(" ")
                        Outgroup1 = fields[-3]
                        Outgroup2 = fields[-2]
                        Outgroup3 = fields[-1]
                        Loc = fields[0]
                        if Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0" and Outgroup3 == "0,0,0,0":
                                print(Loc + "\t" + "NA")
                        Probability = Allele_Prob[Loc]
                        if float(Probability) >= 0.5:
                                print(Loc + "\t" + Dic_Ref[Loc])
                        else:
                                print(Loc + "\t" + Dic_Alt[Loc])
                #Outgroups = 4 
                if sys.argv[4] == "2"
                        fields = line.strip("\n").split(" ")
                        Outgroup1 = fields[-2]
                        Outgroup2 = fields[-1]
                        Loc = fields[0]
                        if Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0":
                                print(Loc + "\t" + "NA")
                        Probability = Allele_Prob[Loc]
                        if float(Probability) >= 0.5:
                                print(Loc + "\t" + Dic_Ref[Loc])
                        else:
                                print(Loc + "\t" + Dic_Alt[Loc])
