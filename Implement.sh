#Extract Location co-ordinates of all Lines
#awk -F "\"*,\"*" '{print $1}' EST.198.Thaliana.sort.txt > AllLocations.txt

#Add these co-ordinates to the Species file
#paste AllLocations.txt EST.Input > EST.Loc.Input

#Split into 150 equally sized files due to segmentation faults in programme
#Sample used = Thaliana, Lyrata, Halleri, C_sativus
#split -l 71382 EST.Loc.Input ThLyHaSa

#Perform package on split files
files=`ls *ThLyHaSa*`

for file in $files
do

./est-sfs config-kimura.txt $file seedfile.txt $file.output.txt $file.pvalue.txt
done

#Create P-value folder
#mkdir P_value

#Move all output pvalue files to new folder
#mv *pvalue* ./P_value

#Remove non-informative lines
files=`ls *Th*`

for file in $files
do

tail -71383 $file > $file.tail

done

#Concatenate all of these files into 1 big file
#cat *tail* >  AllThLyHaSa.txt

#Add location co-ordinates
paste ../AllLocations.txt AllThLyHaSa.txt > AllLocThLyHaSa.txt


#Implement Python script
#This outputs all locations. Those without an analgous site in the Outgroup species returns a "NA" value
#Those locations with ancestral allele probabilites equal to or greater than 0.5 outputs a the reference
#allele nucleotide as well as the string "Ancestral". Those locations with ancestral allele probabilites
#less than 0.5 outputs a the alternative allele nucleotide as well as the string "Derived".
python Outgroup.py Updated1001.txt ThLyHaNa/AllLocThLyHaSa.txt ../EST.Loc.Input 3 > ThLyHaSa.Allele.Output

#Repeat for ThLyHall ThLyHaNa and ThLyHaPe to generate ThLyHall.Allele.Output ThLyHaNa.Allele.Output ThLyHaPe.Allele.Output
#python Outgroup.py Updated1001.txt ThLyHaSa/AllLocThLyHall.txt ../EST.Loc.Input 3 > ThLyHall.Allele.Output
#python Outgroup.py Updated1001.txt ThLyHaNa/AllLocThLyHaSa.txt ../EST.Loc.Input 3 > ThLyHaNa.Allele.Output
#python Outgroup.py Updated1001.txt ThLyHaNa/AllLocThLyHaSa.txt ../EST.Loc.Input 3 > ThLyHaSa.Allele.Output

#Alternatively, if one wud only like to use locations with at least 1 Outgroup:
#Hash out the lines in #Outgroup.py and re-hash the lines above


#Combines data from all files, identifying the whether the major allele at each site is ancestral
#or derived.
python Out_Estimate_State.py > Output.txt

#Extract the locations whereby all files agree
#grep "same" Output.txt | wc -l

#Extract the lines with at least 1 Outgroup
#grep -v "No_Outgroup" > Output.Outgroup.txt

#Extract the Derived entries
#grep "Derived" Output.txt > Output.Derived.txt
#grep "Derived" Output.Outgroup.txt > Output.Outgroup.Derived.txt


#Extract the Ancestral entries
#grep "Ancestral" Output.txt > Output.Ancestral.txt
#grep "Ancestral" Output.Outgroup.txt > Output.Outgroup.Ancestral.txt

###########################################################################################################
#Stats: Using All Locations: 10,707,430 in total
#                            10,707,430 of these had the same alleles across the 4 samples (Output.txt)
#               Of the same: 10,105,460 are Ancestral and      
#                            601,970 are Derived
#

#Stats: Using All Locations with at least 1 Outgroup: 7,682,710 in total
#                            7,682,710 of these had the same alleles across the 4 samples (Output.Outgroup.txt)
#               Of the same: 7,110,609 are Ancestral and (Output.Outgroup.Ancestral.txt) 
#                            572,101 are Derived (Output.Outgroup.Derived.txt)
###########################################################################################################


#Then Download the indiviual Strains from 1001 Arabidopsis Genome
#wget /data/GMI-MPI/releases/v3.1/intersection_snp_short_indel_vcf/

#Annotate the VCF files
samples=`ls *vcf.gz*`

for sample in $samples
do

/home/apeters/anaconda3/bin/tabix $sample
/home/apeters/anaconda3/bin/bcftools +fill-tags $sample -- -t AC,AF,AN > Updated.$sample

done

#Create new output directory
mkdir AllSameOutLocations

#Count number of derived and ancestral alleles in each inidiviudal file 

samples=`ls *Updated*`

for sample in $samples
do

python Specific_Allele_Count.py NewAllLocations.same.derived.txt NewAllLocations.same.ancestral.txt $sample > AllSameOutLocations/$sample

done

#Concatenate all the results
#cat *Updated* > AllSamplesAllSameLocations.txt

#Extract all sample names
#awk '{print $1}' AllSamplesAllSameLocations.txt | tr -d Updated.inrscio_vfgz > Samplenames.txt

#Extract all Ancestral Allele counts
#awk '{print $2}' AllSamplesAllSameLocations.txt > Anc.txt

#Extract all Derived Allele counts
#awk '{print $3}' AllSamplesAllSameLocations.txt > Der.txt

#Create csv file with strain id and ancestral counts
#paste Samplenames.txt Anc.txt | awk 'gsub("\t",",")' > AncestralCounts.txt

#Create csv file with strain id and derived counts
#paste Samplenames.txt Der.txt | awk 'gsub("\t",",")' > DerivedCounts.txt

#Then use the GWAS portal at https://gwas.gmi.oeaw.ac.at/ and follow the steps to use
#Derived Counts as a quantatitive pheonotype for a GWAS




