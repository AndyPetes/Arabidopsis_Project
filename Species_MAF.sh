#!/bin/bash


# Your job name
#$ -N MAF

# The job should be placed into the queue 'all.q'
#$ -q all.q

# Running in the current directory
#$ -cwd

# Export some necessary environment variables
#$ -v PATH
#$ -v LD_LIBRARY_PATH
#$ -v PYTHONPATH
#$ -S /bin/bash

#Download Multiple Alignment Format (MAF), e.g. Lyrata
#wget ftp://ftp.ensemblgenomes.org/pub/plants/release-43/maf/atha_tair10.v.alyr_v.1.0.lastz_net.tar.gz

#Unzip the file
#tar -xvzf atha_tair10.v.alyr_v.1.0.lastz_net.tar.gz

#Enter this directory
#cd atha_tair10.v.alyr_v.1.0.lastz_net

#Make Directory for new Input
#mkdir EST_Input

#Loop through all of the MAF Files
for sample in *maf; 

do 
       #Perform python script on all MAF files and output them to a new directory labelled "EST_Input"
       python MAF.Arabidopsis.py <path_to>/Updated1001.txt $sample "lyrata" > EST_Input/$sample.txt; 
done

#Enter created directory
#cd EST_Input

#Enter sample species name here to label downstream files
species='Lyrata'

#Concatentae all out files from the python script
cat *txt* > EST.All.$species.txt
#Sort the output based on genomic co-ordinate in Arabidopsis
sort -k 1 EST.All.$species.txt > EST.All.$species.sort.txt
#Create an output at all co-ordinates in the thaliana data
python /data4/apeters/Arabidopsis/Thaliana/EST_Input/Transform.EST.py EST.All.$species.sort.txt /data4/apeters/Arabidopsis/Thaliana/EST_Input/EST.198.Thaliana.sort.txt > EST.Final.$species.txt
#Reomove the location co-ordinates for EST package Input
cut -d, -f1 --complement EST.Final.$species.txt > EST.Final.$species.NoLoc.txt


echo All done
