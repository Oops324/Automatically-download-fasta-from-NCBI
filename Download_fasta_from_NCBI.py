#!/usr/bin/env python

'''
Author: Fei Jing
Date: 1/Nov/2017
Usage: python primer_pipeline.py pathogen.gb
Output:
pathogen_filter.fasta
'''
import re
import datetime
import sys
import os
from Bio import Entrez

def Eutility(Pathogen,startYear):
        Entrez.email = "primer@gmail.com"
        print "#"*30,"Get pathogen fasta from NCBI"

        search_handle = Entrez.esearch(db="nucleotide", term="Adenoviridae[Porgn] AND 2015[EDAT] AND hexon[All fields] AND human[All fields]", usehistory="y",idtype="acc",restart="0",retmax="10")
        search_record = Entrez.read(search_handle)
        webenv = search_record["WebEnv"]
        query_key = search_record["QueryKey"]
        
        print search_record["QueryTranslation"]
        fastaName = "Result_human_hexon_" + Pathogen +"_" + startYear  + ".fa"
        fetch_handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text",webenv=webenv,query_key=query_key,idtype="acc",retmax="10000")
        data = fetch_handle.read()
        file = open(fastaName,'w')
        file.write(data)

if __name__=="__main__":
        pathogen = sys.argv[1]
        startYear = sys.argv[2]
        Pathogen = pathogen.replace(" ","_")
	Eutility(Pathogen,startYear)
