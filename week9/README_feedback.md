This is a good start! Clustermap and dendrogram both look fine. With the regression, you can use melt, but it's probably going to be pretty difficult. It is probably easier to add two columns to your `transform` dataframe for sex and stage. Then you can loop through the genes (columns) in your dataframe, and regress the logged FPKMs for that gene onto the stage (and sex). As of right now, I think you're regressing FPKMs onto stage for every single gene at once. That's why you're getting the same, almost 0 p-value over and over again. Still need the two qq-plots, the FDR-siginificant genes and overlap, and the volcano plot (-4.5) Let one of the TAs know if you need some help!

2.5/7