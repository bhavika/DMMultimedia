import pandas as pd
from functools import reduce
import logging
from gensim import corpora
from gensim.models import ldamodel

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

flatten = lambda l: [item for sublist in l for item in sublist]


def join_cols(df, cols):
    return reduce(lambda x, y: x.astype(str).str.cat(y.astype(str)), [df[col] for col in cols])


def create_corpus(path, word_length):
    train = pd.read_csv(path, sep=' ')
    cols = train.shape[1]
    no_words = cols / word_length
    mod_val = cols % word_length
    print mod_val

    corp_list = []

    # We combine all columns into one column containing a
    # string that is just all the characters from the SAX representation
    cols = list(train.columns.values)
    train['Doc'] = join_cols(train, cols)

    for index, rows in train.iterrows():
        splitter = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
        words = splitter(rows['Doc'], word_length)
        corp_list.append(words)
    return corp_list


def topic_modeling(datasetno, wordlength = 5):
    corpus_list = create_corpus('../data/train{}.csv'.format(datasetno), word_length=wordlength)
    dictionary = corpora.Dictionary(corpus_list)
    dictionary.save('../models/ts_dict.dict')
    bow = [dictionary.doc2bow(text) for text in corpus_list]
    corpora.MmCorpus.serialize('../models/ts%d_corpus.mm'.format(datasetno), bow)

    lda_20 = ldamodel.LdaModel(corpus=bow, id2word=dictionary, num_topics=20, update_every=1, chunksize=10000, passes=20)
    lda_20.save('../models/ts%d_lda_20.lda'%(datasetno))

    lda_30 = ldamodel.LdaModel(corpus=bow, id2word=dictionary, num_topics=30, update_every=1, chunksize=10000, passes=20)
    lda_30.save('../models/ts%d_lda_30.lda'%(datasetno))

    lda_40 = ldamodel.LdaModel(corpus=bow, id2word=dictionary, num_topics=40, update_every=1, chunksize=10000, passes=20)
    lda_40.save('../models/ts%d_lda_40.lda'%(datasetno))


def display_topics(path, n, datasetno):
    model = ldamodel.LdaModel.load(path)
    topics = model.show_topics(num_topics=n)
    print "Printing topics for time series datasetno", datasetno
    for i in range(len(topics)):
        print topics[i]


# run for any dataset by no between 1 - 5
topic_modeling(datasetno=2)

# test display topics for dataset 1
display_topics('../models/ts1_lda_20.lda', 20, 1)
display_topics('../models/ts1_lda_30.lda', 30, 1)
display_topics('../models/ts1_lda_40.lda', 40, 1)


