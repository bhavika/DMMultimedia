library(jmotif)
library(stringr)

# train1_motifs <- readRDS('DS3motifs_train.rds')
# 
# motifs = train1_motifs$motifs
# #
# # print(motifs[[1]]$Indices[1])
# 
# train1_motifs = c()
# 
# for (i in 1:length(motifs)){
#   train1_motifs[[i]] = c(length(motifs[[i]]$Indices), motifs[[i]]$Motif.SAX)
# }
# 
# print (train1_motifs)

read_dataset <- function(i){
  base_path = str_c('../data/dataset', i)
  train_path = str_c(base_path, '/train.txt')
  test_path = str_c(base_path, '/test.txt')
  train = read.table(train_path, sep="", header=FALSE)
  test = read.table(test_path, sep="", header=FALSE)
  dataset <- list(train, test)
  return(dataset)
}

dataset <- read_dataset(1)
train <- dataset[[1]]
test <- dataset[[2]]

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
as.matrix(sapply(test, as.numeric))

train = unlist(train[,])

train <- data.matrix(train)

print (class(train))

wb <- manyseries_to_wordbag(train, w_size = 5, paa_size = 5, a_size = 5, nr_strategy = "mindist", n_threshold = 0.01)


filename = str_c("wb_", 1 , "_train.rds")
print(filename)
saveRDS(wb, filename)