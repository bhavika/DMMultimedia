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

get_unique_labels <- function(datasetno, tr_te){
  labels = get_labels(datasetno, tr_te)
  unique_labels = unique(labels)
  print(unique_labels)
}

read_motifs <- function(filename, datasetno, tr_te){
  motif_df <- readRDS(filename)
  motifs <- motif_df$motifs
  
  # we want to link the labels to the motifs - for using jmotif's bagwise tfidf
  labels = get_labels(datasetno, tr_te)
  
  unique_labels = unique(labels)
  print(unique_labels)
  
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
  
  
  # print ("trying to convert to count table")
  # print (str_c("Dataset no: ", datasetno))
  featureset <- as.data.frame(table(featureset))
  
  
  # This is a dataframe filtered by label
  Label1 <- subset(featureset, V1==1)
  Label2 <- subset(featureset, V1==2)
  Label3 <- subset(featureset, V1==3)
  Label4 <- subset(featureset, V1==4)
  Label5 <- subset(featureset, V1==5)
  Label6 <- subset(featureset, V1==6)
  Label7 <- subset(featureset, V1==7)
  Label8 <- subset(featureset, V1==8)
  Label9 <- subset(featureset, V1==9)
  Label10 <- subset(featureset, V1==10)
  Label11 <- subset(featureset, V1==11)
  Label12 <- subset(featureset, V1==12)
  Label13 <- subset(featureset, V1==13)
  Label14 <- subset(featureset, V1==14)
  Label15 <- subset(featureset, V1==15)
  
  Label1 <- Label1[, c("words", "Freq")]
  Label2 <- Label2[, c("words", "Freq")]
  Label3 <- Label3[, c("words", "Freq")]
  Label4 <- Label4[, c("words", "Freq")]
  Label5 <- Label5[, c("words", "Freq")]
  Label6 <- Label6[, c("words", "Freq")]
  Label7 <- Label7[, c("words", "Freq")]
  Label8 <- Label8[, c("words", "Freq")]
  Label9 <- Label9[, c("words", "Freq")]
  Label10 <- Label10[, c("words", "Freq")]
  Label11 <- Label11[, c("words", "Freq")]
  Label12 <- Label12[, c("words", "Freq")]
  Label13 <- Label13[, c("words", "Freq")]
  Label14 <- Label14[, c("words", "Freq")]
  Label15 <- Label15[, c("words", "Freq")]
  
  # rename columns for the TF-IDF SAX implementation in jmotif - words & counts
  colnames(Label1)[2] <- "counts"
  colnames(Label2)[2] <- "counts"
  colnames(Label3)[2] <- "counts"
  colnames(Label4)[2] <- "counts"
  colnames(Label5)[2] <- "counts"
  colnames(Label6)[2] <- "counts"
  colnames(Label7)[2] <- "counts"
  colnames(Label8)[2] <- "counts"
  colnames(Label9)[2] <- "counts"
  colnames(Label10)[2] <- "counts"
  colnames(Label11)[2] <- "counts"
  colnames(Label12)[2] <- "counts"
  colnames(Label13)[2] <- "counts"
  colnames(Label14)[2] <- "counts"
  colnames(Label15)[2] <- "counts"
  
  # convert factors type to characters
  Label1$words <- as.character(Label1$words)
  #replace commas and spaces - convert to a word instead of spaced characters
  Label1$words <- as.character(gsub(", ", "", Label1$words))
  
  Label2$words <- as.character(Label2$words)
  Label2$words <- as.character(gsub(", ", "", Label2$words))
  
  Label3$words <- as.character(Label3$words)
  Label3$words <- as.character(gsub(", ", "", Label3$words))
  
  Label4$words <- as.character(Label4$words)
  Label4$words <- as.character(gsub(", ", "", Label4$words))
  
  Label5$words <- as.character(Label5$words)
  Label5$words <- as.character(gsub(", ", "", Label5$words))
  
  Label6$words <- as.character(Label6$words)
  Label6$words <- as.character(gsub(", ", "", Label6$words))
  
  Label7$words <- as.character(Label7$words)
  Label7$words <- as.character(gsub(", ", "", Label7$words))
  
  Label8$words <- as.character(Label8$words)
  Label8$words <- as.character(gsub(", ", "", Label8$words))
  
  Label9$words <- as.character(Label9$words)
  Label9$words <- as.character(gsub(", ", "", Label9$words))
  
  Label10$words <- as.character(Label10$words)
  Label10$words <- as.character(gsub(", ", "", Label10$words))

  Label11$words <- as.character(Label11$words)
  Label11$words <- as.character(gsub(", ", "", Label11$words))
  
  
  Label12$words <- as.character(Label12$words)
  Label12$words <- as.character(gsub(", ", "", Label12$words))
  
  
  Label13$words <- as.character(Label13$words)
  Label13$words <- as.character(gsub(", ", "", Label13$words))
  
  
  Label14$words <- as.character(Label14$words)
  Label14$words <- as.character(gsub(", ", "", Label14$words))
  
  
  Label15$words <- as.character(Label15$words)
  Label15$words <- as.character(gsub(", ", "", Label15$words))
  # print (str_c(filename, " has ", max_motifs))
  bags = list(Label1, Label2, Label3, Label4, Label5, Label6, Label7, Label8, Label9, Label10, Label11, Label12, Label13, Label14, Label15)
  return (bags)
}


tf_idf <- function(bags){
  Label1 <- bags[[1]]
  Label2 <- bags[[2]]
  Label3 <- bags[[3]]
  Label4 <- bags[[4]]
  Label5 <- bags[[5]]
  Label6 <- bags[[6]]
  Label7 <- bags[[7]]
  Label8 <- bags[[8]]
  Label9 <- bags[[9]]
  Label10 <- bags[[10]]
  Label11 <- bags[[11]]
  Label12 <- bags[[12]]
  Label13 <- bags[[13]]
  Label14 <- bags[[14]]
  Label15 <- bags[[15]]
  
  
  tfidf = bags_to_tfidf(list("Label1"=Label1, "Label2"=Label2, "Label3"=Label3, "Label4"=Label4, "Label5"=Label5, "Label6"=Label6,
                             "Label7"=Label7, "Label8"=Label8, "Label9"=Label9, "Label10"=Label10, "Label11"=Label11
                             ,"Label12"=Label12, "Label13"=Label13, "Label14"=Label14, "Label15"=Label15))
  return (tfidf)
}

classify <- function(datasetno, tfidf)
{
  testlength <- get_length_dataset(datasetno, "test")
  labels_test <- get_labels(datasetno, "test")
  predictions <- rep (-1, testlength)
  dt = get_train_test(datasetno)
  test = dt[[2]]

    # This code has been adapted from [2]  Pavel Senin, jMotif-R, https://github.com/jMotif/jmotif-R 
  # The example given is from the SAX VSM classifier. It has been modified for our implementation.
  
  for (i in 1: testlength){
    series = test[i, ]
    series = as.numeric(series)
    bag = series_to_wordbag(series, w = 5, p = 5 , a = 5, "exact", 0.01)
    cosines = cosine_sim(list("bag"=bag, "tfidf"= tfidf))
    if ( length(a <- which(cosines$cosines == max(cosines$cosines))) == 0){
      predictions[i] = sample(1:15, 1)
    }
    else{
      predictions[i] = which(cosines$cosines == max(cosines$cosines))
    }
  }
  
  print(predictions)
  # classification error
  accuracy = length(which((labels_test == predictions)))/testlength
  error = length(which((labels_test != predictions))) / testlength
  print (accuracy)
}


train_bags <- read_motifs('DS4motifs_train.rds', 4 , "train")
tfidf = tf_idf(train_bags)
classify(4, tfidf)

