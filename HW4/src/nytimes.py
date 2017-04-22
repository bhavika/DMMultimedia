import logging
from gensim.corpora.ucicorpus import UciCorpus
from gensim.corpora import MmCorpus
from gensim.models import ldamodel

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

corpus = UciCorpus('../data/docword.nytimes.txt', '../data/vocab.nytimes.txt')
MmCorpus.serialize('../models/corpus.mm', corpus)

# save the dictionary
dictionary = corpus.create_dictionary()
dictionary.save('../models/dict.dict')

lda_20 = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20, update_every=1, chunksize=10000, passes=1)
lda_20.save('../models/lda_20.lda')

lda_10 = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, update_every=1, chunksize=10000, passes=1)
lda_10.save('../models/lda_10.lda')

lda_5 = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, update_every=1, chunksize=10000, passes=1)
lda_5.save('../models/lda_5.lda')


lda_20_topics = lda_20.show_topics(num_topics=20, num_words=20, log=True)
lda_10_topics = lda_10.show_topics(num_topics=10, num_words=20, log=True)
lda_5_topics = lda_5.show_topics(num_topics=5, num_words=20, log=True)
