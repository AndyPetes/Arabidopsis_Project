#Extract Location co-ordinates of all Lines
#awk -F "\"*,\"*" '{print $1}' EST.198.Thaliana.sort.txt > AllLocations.txt

#Add these co-ordinates to the Species file
#paste AllLocations.txt EST.Input > EST.Loc.Input

#Split into 150 equally sized files due to segmentation faults in programme
#Sample used = Thaliana, Lyrata, Halleri, C_sativus
#split -l 71382.7 EST.Loc.Input ThLyHaSa

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
python Out_Estimate_State.py > NewAllLocations.txt

#Extract the locations whereby all files agree
#grep "same" NewAllLocations.txt > NewAllLocations.same.txt

#Extract the Derived entries
#grep "Derived" NewAllLocations.same.txt > NewAllLocations.same.derived.txt

#Extract the Ancestral entries
#grep "Ancestral" NewAllLocations.same.txt > NewAllLocations.same.ancestral.txt

###########################################################################################################
#Stats: Using All Locations: 10,707,413 in total
#                            10,707,317 of these had the same alleles across the 4 samples (NewAllLocations.same.txt)
#                            96 had different alleles across the samples
#               Of the same: 10,579,290 are Ancestral and (NewAllLocations.same.ancestral.txt)     
#                            128,027 are Derived (NewAllLocations.same.derived.txt)
#

#Stats: Using All Locations with at least 1 Outgroup: 2,200,002 in total
#                            2,200,001 of these had the same alleles across the 4 samples (NewAllLocations.same.txt)
#                            1 had different alleles across the samples
#               Of the same: 2,122,202 are Ancestral and (NewAllLocations.same.ancestral.txt) 
#                            128,027 are Derived (NewAllLocations.same.derived.txt)
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
#paste Samplenames.txt Anc.txt | awk 'gsub("\t","s")' > AncestralCounts.txt

#Create csv file with strain id and derived counts
#paste Samplenames.txt Der.txt | awk 'gsub("\t","s")' > DerivedCounts.txt

#Then use the GWAS portal at https://gwas.gmi.oeaw.ac.at/ and follow the steps to use
#Derived Counts as a quantatitive pheonotype for a GWAS




