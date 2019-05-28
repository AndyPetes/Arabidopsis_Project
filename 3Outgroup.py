#import sys
Dic_Ref = {}
Dic_Alt = {}


#Create Dictionary from 1001.vcf file
with open("/home/andrewp94/Downloads/Head1001.txt","r") as IN:
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
with open("/home/andrewp94/Downloads/practice.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split(" ")
                Location = fields[0]
                Probability = fields[8]
                Allele_Prob[Location] = Probability

#Create output of Ancestral Alleles
with open("/home/andrewp94/Downloads/EST.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split(" ")
                Outgroup1 = fields[-3]
                Outgroup2 = fields[-2]
                Outgroup3 = fields[-1]
                if Outgroup1 == "0,0,0,0" and Outgroup2 == "0,0,0,0" and Outgroup3 == "0,0,0,0":
                    continue
                Loc = fields[0]
                Probability = Allele_Prob[Loc]
                if float(Probability) >= 0.5:
                        print(Loc + "\t" + Dic_Ref[Loc])
                else:
                        print(Loc + "\t" + Dic_Alt[Loc])
