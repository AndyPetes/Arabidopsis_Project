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

#Enter sample species name here
species_name='Lyrata'

for species in $species_name
do

cat *txt* > EST.All.$species.txt
sort -k 1 EST.All.$species.txt > EST.All.$species.sort.txt
python /data4/apeters/Arabidopsis/Thaliana/EST_Input/Transform.EST.py EST.All.$species.sort.txt /data4/apeters/Arabidopsis/Thaliana/EST_Input/EST.198.Thaliana.sort.txt > EST.Final.$species.txt
cut -d, -f1 --complement EST.Final.$species.txt > EST.Final.$species.NoLoc.txt

done

echo All done
