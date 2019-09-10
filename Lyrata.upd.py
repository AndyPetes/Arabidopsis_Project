import sys
input_data = sys.argv

with open(sys.argv[1],"r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Thaliana_Data = fields[1]
                Lyrata_Data = fields[2]
                Halleri_Data = fields[3]
                Nucleotides = Thaliana_Data.split(",")
                A = int(Nucleotides[0])
                C = int(Nucleotides[1])
                G = int(Nucleotides[2])
                T = int(Nucleotides[3])
                #Unhash Following Line for Method 2
                ##if Lyrata_Data == Halleri_Data:
                    if Lyrata_Data == "1,0,0,0" and A >= 1:
                        if C >= 1:
                            print(Location + "\t" + "A" + "\t" + "C" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif G >= 1:
                            print(Location + "\t" + "A" + "\t" + "G" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif T >= 1:
                            print(Location + "\t" + "A" + "\t" + "T" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
       	       	       	else:
       	       	       	    print(Location + "\t" + "A" + "\t" + "N" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_2nd_SNP")
                    elif Lyrata_Data == "1,0,0,0" and A == 0:
                        print(Location + "\t" + "A" + "\t"  + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_Allele_Thaliana")
                    elif Lyrata_Data == "0,1,0,0" and C >= 1:
                        if A >= 1:
                            print(Location + "\t" + "C" + "\t" + "A" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif G >= 1:
                            print(Location + "\t" + "C" + "\t" + "G" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif T >= 1:
                            print(Location + "\t" + "C" + "\t" + "T" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        else:
       	       	       	    print(Location + "\t" + "C" + "\t" + "N" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_2nd_SNP")
                    elif Lyrata_Data == "0,1,0,0" and C == 0:
                        print(Location + "\t" + "C" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_Allele_Thaliana")
                    elif Lyrata_Data == "0,0,1,0" and G >= 1:
                        if A >= 1:
                            print(Location + "\t" + "G" + "\t" + "A" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif C >= 1:
                            print(Location + "\t" + "G" + "\t" + "C" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif T >= 1:
                            print(Location + "\t" + "G" + "\t" + "T" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        else:
       	       	       	    print(Location + "\t" + "G" + "\t" + "N" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_2nd_SNP")
                    elif Lyrata_Data == "0,0,1,0" and G == 0:
                        print(Location + "\t" + "G" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_Allele_Thaliana")
                    elif Lyrata_Data == "0,0,0,1" and T >= 1:
                        if A >= 1:
                            print(Location + "\t" + "T" + "\t" + "A" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif C >= 1:
                            print(Location + "\t" + "T" + "\t" + "C" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        elif G >= 1:
                            print(Location + "\t" + "T" + "\t" + "G" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Yes_Outgroup")
                        else:
                            print(Location + "\t" + "T" + "\t" + "N" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_2nd_SNP")
                    elif Lyrata_Data == "0,0,0,1" and T == 0:
                        print(Location + "\t" + "T" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_Allele_Thaliana")
                    elif Lyrata_Data == "0,0,0,0":
                        print(Location + "\t" + "N" + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "Outgroup_No_Align")
                    else:
                        print(Location + "\t" + Thaliana_Data + "\t" + Lyrata_Data + "\t" + Halleri_Data + "\t" + "No_Thaliana")
