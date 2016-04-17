#!/bin/bash

#BSUB -L /bin/bash
#BSUB -J <job_name>
#BSUB -q priority

module add UHTS/Analysis/samtools/latest

python3 kallisto_sam_convertor.py <pseudoalignment.sam> /scratch/cluster/monthly/mls_2015/SAGE/genome/Pseudomonas_protegens_S5_genome.gtf | samtools view -bS - | samtools sort - -o <output.bam>
