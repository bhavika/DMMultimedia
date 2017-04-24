from scipy.io import loadmat, mmwrite
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix
import logging
from gensim.corpora import BleiCorpus, LowCorpus, MalletCorpus
from gensim.corpora import MmCorpus
from gensim.models import ldamodel
from gensim.matutils import Dense2Corpus
import gensim


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

mnist_all = loadmat('../data/mnist_all.mat')

mnist_list = []
# for i in range(10):
#     mnist_list.append(mnist_all['test'+str(i)])

for i in range(10):
    mnist_list.append(mnist_all['test'+str(i)])

corpus = Dense2Corpus(mnist_list[1])

LowCorpus.serialize('/tmp/corpus.low', corpus)

lda_50 = ldamodel.LdaModel(corpus=corpus, num_topics=50, update_every=1, chunksize=10000, passes=50)
lda_50.save('../models/mnist_lda_50.lda')
lda_50_topics = lda_50.show_topics(num_topics=50, num_words=20, log=True)

lda_100 = ldamodel.LdaModel(corpus=corpus, num_topics=100, update_every=1, chunksize=10000, passes=50)
lda_100.save('../models/mnist_lda_100.lda')
lda_100_topics = lda_50.show_topics(num_topics=100, num_words=50, log=True)

lda_20 = ldamodel.LdaModel(corpus=corpus, num_topics=20, update_every=1, chunksize=10000, passes=50)
lda_20.save('../models/mnist_lda_20.lda')
lda_20_topics = lda_20.show_topics(num_topics=20, num_words=10, log=True)

