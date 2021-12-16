This is a good start! Clustermap and dendrogram both look fine. With the regression, you can use melt, but it's probably going to be pretty difficult. It is probably easier to add two columns to your `transform` dataframe for sex and stage. Then you can loop through the genes (columns) in your dataframe, and regress the logged FPKMs for that gene onto the stage (and sex). As of right now, I think you're regressing FPKMs onto stage for every single gene at once. That's why you're getting the same, almost 0 p-value over and over again. Still need the two qq-plots, the FDR-siginificant genes and overlap, and the volcano plot (-4.5) Let one of the TAs know if you need some help!

2.5/7


I added the sex and stage columns to the transform df and named it transfrom2. From there I did my qqplot again and found the genes that were differentially expressed by stage and sex (the two text files named gene_list and sex_gene_list) and found the overlap between those two (overlap.txt). Finally I ploted the volcano plot.

Great work! Just a couple of minor things:
1. For the QQ plots, the expected distribution is not a normal distribution. Under the null hypothesis, the expected distribution of the p-values is a uniform distribution (think about it, for any given alpha, you would expect the same proportion of p-values to be below that alpha, just by chance). Currently, you're comparing your p-values to a normal distribution, which doesn't make a ton of sense. (-1)
2.I also think you're grabbing the wrong pvalues from the results. It looks like you're grabbing the p-value of the intercept, rather than that of stage. This is also probably why your volcano plot does not look as it should. (-1)

5/7

I fixed the qq plots and ploted the correct P-vaules for both sex and stage diff expressed genes. I also corrted the valcano plot based on those p-vlalues. 

12/15: I see the updates, 7/7
^
A note from Dylan: Your p-values are all a bit off, and the reason is because you accidently removed male_10 and male_11 from your dataframe. You also accidently dropped two of the stage 14 points in your first regression. But, everything else about the code looks totally correct.
