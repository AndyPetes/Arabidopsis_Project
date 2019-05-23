## Arabidopsis_Project
### Infer Arabidopsis Ancestral Alleles


This directory contains python scripts and bash scripts that demonstrate how to manipulate plant [Arabidopsis thaliana 1001 Genomes Data](https://1001genomes.org/index.html), and it's outgroup's (lyrata, helleri, etc.) data, using Multiple Alignment Format (MAF) files, located at [Plant Ensembl](http://plants.ensembl.org/index.html), in order to infer ancestral alleles for the Arabidopsis thaliana species.

***

### Pre-requisites

* Unix Environment
* python/2.7.2
* est-sfs-release-2.03
* GNU Scientific Library (gsl)

***

### Protocol - Python Scripts

* [Loc_Ancestral.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Loc_Ancestral.py) takes Arabidopsis VCF Data and outputs it in a readable format for the EST program.
* [MAF.Arabidopsis.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/MAF.Arabidopsis.py) generates nucleotide counts based on alignments (MAF files) between thaliana and an outgroup species.
* [Transform.EST.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Transform.EST.py) generate nucleotide counts at all variant positions in the thaliana data, not just at the variant alignment positions, which was performed above.


***

### Protocol - Bash Scripts

* [Thaliana_MAF.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Thaliana_MAF.sh) details how to manipulate the Thaliana data into an EST readible format.
* [Species_MAF.sh](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Species_MAF.sh) details how to manipulate the other Species data into an EST readible format.

***

### Authors

* **Andrew Peters**
* **Cathal Seoighe**

***

### License

This project is licensed  - see the [LICENSE](LICENSE) file for details

***
