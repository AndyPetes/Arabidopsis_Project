#Generates an output compatible with EST-SFS
#sys.argv[1] = /data4/apeters/Thaliana/1001Updated.txt
#sys.argv[2] = MAF File
#sys.argv[3] = Species name (i.e. Lyrata)

import sys

Dic = {}

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
                    Dic[Chromosome + "_" + Position] = Reference


#Create Dictionary for Thaliana:Lyrata Sequences                
Thaliana_Sequence = []
Lyrata_Sequence = []

with open(sys.argv[2],"r") as IN:
        for line in IN:
                if line.startswith("s"):
                    fields = line.strip("\n").split(" ")
                    Species = fields[1]
                    Sequence = fields[-1]
                    if sys.argv[3] in Species:
                        Lyrata_Sequence.append(Sequence)
                    if "thaliana" in Species:
                        Thaliana_Sequence.append(Sequence)

Sequence_Dic = {Thaliana_Sequence[i]: Lyrata_Sequence[i] for i in range(len(Thaliana_Sequence))}  

chromosome_number = ["1_","2_","3_","4_","5_"]


with open(sys.argv[2],"r") as IN:
        for chrom in chromosome_number:
            if chrom in IN.name:
                for line in IN:
                #'s' denotes the sequence alignments
                  if line.startswith("s"):
                    #Split into different fields
                    fields = line.strip("\n").split()
                    #Allocate Species
                    Species = fields[1]
                    #Allocate Sequence
                    if "thaliana" in Species:
                        Sequence = fields[-1]
                        #Allocate Position
                        Position = fields[2]
                        #Create empty sequence string
                        seq=''
                        #Loop through each nucleotide of the sequence
                        for nucleotide in Sequence:
                            #Keep appending Nucleotide to the "seq"
                            seq += nucleotide
                            #Create a variable for lengrth of "seq"
                            Seq_Len = len(seq) - 1
                            #Count number of gaps with each iteration as they gradually appear in "seq"
                            Gap = seq.count("-")
                            #Generate location of nucleotide if no gaps were present
                            NoGap = Seq_Len - int(Gap)
                            #Get genomi co-ordinate of nucleotide without gaps present
                            New_Location = int(Position) + int(NoGap)
                            #This is the last nucleotide in the incresing "seq" string as it loops through
                            NoGapNuc = seq[-1].upper()
                            #Skip Nucleotide if they contain gaps
                            if NoGapNuc == "-":
                                continue
                            #Add chromosome location to genomic position to look up in earlier created dictionary
                            Site = str(chrom) + str(New_Location)
                            #Proceed if the genomic location is in the initial dictionary
                            if str(Site) in Dic:
                                    #Retrieve Reference SNP from 1001 Arabidopsis Database
                                    VCF_Base = Dic[str(Site)]
                                    #If the Reference Base is same as Alignment Proceed
                                    if VCF_Base == NoGapNuc:
                                        #Get Complementary Base Pair in Lyrata
                                        Aligned_Lyrata_Base = Sequence_Dic[Sequence][len(seq) - 1].upper()
                                        if Aligned_Lyrata_Base == "A":
                                            print(str(Site) + "\t" + "1,0,0,0")
                                        if Aligned_Lyrata_Base == "C":
                                            print(str(Site) + "\t" + "0,1,0,0")
                                        if Aligned_Lyrata_Base == "G":
                                            print(str(Site) + "\t" + "0,0,1,0")
                                        if Aligned_Lyrata_Base == "T":
                                            print(str(Site) + "\t" + "0,0,0,1")
                                        if Aligned_Lyrata_Base == "-":
                                            print(str(Site) + "\t" + "0,0,0,0")