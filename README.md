# BLAST_parse
To get the top hit while performing BLAST for multiple DNA/protein sequences

While performing BLAST for multiple (say more than 10) gene sequences, running BLAST_parse.py will give the genus, species, percentage identity, E value, query coverage and accession number of the top hit for each gene sequence in a single .csv file.


### Input:

The BLAST results will be given as input for this python script. Among the multiple BLAST output formats provided, the results should be downloaded in .text format (file name used in the example below is blast_output.txt). The BLAST's built-in feature to sort or filter the results can be applied before downloading the result in .txt format. Ensure that the gene name is mentioned without space after ">" symbol in the fasta format.


### Pre-requirement:

Python

Pandas

sys


### Usage:

`python BLAST_parse.py blast_output.txt` 
