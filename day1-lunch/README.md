cp *.bed ../../qbb2021-answers/day1-lunch
cp *.dm6.chrom.sizes ../../qbb2021-answers/day1-lunch
>feature_count.txt
#coppied the files and created a feature count file
wc K27me3.bed > feature_count.txt
wc K9me3.bed >> feature_count.txt
wc fbgenes.bed >> feature_count.txt
wc S2_9state.bed >> feature_count.txt
wc LADs_Kc.bed >> feature_count.txt
wc K4me3.bed >> feature_count.txt
#recoreded all the features from the file in the feature count file
Biological observation: LAD file is smaller, and the line counts are less than character/word count
cut -f 1 fbgenes.bed | sort | uniq -c > fbgenes.info
Observation about fbgenes.bed file: chr3 has more genes associated with it 
#recoreded observations about the files
>chr-with-fbgenes-k9.txt
bedtools intersect -a fbgenes.bed -b K9me3.bed > chr-with-fbgenes-k9.txt
#created a chr-with-fbgenes-k9 txt file which contains chromosomes enriched in genes that overlap k9me3
Biological observations:certain chromosomes contain more enriched genes than others.ChrY is smaller than the rest as expected.
