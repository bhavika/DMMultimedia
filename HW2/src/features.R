train1_motifs <- readRDS('DS2motifs_train.rds')

motifs = train1_motifs$motifs
# 
# print(motifs[[1]]$Indices[1])

train1_motifs = c()

for (i in 1:length(motifs)){
  train1_motifs[[i]] = c(length(motifs[[i]]$Indices), motifs[[i]]$Motif.SAX)
}

