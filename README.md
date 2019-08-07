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
* [MAF.Species.Tab.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/MAF.Species.Tab.py) generates nucleotide counts based on alignments (MAF files) between thaliana and an outgroup species.
* [get_uniq.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/get_uniq.py) outputs the genomic locations and associated nucleotide that occur exactly once after alignment, i.e. unique positions.
* [reformat.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/reformat.py) a small script that reformats the output in a more readable way for following steps.
* [reformat2.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/reformat2.py) outputs all recurring positions, using the unique positions as a dictionary.
* [Transform.EST.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Transform.EST.py) generate nucleotide counts at all variant positions in the thaliana data, not just at the variant alignment positions, which was performed above.
* [New_Outgroup.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/New_Outgroup.py) details what positions are non-applicable, ancestral or dervived, dependent on the ancestral allele probabilities outputted by the EST program.
* [Out_Estimate_State.Ancestral.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Out_Estimate_State.Ancestral.py) extracts the allele nucleotide and ancestral state at each position for each sample used.
* [Out_Estimate_State.Derived.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Out_Estimate_State.Derived.py) extracts the allele nucleotide and derived state at each position for each sample used.
* [Specific_Allele_Count.prac.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/Specific_Allele_Count.prac.py) counts number of derived and ancestral alleles in each inidiviudal file in accordance with the ancestral probabilities previously generated.
* [InputAA.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/InputAA.py) Uses the output from "Out_Estimate_State.py" to create a text file with output compatabile with the "AA" field in a VCF file.
* [FinalAA.py](https://github.com/AndyPetes/Arabidopsis_Project/blob/master/FinalAA.py) uses the output just generated and inputs this information into the 100.Updated.vcf file

***

### Contributors

* **Andrew Peters**
* **Cathal Seoighe**

***
