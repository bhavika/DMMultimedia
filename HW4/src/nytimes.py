import pandas
from gensim.corpora.ucicorpus import UciReader, UciCorpus
import numpy as np
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.corpora import dictionary

vocab = np.genfromtxt('../data/vocab.nytimes.txt', dtype=str)
lemma = WordNetLemmatizer()

corpus = UciReader('../data/docword.nytimes.txt.gz')


# print corpus
def clean(vocab):
    normalized = [lemma.lemmatize(word) for word in vocab]
    return normalized


normal_vocab = clean(vocab)

# print normal_vocab

# doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]
#
# print doc_term_matrix