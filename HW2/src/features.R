library(jmotif)
library(stringr)

### In this script we collect all the unique patterns that exist in each dataset

# Get data in the form of train-test pairs

get_train_test <- function(datasetno) {
  base_path = str_c('./data/dataset', datasetno)
  train_path = str_c(base_path, '/train.txt')
  test_path = str_c(base_path, '/test.txt')
  train = read.table(train_path, sep="", header=FALSE)
  test = read.table(test_path, sep="", header=FALSE)
  dataset <- list(train, test)
  return (dataset)
}

# Get the train labels for any dataset
get_labels <- function(i, tr_te)
{
  dataset = get_train_test(i)
  
  # These are dataframes
  train = dataset[[1]]
  test = dataset[[2]]
  train[,] <- lapply(train, function(x) {x[is.nan(x)] <- 0; return (x)})
  test[,] <- lapply(test, function(x) {x[is.nan(x)] <- 0; return (x)})
  test_labels <- test["V1"]
  train_labels <- train["V1"]
  
  return (train_labels)
}


get_test_length <- function(datasetno)
{
  dataset = get_train_test(datasetno)
  test = dataset[[2]]
  n = dim(test)[1]
  test_labels <- test["V1"]
  test_info = list(n, test_labels)
  return (test_info)
}

read_motifs <- function(filename, datasetno){
   motif_df <- readRDS(filename)
   motifs <- motif_df$motifs
   # 
   # print (length(motifs))
   # 
   # we want to link the labels to the motifs - for using jmotif's bagwise tfidf
   train_labels = get_train_labels(datasetno)
   
   # print (class(train_labels))
   # 
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
  
   # print ("How many motifs are there?")
   # print (length((unique_words)))
   
   # A dataset containing the label and motifs, we later convert this to a table
   # containing the frequency of each motif for a specific label 
   featureset = data.frame(unique_words, train_labels, max_motifs)
   
   # print ("Featureset has type")
   # print (class(featureset))
   # 
   # print(featureset)
   # 
   print ("Length of featureset")
   print (dim(featureset))
   
   # print ("trying to convert to count table")
   # print (str_c("Dataset no: ", datasetno))
   featureset <- as.data.frame(table(featureset))
   
   # This is a dataframe filtered by label
   Label1 <- subset(featureset, V1==1)
   Label2 <- subset(featureset, V1==2)
    
   Label1 <- Label1[, c("unique_words", "Freq")]
   Label2 <- Label2[, c("unique_words", "Freq")]
   
   
   # rename columns for the TF-IDF SAX implementation in jmotif
   colnames(Label1)[1] <- "words"
   colnames(Label1)[2] <- "counts"
   
   colnames(Label2)[1] <- "words"
   colnames(Label2)[2] <- "counts"
   
   # convert factors type to characters
   Label1$words <- as.character(Label1$words)
   #replace commas and spaces - convert to a word instead of spaced characters
   Label1$words <- as.character(gsub(", ", "", Label1$words))
   
   Label2$words <- as.character(Label2$words)
   Label2$words <- as.character(gsub(", ", "", Label2$words))

   # print (str_c(filename, " has ", max_motifs))
   labels = list(Label1, Label2)
   return (labels)
}



#unq_words_train_1 <- read_motifs('DS_1_motifs_train.rds', 1)
train_2_wc <- read_motifs('DS2motifs_train.rds', 2)
#test_2_wc <- read_motifs('DS_2_motifs_test.rds', 2)

tf_idf <- function(label){
  Label1 <- label[[1]]
  Label2 <- label[[2]]
  tfidf = bags_to_tfidf(list("Label1"=Label1, "Label2"=Label2))
  return (tfidf)
}


tfidf = tf_idf(train_2_wc)

# [[1]] is length of test set
# [[2]] is test labels
tl <- get_test_length(1)

predictions = rep(-1, tl[[1]])
labels_test = tl[[2]]
dt = get_train_test(2)
test = dt[[2]]

for (i in 1: tl[[1]]){
  series = test[i, ]
  print (series)
  bag = series_to_wordbag(series, w = 5, p = 5 , a = 5, "exact", 0.01)
  cosines = cosine_sim(list("bag"=bag, "tfidf"= tfidf))
  predictions[i] = which(cosines$cosines == max(cosines$cosines))
}

# classification error

error = length(which((labels_test != predictions))) / length(labels_test)

print(error)



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



