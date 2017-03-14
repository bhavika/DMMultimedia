train1 <- read.table('./data/dataset1/train.txt', sep= "", header=FALSE)
test1 <- read.table('./data/dataset1/test.txt', sep="", header=FALSE)


plot.ts(train1[1, ])