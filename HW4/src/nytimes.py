import logging
from gensim.corpora.ucicorpus import UciCorpus
from gensim.corpora import MmCorpus
from gensim.models import ldamodel

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

corpus = UciCorpus('../data/docword.nytimes.txt', '../data/vocab.nytimes.txt')
MmCorpus.serialize('../models/corpus.mm', corpus)

#save the dictionary

dictionary = corpus.create_dictionary()
dictionary.save('../models/dict.dict')

lda_20 = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20, update_every=1, chunksize=10000, passes=1)
lda_20.save('../models/lda_20.lda')

lda_30 = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=30, update_every=1, chunksize=10000, passes=1)
lda_30.save('../models/lda_30.lda')

lda_40 = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=40, update_every=1, chunksize=10000, passes=1)
lda_40.save('../models/lda_40.lda')

# Visualize NYTimes topics
lda_20 = ldamodel.LdaModel.load('../models/lda_20.lda')
lda_30 = ldamodel.LdaModel.load('../models/lda_30.lda')
lda_40 = ldamodel.LdaModel.load('../models/lda_40.lda')


def display_topics(model, n):
    topics = model.show_topics(num_topics=n)
    for i in range(len(topics)):
        print topics[i]


display_topics(lda_20, 20)
display_topics(lda_30, 30)
display_topics(lda_40, 40)
