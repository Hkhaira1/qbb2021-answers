Hi Harjit, 

- It looks like you're missing the step where you'd extract the methylation data (-0.5) 
- I think as a result of that your plots for the histograms and scatter aren't showing us what they're asked (-2) 
- So, can you do the extraction and then re-plot? 

2.5/5

- I extracted the data and reploted it. 


12-13-21

Good work! Just one issue:
1. You're using python to map the bedgraph annotations onto the promoter bed file, which in theory is fine, but `bedtools map` is designed specifically for this, and is almost certainly easier. That being said, your code actually looks good in that respect, so I'm not entirely sure why your results don't match our results. But I'm not going to take off any points on the histograms because I don't know what the issue is!

5/5
