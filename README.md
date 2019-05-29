## Arabidopsis_Project
### Infer Arabidopsis Ancestral Alleles


This directory contains python scripts and bash scripts that demonstrate how to manipulate plant [Arabidopsis thaliana 1001 Genomes Data](https://1001genomes.org/index.html), and it's outgroup's (lyrata, halleri, etc.) data, using Multiple Alignment Format (MAF) files, located at [Plant Ensembl](http://plants.ensembl.org/index.html), in order to infer ancestral alleles for the Arabidopsis thaliana species.

***

### Pre-requisites

* Unix Environment
* python/2.7.2
* est-sfs-release-2.03
* GNU Scientific Library (gsl)

***

### Sample Files

* [Head.Updated1001.txt](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Head.Updated1001.txt) is a sample text file (first 200 lines) of the "Updated1001.txt" file used for thaliana analysis. Details of how this is created is present in [Thaliana_MAF.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Thaliana_MAF.sh)

***

### Protocol - Bash Scripts
#### Implement Bash Scripts in the Following order:
* [Thaliana_MAF.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Thaliana_MAF.sh) details how to manipulate the Thaliana data into an EST readible format.
* [Species_MAF.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Species_MAF.sh) details how to manipulate the other Species data into an EST readible format.
* [Implement.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Implement.sh) details the steps involved implementing the EST algorithm and interrogating it's output.

***

### Protocol - Python Scripts

* [Loc_Ancestral.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Loc_Ancestral.py) takes Arabidopsis VCF Data and outputs it in a readable format for the EST program.
* [MAF.Arabidopsis.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/MAF.Arabidopsis.py) generates nucleotide counts based on alignments (MAF files) between thaliana and an outgroup species.
* [Transform.EST.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Transform.EST.py) generate nucleotide counts at all variant positions in the thaliana data, not just at the variant alignment positions, which was performed above.
* [Outgroup.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Outgroup.py) details what positions are non-applicable, ancestral or dervived, dependent on the ancestral allele probabilities outputted by the EST program.

***

### Contributors

* **Andrew Peters**
* **Cathal Seoighe**

***
