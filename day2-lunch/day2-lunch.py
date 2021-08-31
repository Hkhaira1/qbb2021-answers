import sys

#f= open(sys.argv[1], 'r')
# for line in f:
 #    print(line.strip())
#
#
#f2= open(sys.argv[2],'r')
# for line in f2:
#     print(line.strip())
f=open(sys.argv[1])    
flydict= dict()
for line in f:
    fields= line.strip().split('\t')
    flydict[fields[0]]= fields[1]

f2=open(sys.argv[2],'r')
for line in f2:
    fields=line.strip().split('\t')
    print(fields)
    gene_name=fields[8]
    if gene_name in flydict:
        protein_id= flydict[gene_name]
        fields[8]=protein_id
        print(gene_name, protein_id)
        print(fields)
    else:
        if len(sys.argv)==4:
            fields[8]=sys.argv[3]
            print(fields)
        else:
            continue