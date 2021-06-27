#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for i in range(len(dna)):
  print(dna[:3])
  print(dna[3:6])
  print(dna[6:9])
  print(dna[9:12])
  print(dna[12:15])
  print(dna[15:18]) 
  print(dna[18:21])
  print(dna[21:24])
  print(dna[24:27])

"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
