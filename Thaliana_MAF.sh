#!/bin/bash


# Your job name
#$ -N Thaliana_MAF

# The job should be placed into the queue 'all.q'
#$ -q all.q

# Running in the current directory
#$ -cwd

# Export some necessary environment variables
#$ -v PATH
#$ -v LD_LIBRARY_PATH
#$ -v PYTHONPATH
#$ -S /bin/bash

#First Download VCF Data from 1001 Arabidopsis Genomes website
wget https://1001genomes.org/data/GMI-MPI/releases/v3.1/1001genomes_snp-short-indel_only_ACGTN.vcf.gz

#Generate Index File
tabix -p vcf 1001genomes_snp-short-indel_only_ACGTN.vcf.gz

#Fill in AC (Allele Count), AF (Allele Frequency) and AN (Total number of alleles) fields
bcftools +fill-tags 1001genomes_snp-short-indel_only_ACGTN.vcf.gz -- -t AC,AF,AN > Updated1001vcf

#Print required information for downstream analysis to a different file so that it is a lighter file
awk '{print $1,$2,$4,$5,$8'} Updated1001.vcf > Updated1001.txt

