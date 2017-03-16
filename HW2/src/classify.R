library(jmotif)
library(stringr)
data("CBF")

# print (class(CBF[["data_train"]]))
# print (class(CBF["labels_train"]))

read_dataset <- function(i){
  base_path = str_c('./data/dataset', i)
  train_path = str_c(base_path, '/train.txt')
  test_path = str_c(base_path, '/test.txt')
  train = read.table(train_path, sep="", header=FALSE)
  test = read.table(test_path, sep="", header=FALSE)
  dataset <- list(train, test)
  return(dataset)
}

# 
# dataset <- read_dataset(4)
# train <- dataset[[1]]
# test <- dataset[[2]]
# 
# 
# labels_train = list(train["V1"])
# train["V1"] <- NULL
# print (class(labels_train))
# 
# data_train = data.matrix(train)
# colnames(data_train) <- NULL
# print (data_train)
# 
# 
# labels_test <- list(test["V1"])
# test["V1"] <- NULL
# print (class(labels_test))

#
# w <- 60 # the sliding window size
# p <- 6  # the PAA size
# a <- 6  # the SAX alphabet size

# convert the train classes to wordbags (the dataset has three labels: 1, 2, 3)
#
# cylinder <- manyseries_to_wordbag(CBF[["data_train"]][CBF[["labels_train"]] == 1,], w, p, a, "exact", 0.01)
# bell <- manyseries_to_wordbag(CBF[["data_train"]][CBF[["labels_train"]] == 2,], w, p, a, "exact", 0.01)
# funnel <- manyseries_to_wordbag(CBF[["data_train"]][CBF[["labels_train"]] == 3,], w, p, a, "exact", 0.01)
# 
# # compute tf*idf weights for three bags
# 
# cylinder = subset(cylinder, counts>1)
# 

tfidf = bags_to_tfidf( list("cylinder" = cylinder, "bell" = bell, "funnel" = funnel) )

# 
# labels_predicted = rep(-1, length(CBF[["labels_test"]]))
# labels_test = CBF[["labels_test"]]
# data_test = CBF[["data_test"]]
# for (i in c(1:length(data_test[,1]))) {
#   series = data_test[i,]
#   bag = series_to_wordbag(series, w, p, a, "exact", 0.01)
#   cosines = cosine_sim(list("bag"=bag, "tfidf" = tfidf))
#   labels_predicted[i] = which(cosines$cosines == max(cosines$cosines))
# }
# 
# # compute the classification error
# #
# error = length(which((labels_test != labels_predicted))) / length(labels_test)
# error
# 
# # findout which time series were misclassified
# #
# # which((labels_test != labels_predicted))
# 
# l = list(c(1, 2, NaN), c(3, 4, NaN))
# x = data.frame(l, header=FALSE)
# 
# max(NaN, NaN)


for (i in c(1, 2, 3)){
  assign(paste("Label", i, sep=""), i)
}

ls()