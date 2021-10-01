#Using the qqman R package we can create manhattan plot and QQ plots for the assocation data.
#QQ plot for the GS451_IC50 DATA
qq(GS451_IC50$P)
#manhattan plot for the GS451_IC50 DATA
manhattan(GS451_IC50, chr = "CHR", bp= "BP", p= "P", snp= "SNP",
          col=c('black','gray'), chrlabs = NULL,
          suggestiveline = -log10(1e-05), genomewideline = F,
          highlight=NULL, logp= TRUE, annotateTop = TRUE)
#QQ plot for the CB1908_IC50 DATA
qq(CB1908_IC50$P)
#manhattan plot for the CB1908_IC50 DATA
manhattan(CB1908_IC50, chr = "CHR", bp= "BP", p= "P", snp= "SNP",
          col=c('black','gray'), chrlabs = NULL,
          suggestiveline = -log10(1e-05),genomewideline = F, 
          logp= TRUE, annotateTop = TRUE)
##Highlights the top SNPS
manhattan(CB1908_IC50, annotatePval = 0.05)
manhattan(GS451_IC50, annotatePval = 0.05)
