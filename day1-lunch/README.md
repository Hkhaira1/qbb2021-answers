cp *.bed ../../qbb2021-answers/day1-lunch
cp *.dm6.chrom.sizes ../../qbb2021-answers/day1-lunch
>feature_count.txt
wc K27me3.bed > feature_count.txt
wc K9me3.bed >> feature_count.txt
wc fbgenes.bed >> feature_count.txt
wc S2_9state.bed >> feature_count.txt
wc LADs_Kc.bed >> feature_count.txt
wc K4me3.bed >> feature_count.txt
Biological observation: LAD file is smaller, and the line counts are less than character/word count
cut -f 1 fbgenes.bed | sort | uniq -c > fbgenes.info
Observation about fbgenes.bed file: chr3 has more genes associated with it 
