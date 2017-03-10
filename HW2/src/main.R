library(TSMining)
library(foreach)
library(magrittr)

train1 <- read.table('./data/dataset1/train.txt', sep= "", header=FALSE)
test1 <- read.table('./data/dataset1/test.txt', sep="", header=FALSE)

train1[,] <- lapply(train1, function(x) {x[is.nan(x)] <- 0; return (x)})

test1_labels <- test1["V1"]
train1_labels <- train1["V1"]


# remove the labels from test set
test1["V1"] <- NULL
train1["V1"] <- NULL

print (train1)

as.matrix(sapply(train1, as.numeric))

for (i in 1:dim(train1)[1]){
  ts = as.numeric(train1[i,])
  z <- Func.motif(ts = ts, global.norm = TRUE, local.norm = TRUE, window.size = 5, overlap = 0, w = 5, a = 5, eps=0.01)
}



