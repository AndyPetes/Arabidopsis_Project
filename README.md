## Arabidopsis_Project - Infer Arabidopsis Ancestral Alleles


This directory contains python scripts and bash scripts that demonstrate how to manipulate plant
* [(Arabidopsis thaliana 1001 Genomes Data)](https://1001genomes.org/index.html), and it's outgroup's (lyrata, helleri, etc.) data,  using Multiple Alignment Format (MAF) files, located at
* [Plant Ensembl](http://plants.ensembl.org/index.html) ,in order to infer ancestral alleles for the Arabidopsis thaliana.

***

### Pre-requisites

* Unix Environment
* python/2.7.2
* est-sfs-release-2.03
* GNU Scientific Library (gsl)

***

### Protocol - Python - Scripts

* [Loc_Ancestral.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Loc_Ancestral.py) takes Arabidopsis VCF Data and outputs it in a readable format for the EST program.
* [MAF.Arabidopsis.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/MAF.Arabidopsis.py) generates nucleotide counts based on alignments (MAF files) between thaliana and an outgroup species.
* [Transform.EST.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Transform.EST.py) generate nucleotide counts at all variant positions in the thaliana data, not just at the variant alignment positions, which was performed above.


***

### Protocol - Bash Scripts

* [Thaliana_MAF.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Thaliana_MAF.sh) details how to manipulate the Thaliana data into an EST readible format.
* [Species_MAF.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Species_MAF.sh) details how to manipulate the other Species data into an EST readible format.




Prior Steps on a Linux HPC:

tabix -p vcf 1001genomes_snp-short-indel_only_ACGTN.vcf.gz

bcftools +fill-tags 1001genomes_snp-short-indel_only_ACGTN.vcf.gz -- -t AC,AF,AN > Updated1001vcf

awk '{print $1,$2,$4,$5,$8'} Updated1001.vcf > Updated1001.txt

Download MAF alignments from Plant Ensembl

python MAF.Arabidopsis.py Updated1001.txt <maf.sample.name> <species_name> > EST.species.txt

cat <species.txt> > EST.AllSpecies.txt

python Loc_Ancestral.py Updated1001.txt > EST.thaliana.txt

sort -k 1 EST.AllSpecies.txt > EST.AllSpecies.sort.txt
#Species Data = Output from MAF.Arabidopsis.py

sort -k 1 Thaliana.txt > Thaliana.sort.txt
#Thaliana Data = Output from Loc_Ancestral.py

python Transform.EST.py EST.AllSpecies.sort.txt EST.Thaliana.sort.txt > EST.Final.Lyrata.txt

cut -d, -f1 --complement EST.198.Thaliana.sort.txt > EST.198.Thaliana.NoLoc.sort.txt

cut -d, -f1 --complement EST.Final.Lyrata.txt > EST.Final.Lyrata.NoLoc.txt 

cut -d, -f1 --complement EST.Final.Halleri.txt > EST.Final.Halleri.NoLoc.txt 

paste EST.198.Thaliana.NoLoc.sort.txt EST.Final.Lyrata.NoLoc.txt EST.Final.Halleri.NoLoc.txt > EST.Input
