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





