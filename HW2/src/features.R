library(jmotif)
library(stringr)

### In this script we collect all the unique patterns that exist in each dataset

# train1_motifs <- readRDS('DS4motifs_train.rds')

read_motifs <- function(filename){
   motif_df <- readRDS(filename)
   motifs <- motif_df$motifs
   
   motif_list = c()
   
   # for (i in 1:length(motifs)){
   #   motifs[[i]] = c(length(motifs[[i]]$Indices), motifs[[i]]$Motif.SAX)
   # }
   # 
   unique_words = c()
   
   for(i in 1: length(motifs)){
     for(j in 1: length(motifs[[i]]$Indices)){
       unique_words[[i]] <- toString(motifs[[i]]$Motif.SAX[[j]][2,][2:6])
     }
   }
   
   unq <- unique(unique_words)
   
   return (unq)
}


unique_words_4 <- read_motifs('DS4motifs_train.rds')

print (unique_words_4)

# 
# motifs = train1_motifs$motifs
# #
# # print(motifs[[1]]$Indices[1])
# 
# train1_motifs = c()
# 
# # print (motifs[[35]]$Motif.SAX[[2]])
# # print (toString(motifs[[35]]$Motif.SAX[[2]][2, ][2:6]))
# 
# unique_motifs_4 = unique(unique_words_4)
# 
# print (unique_motifs_4[[2]])