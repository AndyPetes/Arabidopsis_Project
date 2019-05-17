#Prior Steps on a Linux HPC:
#tabix -p vcf 1001genomes_snp-short-indel_only_ACGTN.vcf.gz
#bcftools +fill-tags 1001genomes_snp-short-indel_only_ACGTN.vcf.gz -- -t AC,AF,AN > Updated1001vcf
#awk '{print $1,$2,$4,$5,$8'} Updated1001.vcf > Updated1001.txt
#Download MAF alignments


#Usage: Generate Nucleotide Counts based of Common Ancestors based on Alignments for Ancestral Allle Inference  

#for sample in *maf; 
#do 
#       python MAF.Arabidopsis.py Updated1001.txt $sample "lyrata" > $sample.txt; 
#done


#This example compares the Thaliana to the Halleri Species
#sys.argv[1] = /data4/apeters/Thaliana/1001Updated.txt
#sys.argv[2] = MAF File
#sys.argv[3] = Species name in MAF file (i.e. "lyrata", "halleri", "tauschii")

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

#print(Dic)

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
             		fields = line.strip("\n").split(" ")
             		#Allocate Species
             		Species = fields[1]
             		#Allocate Sequence
			if "thaliana" in Species:
                          Sequence = fields[-1]
                          #Allocate Position
                          Position = fields[4]
                          #Some Positions are in the different field, mostly "fields[5]"
                          if Position == "":
                        	continue
                    	  #Calculate length of Alignment
                    	  Location_List = []
                    	  for i in range(len(Sequence)):
                        	#Get Specific Nucleotide along length of alignment
                        	Site = (int(Position) + i)
                                Location = chrom + str(Site) 
                                Location_List.append(Location)
                        	#Look if Range of positions along alignment is in the Dictionary
                        	if str(Location) in Dic:
                            	#Retrieve Reference SNP from 1001 Arabidopsis Database
                            		VCF_Base = Dic[str(Location)]
                            		#Retrieve SNP at MAF position
                            		Sequence_Base = Sequence[i]
					if Sequence_Base == "-":
						continue
					#If the Refernce Base is same as Alignment Proceed
                            		if VCF_Base == Sequence_Base.upper():
                                		#Get Complementary Base Pair in Lyrata
                                		Aligned_Lyrata_Base = Sequence_Dic[Sequence][i]
                                		#print(Aligned_Lyrata_Base)
                                		if Aligned_Lyrata_Base == "A" or Aligned_Lyrata_Base == "a":
                                    			print("%s,1,0,0,0"%(Location))
                                		if Aligned_Lyrata_Base == "C" or Aligned_Lyrata_Base == "c":
                                    			print("%s,0,1,0,0"%(Location))
                                		if Aligned_Lyrata_Base == "G" or Aligned_Lyrata_Base == "g":
                                    			print("%s,0,0,1,0"%(Location))
                                		if Aligned_Lyrata_Base == "T" or Aligned_Lyrata_Base == "t":
                                    			print("%s,0,0,0,1"%(Location))
                                		if Aligned_Lyrata_Base == "-":
                                    			print("%s,0,0,0,0"%(Location))
                    #if Dic.keys() not in Location_List:
                    #    print("%s,%s,0,0,0,0"%(Chromosome,Location))
                    	#Allocate NewPosition
                    	Position2 = fields[5]
                    	#Some Positions are in the different field, mostly "fields[5]"
                    	if Position2 == "":
                        	continue
                    	#Calculate length of Alignment
                    	Location_List = []
                    	for i in range(len(Sequence)):
                        	#Get Specific Nucleotide along length of alignment
                        	Location = (int(Position2) + i)
                        	Location_List.append(Location)
                        	#Look if Range of positions along alignment is in the Dictionary
                        	if str(Location) in Dic:
                            		#Retrieve Reference SNP from 1001 Arabidopsis Database
                            		VCF_Base = Dic[str(Location)]
                            		#Retrieve SNP at MAF position
                            		Sequence_Base = Sequence[i]
                                        if Sequence_Base == "-":
                                                continue
                                        #If the Refernce Base is same as Alignment Proceed
                                        if VCF_Base == Sequence_Base.upper():
						#Get Complementary Base Pair in Lyrata
                                		Aligned_Lyrata_Base = Sequence_Dic[Sequence][i]
                                		#print(Aligned_Lyrata_Base)
                                		if Aligned_Lyrata_Base == "A" or Aligned_Lyrata_Base == "a":
                                    			print("%s,1,0,0,0"%(Location))
                                		if Aligned_Lyrata_Base == "C" or Aligned_Lyrata_Base == "c":
                                    			print("%s,0,1,0,0"%(Location))
                                		if Aligned_Lyrata_Base == "G" or Aligned_Lyrata_Base == "g":
                                    			print("%s,0,0,1,0"%(Location))
                                		if Aligned_Lyrata_Base == "T" or Aligned_Lyrata_Base == "t":
                                    			print("%s,0,0,0,1"%(Location))
                                		if Aligned_Lyrata_Base == "-":
                                    			print("%s,0,0,0,0"%(Location))
