library(TSMining)
library(foreach)
library(magrittr)
library(plyr)
library(stringr)

read_dataset <- function(i){
  base_path = str_c('./data/dataset', i)
  train_path = str_c(base_path, '/train.txt')
  test_path = str_c(base_path, '/test.txt')
  train = read.table(train_path, sep="", header=FALSE)
  test = read.table(test_path, sep="", header=FALSE)
  dataset <- list(train, test)
  return(dataset)
}


discover_motifs_train <- function(dataset, n){
  
  train = dataset[[1]]

  train[,] <- lapply(train, function(x) {x[is.nan(x)] <- 0; return (x)})
  
  print ("Removing labels")
  train_labels <- train["V1"]
  
  # set label column to empty
  train["V1"] <- NULL
  
  as.matrix(sapply(train, as.numeric))
  
  start <- proc.time()
  
  timestamp()
  
  # for dataset 1, we set window.size = 6 but for others, it is 5
  train$motifs = apply(train, 1, function(x) Func.motif(ts = x, global.norm=TRUE, local.norm=TRUE, window.size=5, overlap=0, w = 5, a = 5, eps=0.01))
  
  filename = str_c("DS_", n, "_motifs_train.rds")
  print(filename)
  saveRDS(train, filename)
}

discover_motifs_test <- function(dataset, n){
  
  test = dataset[[2]]
  
  test[,] <- lapply(test, function(x) {x[is.nan(x)] <- 0; return (x)})
  
  print ("Removing labels")
  test_labels <- test["V1"]
  
  # set label column to empty
  test["V1"] <- NULL
  
  as.matrix(sapply(test, as.numeric))
  start <- proc.time()
  
  timestamp()
  
  # for dataset 1, we set window.size = 6 but for others, it is 5
  test$motifs = apply(test, 1, function(x) Func.motif(ts = x, global.norm=TRUE, local.norm=TRUE, window.size=3, overlap=0, w = 5, a = 5, eps=0.01))
  
  filename = str_c("DS_", n, "_motifs_test.rds")
  print(filename)
  saveRDS(test, filename)
}

dataset <- read_dataset(1)
discover_motifs_train(dataset, 1)
discover_motifs_test(dataset, 1)