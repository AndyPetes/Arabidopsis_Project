#Usage:python FinalAA.py FinalAA.output Updated1001.vcf > Updated1001.AA.vcf

#Input Files:
#sys.argv[1] = FinalAA.output
#sys.argv[2] = Updated1001.vcf

import sys

Dict = {}

with open(sys.argv[1],"r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Info = fields[1]
                Dict[Location] = Info

with open(sys.argv[2],"r") as IN:
        for line in IN:
            if line.startswith("#"):
                continue
            fields = line.strip("\n").split("\t")
            Chromosome = fields[0]
            Position = fields[1]
            Location = Chromosome + "_" + Position
            Reference = fields[3]
            Alternative = fields[4]
            Info = fields[7]
            if len(Reference) == 1 and len(Alternative) == 1:
                New_Fields = fields[7].split(";")
                Alt_Freq = float(New_Fields[2][3:])
                if Location in Dict:
                    First_Slice = int(line.index("DP"))
                    Second_Slice = int(line.index("GT"))
                    print(line[:First_Slice] + Dict[Location] + "\t" + line[Second_Slice:])
                    
                else:
                    First_Slice = int(line.index("DP"))
                    Second_Slice = int(line.index("GT"))
                    print(line[:First_Slice] + Info + ";AA=|||unknown\t" + line[Second_Slice:])
