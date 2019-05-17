# Arabidopsis_Project

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
