library(jmotif)
library(stringr)

### In this script we collect all the unique patterns that exist in each dataset

get_labels_dataset <- function(i)
{
  base_path = str_c('./data/dataset', i)
  train_path = str_c(base_path, '/train.txt')
  test_path = str_c(base_path, '/test.txt')
  train = read.table(train_path, sep="", header=FALSE)
  test = read.table(test_path, sep="", header=FALSE)
  dataset <- list(train, test)
  
  # These are dataframes
  train = dataset[[1]]
  test = dataset[[2]]
  
  train[,] <- lapply(train, function(x) {x[is.nan(x)] <- 0; return (x)})
  test[,] <- lapply(test, function(x) {x[is.nan(x)] <- 0; return (x)})
  
  print ("Removing labels")
  test_labels <- test["V1"]
  train_labels <- train["V1"]
  
  labels = c(train_labels, test_labels)
  
  return (train)
}

read_motifs <- function(filename, datasetno){
   motif_df <- readRDS(filename)
   motifs <- motif_df$motifs
   
   print (length(motifs))
   
   # we want to link the labels to the motifs - for using jmotif's bagwise tfidf
   train = get_labels_dataset(datasetno)
  
   train_labels <- train["V1"]
   
   print (class(train_labels))
   
   motif_list = c()
   max_motifs = 0
   unique_words = c()

   for(i in 1: length(motifs)){
     for(j in 1: length(motifs[[i]]$Indices)){
       
       unique_words[[i]] <- toString(motifs[[i]]$Motif.SAX[[j]][2,][2:6])
       
       if((length(motifs[[i]]$Indices)) > max_motifs) {
         max_motifs = length(motifs[[i]]$Indices)
       }
     }
   }
  
   print ("How many motifs are there?")
   print (length((unique_words)))
   
   # A dataset containing the label and motifs, we later convert this to a table
   # containing the frequency of each motif for a specific label 
   featureset = data.frame(unique_words, train_labels, max_motifs)
   
   # print ("Featureset has type")
   # print (class(featureset))
   # 
   # print(featureset)
   # 
   # print ("Length of featureset")
   # print (dim(featureset))
   
   print ("trying to convert to count table")
   print (str_c("Dataset no: ", datasetno))
   featureset <- as.data.frame(table(featureset))
   
   # This is a dataframe filtered by label
   Label1 <- subset(featureset, V1==1)
   Label2 <- subset(featureset, V1==2)
   Label3 <- subset(featureset, V1==3)
   Label1 <- Label1[, c("unique_words", "Freq")]
   Label2 <- Label2[, c("unique_words", "Freq")]
   Label3 <- Label3[, c("unique_words", "Freq")]
   
   # rename columns for the TF-IDF SAX implementation in jmotif
   colnames(Label1)[1] <- "words"
   colnames(Label1)[2] <- "count"
   
   colnames(Label2)[1] <- "words"
   colnames(Label2)[2] <- "count"
   
   colnames(Label3)[1] <- "words"
   colnames(Label3)[2] <- "count"

   # convert factors type to characters
   Label1$words <- as.character(Label1$words)
   #replace commas and spaces - convert to a word instead of spaced characters
   Label1$words <- as.character(gsub(", ", "", Label1$words))
   
   Label2$words <- as.character(Label2$words)
   Label2$words <- as.character(gsub(", ", "", Label2$words))
  
   Label3$words <- as.character(Label3$words)
   Label3$words <- as.character(gsub(", ", "", Label3$words))
   
   print (str_c(filename, " has ", max_motifs))
   
   #TFIDF using jMotif
   tfidf = bags_to_tfidf(list("Label1"= Label1)

   print (tfidf)
   # print (as.data.frame(table(unique_words)))

   # unq <- unique(unique_words)
   # return (unq)
}

unq_words_train_1 <- read_motifs('DS_1_motifs_train.rds', 1)
#unq_words_train_2 <- read_motifs('DS2motifs_train.rds', 2)
#unq_words_test_2 <- read_motifs('DS_2_motifs_test.rds', 2)
# unq_words_train_4 <- read_motifs('DS4motifs_train.rds', 4)
# unq_words_test_4 <- read_motifs('DS_4_motifs_test.rds', 4)
# unq_words_train_3 <- read_motifs('DS3motifs_train.rds', 3)
# unq_words_test_3 <- read_motifs('DS_3_motifs_test.rds', 3 )
# unq_words_train_5 <- read_motifs('DS5motifs_train.rds', 5)
# unq_words_test_5 <- read_motifs('DS_5_motifs_test.rds', 5)

# print ("Dataset 2: ")
# print (union(unq_words_test_2, unq_words_train_2))
# 
# print ("Dataset 3: ")
# print (union(unq_words_test_3, unq_words_train_3))
# 
# print ("Dataset 4: ")
# print (union(unq_words_test_4, unq_words_train_4))
# 
# print ("Dataset 5: ")
# print (union(unq_words_test_5, unq_words_train_5))



