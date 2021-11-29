4. When you run freebayes, you should be running it on all of the bam files at once, to create one combined vcf. You'll use this vcf for parts 5-8. You'll need to modify your answer for step 2, so that in your R string, the samples have different ids (ID) as well (-0.25)
 
7. I'm missing the first 1000 lines of your final vcf (-0.5)
8. Again, you should only be running this for one vcf file, your file vcf file. The reason your histograms look a little weird is likely because the data your plotting is strings, rather than ints or floats. You'll need to change the data type before plotting it. Also looking for the snp effect plot (-3)

4.25/8
- Issues fixed: 
- I ran the freebayes for all the bam files at once 
- Printed out the first 1000 lines
- I changed the data types to ints before ploting