#!/usr/bin/env python

__author__="Ashikha"

#To analyse the blast results in text format
import sys
import pandas as pd
lines=[] #create an empty list which will be filled with the list of strings after the file is read
headers=["Gene name","Genus","Species","Percentage identity","E value","Query coverage","Accession number"]
df_heads=pd.DataFrame(headers).T
df_heads.to_csv("output_file.csv", mode='a',index=False, header=False) 
with open(sys.argv[1]) as f: 
    lines=f.readlines() 

count=0 #create empty integer variable with 0

for line in lines: 
    count +=1 
    if "Query #" in line: #if you find the word query in the line, do the following
        gene_name_line=lines[count-1] #take one line before that line as there is gene name in that line
        gene_name_line_split=gene_name_line.split() #split the line into multiple elements
        if "Sequences producing significant alignments:" in lines[count+1]: #if "seq.. alignments" is present in the one line after that line, collect the fourth line from that line and split it and then extract only the first element and last three elements
            new_line=lines[count+4]
            split_line_list=new_line.split()
            lst=[gene_name_line_split[2],split_line_list[0],split_line_list[1],split_line_list[-3],split_line_list[-4],split_line_list[-5],split_line_list[-1]]
        else:
            lst=[gene_name_line_split[2],"NA","NA","NA","NA","NA","NA"]
        df=pd.DataFrame(lst).T #convert the list into dataframe and transponse it
        df.to_csv("output_file.csv", mode='a',index=False, header=False) #write the dataframe into a csv file
    else:
        pass


