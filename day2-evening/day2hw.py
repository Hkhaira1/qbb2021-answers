#!/usr/bin/env python3

def FASTAReader(file):
    # Get the first line, which should contain the sequence name
    line = file.readline()

    # Let's make sure the file looks like a FASTA file
    assert line.startswith('>'), "Not a FASTA file"
    
    # Get the sequence name
    seq_id = line[1:].rstrip('\r\n')

    # create a list to contain the 
    sequence = []

    # Get the next line
    line = file.readline()

    # Add a list to hold all of the sequences in
    sequences = []

    # Keep reading lines until we run out
    while line:
        # Check if we've reached a new sequence (in a multi-sequence file)
        if line.startswith('>'):
            # Add previous sequence to list
            sequences.append((seq_id, ''.join(sequence)))
            
            # Record new sequence name and reset sequence
            seq_id = line[1:].rstrip('\r\n')
            sequence = []
        else:
            # Add next chunk of sequence
            sequence.append(line.strip())
        
        # Get the next line
        line = file.readline()
    # Add the last sequence to sequences
    sequences.append((seq_id, ''.join(sequence)))

    return sequences

import sys

f=FASTAReader(open(sys.argv[1],'r'))
f2=FASTAReader(open(sys.argv[2],'r'))
f3=int(sys.argv[3])

query_dna=f[0][1]
#print(query_dna)

def kmerize(seq, kmer_len):
    kmer_dict={}
    for i in range(len(seq)-kmer_len + 1):
        kmer= seq[i:i + kmer_len]
        if kmer in kmer_dict:
            kmer_dict[kmer].append(i)
        else:
            kmer_dict[kmer]=[i]
    return kmer_dict
query_kmer= kmerize(query_dna,f3)

#part 2

for i in f2:
    target_name=i[0]
    target_dna=i[1]
    target_kmer=kmerize(target_dna,f3)
    for q-kmers, q-pos in query_kmer.items():
        if q-kmers in t-kmers:
            print(target_name,t_kmers[q-kmers], q-pos)
    
        