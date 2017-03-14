library(jmotif)
library(stringr)

### In this script we collect all the unique patterns that exist in each dataset

# train1_motifs <- readRDS('DS4motifs_train.rds')

read_motifs <- function(filename){
   motif_df <- readRDS(filename)
   motifs <- motif_df$motifs
   
   motif_list = c()
   
   # for (i in 1:length(motifs)){
   #   motif_list[[i]] = c(length(motifs[[i]]$Indices), motifs[[i]]$Motif.SAX)
   # }
  
   
   unique_words = c()

   for(i in 1: length(motifs)){
     for(j in 1: length(motifs[[i]]$Indices)){
       unique_words[[i]] <- toString(motifs[[i]]$Motif.SAX[[j]][2,][2:6])
     }
   }

   unq <- unique(unique_words)
   #return (motif_list)
   return (unq)
}



unq_words_train_2 <- read_motifs('DS2motifs_train.rds')
unq_words_test_2 <- read_motifs('DS_2_motifs_test.rds')
unq_words_train_4 <- read_motifs('DS4motifs_train.rds')
unq_words_test_4 <- read_motifs('DS_4_motifs_test.rds')
unq_words_train_3 <- read_motifs('DS3motifs_train.rds')
unq_words_test_3 <- read_motifs('DS_3_motifs_test.rds')


print (unq_words_train_3)
print (unq_words_test_3)


