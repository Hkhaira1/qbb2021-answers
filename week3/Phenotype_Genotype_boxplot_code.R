#Make box plot for top SNP using the GS451_IC50 data
boxplot(GS451_IC50$GS451_IC50~rs7257475_genotypes$rs7257475_T, 
        ylab = "Phenotype_GS451", xlab= "Genotype")
 
#Make box plot for top SNP using the CB1908_IC50 data
boxplot(CB1908_IC50$CB1908_IC50~rs10876043_genotypes$rs10876043_G,
        ylab = "Phenotype_CB1908", xlab = "Genotype")
