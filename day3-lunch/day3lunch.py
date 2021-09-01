import sys

gtf_file = sys.argv[1]
mut_chrom = sys.argv[2]
target_pos = int(sys.argv[3])
f = open(gtf_file)

genes = []
for line in f:
    if line.startswith("#"):
        continue
    fields = line.strip("\r\n").split("\t")
    start = int(fields[3])
    end = int(fields[4])
    if (fields[0] == mut_chrom) and (fields[2] == "gene") and ('gene_biotype "protein_coding"' in line):
        subfields = fields[-1].split(';')
        for field in subfields:
            if "gene_name" in field:
                gene_name = field.split()[1]
        genes.append((gene_name, start, end))
# print(genes)

high=len(genes)-1
low= 0
current_index= (high+low)//2

counter=0
while True:
    counter+=1
    current_gene=genes[current_index][0]
    current_pos=genes[current_index][1]
    # print("Current",type(current_pos))
    # print("Target",type(target_pos))
    if current_pos<target_pos:
        if low==current_index:
            high_pos=genes[high][1]
            low_pos=genes[low][1]
            #calculating the distance 
            if abs(high_pos-target_pos)>abs(low_pos-target_pos):
                low_genes=genes[low][0]
                print(low_genes)
                print(low_pos-target_pos)
            else:
                high_genes=genes[high][0]
                print(high_genes)
                print(high_pos-target_pos)s
            #closest_gene=current_gene
            #print(closest_gene)
            break
        low=current_index
        current_index=(high+low)//2
    else:
        if high==current_index:
            high_pos=genes[high][1]
            low_pos=genes[low][1]
            #calculating the distance
            if abs(high_pos-target_pos)>abs(low_pos-target_pos):
                low_genes=genes[low][0]
                print(low_genes)
                print(low_pos-target_pos)
            else:
                high_genes=genes[high][0]
                print(high_genes)
                print(high_pos-target_pos)
            #closest_gene=current_gene
           # print(closest_gene)
            break
        high=current_index
        current_index=(high+low)//2
print(counter)
        
        


    
        