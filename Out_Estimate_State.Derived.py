#Exact Usage: python Out_Estimate_State.py > NewAllLocations.txt
#Description: Combines data from all files, identifying the whether the major allele at each site is ancestral
#or derived.

#Input Files:
#sys.argv[1] = ThLyHall.Allele.Prob.Output
#sys.argv[2] = ThLyHaSa.Allele.Prob.Output
#sys.argv[3] = ThLyHaNa.Allele.Prob.Output
#sys.argv[4] = ThLyHaPe.Allele.Prob.Output
import sys

ThLyHall = {}
ThLyHaSa = {}
ThLyHaNa = {}
ThLyHaPe = {}
ThLyHaTa = {}
ThLyHallOut = {}
ThLyHaSaOut = {}
ThLyHaNaOut = {}
ThLyHaPeOut = {}
ThLyHaTaOut = {}

with open("ThLyHall.AllSnps.1_9.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Major_Allele = fields[5]
                State = fields[7]
                ThLyHall[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
                      ThLyHallOut[Location] = "No_Outgroup"
                else:
                      ThLyHallOut[Location] = "Outgroup"                

with open("ThLyHaSa.AllSnps.1_9.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Major_Allele = fields[5]
                State = fields[7]
                ThLyHaSa[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
       	       	      ThLyHaSaOut[Location] = "No_Outgroup"             
       	       	else:
       	       	      ThLyHaSaOut[Location] = "Outgroup"
                

with open("ThLyHaNa.AllSnps.1_9.txt","r") as IN:
       	for line in IN:
               	fields = line.strip("\n").split("\t")
               	Location = fields[0]
               	Major_Allele = fields[5]
               	State = fields[7]
               	ThLyHaNa[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
       	       	      ThLyHaNaOut[Location] = "No_Outgroup"             
       	       	else:
       	       	      ThLyHaNaOut[Location] = "Outgroup"
                


with open("ThLyHaPe.AllSnps.1_9.txt","r") as IN:
       	for line in IN:
               	fields = line.strip("\n").split("\t")
               	Location = fields[0]
               	Major_Allele = fields[5]
               	State = fields[7]
               	ThLyHaPe[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
       	       	      ThLyHaPeOut[Location] = "No_Outgroup"             
       	       	else:
       	       	      ThLyHaPeOut[Location] = "Outgroup"

with open("ThLyHaTa.AllSnps.1_9.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Major_Allele = fields[5]
                State = fields[7]
                ThLyHaTa[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
                      ThLyHaTaOut[Location] = "No_Outgroup"
                else:
                      ThLyHaTaOut[Location] = "Outgroup"



with open("AllLocations.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                if Location in ThLyHall and Location in ThLyHaSa and Location in ThLyHaNa and Location in ThLyHaPe and Location in ThLyHaTa:
                    if ThLyHall[Location] == ThLyHaSa[Location] and ThLyHall[Location] == ThLyHaNa[Location] and ThLyHall[Location] == ThLyHaPe[Location] and ThLyHall[Location] == ThLyHaTa[Location]:           
                        if ThLyHallOut[Location] == "No_Outgroup" and ThLyHaSaOut[Location] == "No_Outgroup" and ThLyHaNaOut[Location] == "No_Outgroup" and ThLyHaPeOut[Location] == "No_Outgroup" and ThLyHaTaOut[Location] == "No_Outgroup":    
                               print("No_Outgroup" + "\t" + Location + "\t" + "same" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location] + "\t" + ThLyHaTa[Location])
                               #print("No_Outgroup" + "\t" + Location + "\t" + "NA" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])
                        else:
                               print("Outgroup" + "\t" + Location + "\t" + "same" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location] + "\t" + ThLyHaTa[Location])
                    else:
                        if ThLyHallOut[Location] == "No_Outgroup" and ThLyHaSaOut[Location] == "No_Outgroup" and ThLyHaNaOut[Location] == "No_Outgroup" and ThLyHaPeOut[Location] == "No_Outgroup" and ThLyHaTaOut[Location] == "No_Outgroup":
                               print("No_Outgroup" + "\t" + Location + "\t" + "different" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location] + "\t" + ThLyHaTa[Location])
                               #print("No_Outgroup" + "\t" + Location + "\t" + "NA" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])
                        else:
                               print("Outgroup" + "\t" + Location + "\t" + "different" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location] + "\t" + ThLyHaTa[Location])
