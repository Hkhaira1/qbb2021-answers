f = open("SRR072893.sam")
count=0
for line in f:
    if not line.startswith("@"):
        count = count + 1
#print(count)

f.close()
#make an empty count, and count into it the alignments without anything that starts with @
#6th column is the cigar, m is the alignment match which means 40 is the perfect aligment 

f = open("SRR072893.sam")
count2=0
for m in f:
    if "40M" in m.strip().split():
        count2+=1
#print(count2)

f.close()

#count the indexes for the 3rd question
f = open("SRR072893.sam")
for i in f:
    i.strip().split()==[4]
    print(i)

        

    
    
    
    





    
    
    


