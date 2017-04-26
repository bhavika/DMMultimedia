library(TSMining)
library(foreach)
library(magrittr)
library(plyr)
library(stringr)

read_dataset <- function(i){
  base_path = str_c('../data/dataset', i)
  train_path = str_c(base_path, '/train.txt')
  test_path = str_c(base_path, '/test.txt')
  train = read.table(train_path, sep="", header=FALSE)
  test = read.table(test_path, sep="", header=FALSE)
  dataset <- list(train, test)
  return(dataset)
}

convert_ts2SAX <- function(dataset, n){
  
  train <- dataset[[1]]
  train[,] <- lapply(train, function(x) {x[is.nan(x)] <- 0; return (x)})
  
  print ("Removing labels")
  train_labels <- train["V1"]
  
  # set label column to empty
  train["V1"] <- NULL
  
  as.matrix(sapply(train, as.numeric))
  
  start <- proc.time()
  
  timestamp()
  train$SAX = apply(train, 1, function(x) Func.SAX(x = x, w = dim(train)[1], a = 7, eps = 0.01, norm = TRUE))
  
  print (train)
  write.table(train$SAX, file = "train4.csv",  row.names = FALSE, col.names = FALSE)
}


dataset <- read_dataset(4)
convert_ts2SAX(dataset, 4)