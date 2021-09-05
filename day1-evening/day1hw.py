f = open("SRR072893.sam")
#set all counters to zero outside the for loop
count1=0
count2=0
total_mapq=0
in_range=0
uniq_reads=set()
#start the for loop
for line in f:
    if not line.startswith("@"):
        count1+=1 #cut out the @s at the beiging of the file to count the alignments
        read = line.strip().split('\t')
        #counting the number of perfect aligenments
        if read[5]=="40M":
            count2+=1
            #counting the total MAPQ scores
        total_mapq+=int(read[4])
        pos=int(read[3])
        if (read[2]=='2L') and (pos >= 10000) and (pos<=20000):
            in_range+=1
        uniq_reads.add((pos,read[5]))
f.close()
print("Number of alignments:", count1)
print("Number of perfect alignments:", count2)
avg=total_mapq/count1
print("Average MAPQ score:", avg)
print("Reads starting on Chr2L:", in_range)
pcr=count1 - len(uniq_reads)
print("PCR duplicates:",pcr)



#EXTRA CODE
# f = open("SRR072893.sam")
# count=0
# for line in f:
#     if not line.startswith("@"):
#         count = count + 1
# #print(count)
#
# f.close()
# #make an empty count, and count into it the alignments without anything that starts with @
# #6th column is the cigar, m is the alignment match which means 40 is the perfect aligment
#
# f = open("SRR072893.sam")
# count2=0
# for m in f:
#     if "40M" in m.strip().split():
#         count2+=1
# #print(count2)
#
# f.close()

#count the indexes for the 3rd question
# f = open("SRR072893.sam")
# count=0
# count2=0
# total_mapq=0
# for line in f:
#     if not line.startswith("@"):
#         count = count + 1
#         col=line.strip().split("\t")
# for m in f:
#     if "40M" in m.strip().split():
#         count2+=1
#         col=line.strip().split("\t")
#         if (col[4])==None:
#             print("Error.2")
#         total_mapq +=int(col[4])
# print(total_mapq)


    
    
    
    





    
    
    


