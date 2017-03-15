library(jmotif)
data("CBF")

print (CBF)

# set the discretization parameters
#
w <- 60 # the sliding window size
p <- 6  # the PAA size
a <- 6  # the SAX alphabet size

# convert the train classes to wordbags (the dataset has three labels: 1, 2, 3)
#
cylinder <- manyseries_to_wordbag(CBF[["data_train"]][CBF[["labels_train"]] == 1,], w, p, a, "exact", 0.01)
bell <- manyseries_to_wordbag(CBF[["data_train"]][CBF[["labels_train"]] == 2,], w, p, a, "exact", 0.01)
funnel <- manyseries_to_wordbag(CBF[["data_train"]][CBF[["labels_train"]] == 3,], w, p, a, "exact", 0.01)

# compute tf*idf weights for three bags
#
tfidf = bags_to_tfidf( list("cylinder" = cylinder, "bell" = bell, "funnel" = funnel) )

print (class(cylinder))

print(cylinder)

print (class(bell))

print(class(tfidf))