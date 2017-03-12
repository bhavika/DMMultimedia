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

dataset  <- read_dataset(5)

train = dataset[[1]]
test = dataset[[2]]

train[,] <- lapply(train, function(x) {x[is.nan(x)] <- 0; return (x)})
test[,] <- lapply(test, function(x) {x[is.nan(x)] <- 0; return (x)})

test_labels <- test["V1"]
train_labels <- train["V1"]

# remove the labels from test set
test["V1"] <- NULL
train["V1"] <- NULL

as.matrix(sapply(train, as.numeric))

discover_motifs <- function(x){
  return (Func.motif(ts = x, global.norm=TRUE, local.norm=TRUE, window.size=5, overlap=0, w = 5, a = 5, eps=0.01))
}

as.matrix(sapply(train, as.numeric))

train$motifs = apply(train, 1, function(x) Func.motif(ts = x, global.norm=TRUE, local.norm=TRUE, window.size=5, overlap=0, w = 5, a = 5, eps=0.01))

