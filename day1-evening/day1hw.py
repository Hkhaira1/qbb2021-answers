f = open("SRR072893.sam")
count=0
for line in f:
    if not line.startswith("@"):
        count = count + 1
print(count)
#make an empty count, and count into it the alignments without anything that starts with @
#6th column is the cigar, m is the alignment match which means 40 is the perfect aligment 

for m in f:
    if m==40:
        print(m)
        

    
    
    
    





    
    
    


