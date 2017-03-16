The source code enclosed in HW2_tekwani is in R.

You will have to install the following libraries:

1) TSMining - simply run install.packages("TSMining")
2) jMotif - To install jMotif, you first need to install package 'devtools' as install.packages("devtools")
Now install jMotif by running install_github('jMotif/jMotif-R')

Files:

1) *.rds files: these contain the motifs as generated through motif_discovery.R. 
2) motif_discovery.R: uses TSMining to run motif discovery on each dataset. You would have to call the function as shown at the end of the file.
Running this file is not needed since I have provided the pickles (*.rds) files. Running motif discovery will take upto 8 hours for 5 datasets.
3) features_*.R: Each dataset has been run separately in its own file. I should modularize this with functions but I was having trouble with R so I could not refactor all this code into a single file. 
4) main.R - Also does motif discovery but separately for train and test files. No need to run this. 


