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
  
  if(identical(tr_te, "test"))
    return (test_labels)
  else{
    return (train_labels)
  }
  
}

get_length_dataset <- function(datasetno, tr_te)
{
  dataset = get_train_test(datasetno)
  
  if(identical(tr_te, "test")){
    test = dataset[[2]]
    n = dim(test)[1]
    return (n)  
  }
  
  else{
    train = dataset[[1]]
    n = dim(train)[1]
    return (n)
  }
}


read_motifs <- function(filename, datasetno, tr_te){
   motif_df <- readRDS(filename)
   motifs <- motif_df$motifs
   
   # we want to link the labels to the motifs - for using jmotif's bagwise tfidf
   labels = get_labels(datasetno, tr_te)
   
   motif_list = c()
   max_motifs = 0
   words = c()

   for(i in 1: length(motifs)){
     for(j in 1: length(motifs[[i]]$Indices)){
       
       words[[i]] <- toString(motifs[[i]]$Motif.SAX[[j]][2,][2:6])
       
       if((length(motifs[[i]]$Indices)) > max_motifs) {
         max_motifs = length(motifs[[i]]$Indices)
       }
     }
   }
   
   # A dataset containing the label and motifs, we later convert this to a table
   # containing the frequency of each motif for a specific label 
   featureset = data.frame(words, labels, max_motifs)
   
   print ("Length of featureset")
   print (dim(featureset))
   
   # print ("trying to convert to count table")
   # print (str_c("Dataset no: ", datasetno))
   featureset <- as.data.frame(table(featureset))
   
   # This is a dataframe filtered by label
   Label1 <- subset(featureset, V1==1)
   Label2 <- subset(featureset, V1==2)
    
   Label1 <- Label1[, c("words", "Freq")]
   Label2 <- Label2[, c("words", "Freq")]
   
   
   # rename columns for the TF-IDF SAX implementation in jmotif - words & counts
   colnames(Label1)[2] <- "counts"
   colnames(Label2)[2] <- "counts"
   
   # convert factors type to characters
   Label1$words <- as.character(Label1$words)
   #replace commas and spaces - convert to a word instead of spaced characters
   Label1$words <- as.character(gsub(", ", "", Label1$words))
   
   Label2$words <- as.character(Label2$words)
   Label2$words <- as.character(gsub(", ", "", Label2$words))

   # print (str_c(filename, " has ", max_motifs))
   bags = list(Label1, Label2)
   return (bags)
}


tf_idf <- function(bags){
  Label1 <- bags[[1]]
  Label2 <- bags[[2]]
  tfidf = bags_to_tfidf(list("Label1"=Label1, "Label2"=Label2))
  return (tfidf)
}

classify <- function(datasetno, tfidf)
{
  testlength <- get_length_dataset(datasetno, "test")
  labels_test <- get_labels(datasetno, "test")
  predictions <- rep (-1, testlength)
  dt = get_train_test(datasetno)
  test = dt[[2]]
  
  for (i in 1: testlength){
    series = test[i, ]
    series = as.numeric(series)
    bag = series_to_wordbag(series, w = 5, p = 5 , a = 5, "exact", 0.01)
    cosines = cosine_sim(list("bag"=bag, "tfidf"= tfidf))
    predictions[i] = which(cosines$cosines == max(cosines$cosines))
  }
  
  # classification error
  error = length(which((labels_test != predictions))) / testlength
  return (error)
}



# train_2_bags <- read_motifs('DS2motifs_train.rds', 2, "train")
# tfidf = tf_idf(train_2_bags)

q <- get_labels(4, "train")
q <- list(q)
lbls = unique(q)
lbls