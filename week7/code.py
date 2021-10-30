import numpy as np
import pandas as pd
import sys
##I had to import the fastareader code because I could not get it to work.
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
#######################################################################################################################################################################################


##STEP 1 READING IN THE PARAMETERS

fasta_sequences=FASTAReader(open(sys.argv[1],'r'))
scoring_matrix_file=(open(sys.argv[2],'r')) #10
gap_penalty= float(sys.argv[3])
out_filepath=sys.argv[4]



##assign sequences in the fasta file to sequence 1 and 2
for sequence in fasta_sequences:
    seq_id = sequence[0]
    if "HUM" in seq_id:
        sequence1 = sequence[1]
    elif "MUS" in seq_id:
        sequence2 = sequence[1]
        
#Make lists to read the scoring matrix
scoring_matrix_list = []
scoring_matrix_index = []


# Save DNA and amino acids as indices for the scoring matrix
for line in scoring_matrix_file:
    if line.startswith(" "):
        scoring_matrix_index = line.strip().split()
        continue
        
# have to convert the scores to float, then append to a list
        scores = line.strip().split()[1:]
        for i in range(len(scores)):
            scores[i] = float(scores[i])
            scoring_matrix_list.append(scores)

# convert scoring matrix to an numpy array 

##STEP 2 Initailing matrics

scoring_matrix = pd.read_csv(sys.argv[2],delim_whitespace=True,index_col=0)

#start F matrix
F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

#start traceback matrix
traceback = np.empty((len(sequence1)+1, len(sequence2)+1), dtype= str)

##STEP 3 Populating the matrics

#Fill in the first row and column for the F matrix, similar to the live coding

# first row
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i*gap_penalty
    
    #First column
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j*gap_penalty
    
    # Populate the matrix


for i in range(1,len(sequence1)+1):
    for j in range(1,len(sequence2)+1):
        #loop through columns
#Need to first get match score from score matrix
        d=F_matrix[i-1,j-1] + scoring_matrix.loc[sequence1[i-1],sequence2[j-1]]
        # index1 = scoring_matrix_index.index(sequence1[i-1])
#         index2 = scoring_matrix_index.index(sequence2[j-1])
#
#         match_score = scoring_matrix[index1, index2]
            

        # d = F_matrix[i-1, j-1] + match_score
 #        d = F_matrix[i-1, j-1] + mismatch_score
        h = F_matrix[i, j-1] + gap_penalty
        v = F_matrix[i-1, j] + gap_penalty
        
        F_matrix[i,j] = max(d, h, v)
        if max(d, h, v) == d:
            traceback[i,j] = 'd'
        elif max(d, h, v) == h:
             traceback[i,j] = 'h'
        elif  max(d,h,v)== v:
            traceback[i,j] = 'v'

#print(F_matrix)
#print(traceback)

i,j = (len(sequence1),len(sequence2))
a=''
b=''

while i>0 and j>0:
    if traceback[i,j]== 'd':
        a+=sequence1[i-1]
        b+=sequence2[j-1]
        i,j=i-1,j-1
        continue
    if traceback[i,j]=='h':
        a+=sequence1[i-1]
        b+='-'
        i,j=i,j-1
        continue
    if traceback[i,j]=='v':
        a+='-'
        b+=sequence2[j-1]
        i,j=i-1,j
        continue
        
c=a[::-1]
d=b[::-1]



output1= open(out_filepath,'w')
output1.write('Align 1:|t{}|n'.format(c))
output1.write('Align 1:|t{}|n'.format(d))
output1.close()

output2= open(out_filepath,'w')
output2.write('Align 1:|t{}|n'.format(c))
output2.write('Align 1:|t{}|n'.format(d))
output2.close()

count1=c.count('-')
count2=d.count('-')
print(count1)
print(count2)
print(F_matrix[-1,-1])