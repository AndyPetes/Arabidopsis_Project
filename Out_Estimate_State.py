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
ThLyHallOut = {}
ThLyHaSaOut = {}
ThLyHaNaOut = {}
ThLyHaPeOut = {}

with open("ThLyHall.Allele.Prob.Output","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Major_Allele = fields[1]
                State = fields[3]
                ThLyHall[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
                      ThLyHallOut[Location] = "No_Outgroup"
                else:
                      ThLyHallOut[Location] = "Outgroup"                

with open("ThLyHaSa.Allele.Prob.Output","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                Major_Allele = fields[1]
                State = fields[3]
                ThLyHaSa[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
       	       	      ThLyHaSaOut[Location] = "No_Outgroup"             
       	       	else:
       	       	      ThLyHaSaOut[Location] = "Outgroup"
                

with open("ThLyHaNa.Allele.Prob.Output","r") as IN:
       	for line in IN:
               	fields = line.strip("\n").split("\t")
               	Location = fields[0]
               	Major_Allele = fields[1]
               	State = fields[3]
               	ThLyHaNa[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
       	       	      ThLyHaNaOut[Location] = "No_Outgroup"             
       	       	else:
       	       	      ThLyHaNaOut[Location] = "Outgroup"
                


with open("ThLyHaPe.Allele.Prob.Output","r") as IN:
       	for line in IN:
               	fields = line.strip("\n").split("\t")
               	Location = fields[0]
               	Major_Allele = fields[1]
               	State = fields[3]
               	ThLyHaPe[Location] = Major_Allele + ":" + State
                if fields[4] == "No_Outgroup":
       	       	      ThLyHaPeOut[Location] = "No_Outgroup"             
       	       	else:
       	       	      ThLyHaPeOut[Location] = "Outgroup"



with open("locations.txt","r") as IN:
        for line in IN:
                fields = line.strip("\n").split("\t")
                Location = fields[0]
                if Location in ThLyHall and Location in ThLyHaSa and Location in ThLyHaNa and Location in ThLyHaPe:
                    if ThLyHall[Location] == ThLyHaSa[Location] and ThLyHall[Location] == ThLyHaNa[Location] and ThLyHall[Location] == ThLyHaPe[Location]:           
                        if ThLyHallOut[Location] == "No_Outgroup" and ThLyHaSaOut[Location] == "No_Outgroup" and ThLyHaNaOut[Location] == "No_Outgroup" and ThLyHaPeOut[Location] == "No_Outgroup":    
                               print("No_Outgroup" + "\t" + Location + "\t" + "same" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])
                               #print("No_Outgroup" + "\t" + Location + "\t" + "NA" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])
                        else:
                               print("Outgroup" + "\t" + Location + "\t" + "same" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])                      
                    else:
                        if ThLyHallOut[Location] == "No_Outgroup" and ThLyHaSaOut[Location] == "No_Outgroup" and ThLyHaNaOut[Location] == "No_Outgroup" and ThLyHaPeOut[Location] == "No_Outgroup":
                               print("No_Outgroup" + "\t" + Location + "\t" + "different" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])
                               #print("No_Outgroup" + "\t" + Location + "\t" + "NA" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])
                        else:
                               print("Outgroup" + "\t" + Location + "\t" + "different" + "\t" + ThLyHall[Location] + "\t" + ThLyHaSa[Location] + "\t" + ThLyHaNa[Location] + "\t" + ThLyHaPe[Location])
                               

