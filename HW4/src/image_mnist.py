from scipy.io import loadmat, mmwrite
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix
import logging
from gensim.corpora import BleiCorpus, LowCorpus, MalletCorpus
from gensim.corpora import MmCorpus
from gensim.models import ldamodel
from gensim.matutils import Dense2Corpus
import gensim


mnist = loadmat('../data/binaryalphadigs.mat')
mnist_all = loadmat('../data/mnist_all.mat')

# print (mnist2)
# print (type((mnist2)))

# print type(mnist2['dat'][1])
# # 36 * 39 = 1404

nims = mnist['dat'].size
nimsx = 39
nimsy = 36
nx = 16
ny = 20
W = 320

# print (mnist['dat'][0].size)


def convert_to_bow(dataset):
    nims = dataset['dat'].size
    # x = (dataset['dat'].reshape(nims, 1))

    nnz = 0

    ii = 0
    w = []
    d = []
    c = []


    #for each character
    for i in range(36):
        # each handwritten style
        for j in range(39):
            temp = dataset['dat'][i][j]
            temp_flat = temp.flatten()
            wh = np.nonzero(temp_flat)

            # intensities at pixels
            intensities = []
            for x in np.nditer(wh[0]):
                intensities.append(temp_flat[x])
            nz = np.count_nonzero(temp)

            w[ii:ii+nz] = wh[0]

            d[ii:ii+nz] = [i * j] * (nz)
            c[ii:ii+nz] = intensities

            ii += nz
            nnz += nz

    return w, d, c

    # print dataset['dat'][0][2][0]
    #print np.count_nonzero(x.flat[41][1])


w, d, c = convert_to_bow(mnist)


# print type(w)
# print d
# print type(c)

# print len(w)
# print len(d)
# print len(c)
# #
# m = csc_matrix(w, [d, c])
# # m.eliminate_zeros()
# print m.shape
# print m

# mmwrite('../data/mnist.mtx', m)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#
# corpus = UciCorpus('../data/mnist_docword.mtx', '../data/mnist_docword.mtx.vocab')
# MmCorpus.serialize('../data/mnist.mtx', corpus)
#
# # save the dictionary
# dictionary = corpus.create_dictionary()
# dictionary.save('../models/mnist_dict.dict')
#
# lda_20 = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, update_every=1, chunksize=10000, passes=50)
# lda_20.save('../models/mnist_lda_20.lda')


# lda_20_topics = lda_20.show_topics(num_topics=20, num_words=20, log=True)

# with open('../data/mnist_docword.mtx.vocab', 'w') as f:
#     for i in range(320):
#         f.write(str(i) + "\n")

mnist_list = []
# for i in range(10):
#     mnist_list.append(mnist_all['test'+str(i)])

for i in range(10):
    mnist_list.append(mnist_all['train'+str(i)])

print len(mnist_list)

corpus = Dense2Corpus(mnist_list[1])

LowCorpus.serialize('/tmp/corpus.low', corpus)

# dictionary = corpus.create_dictionary()

lda_20 = ldamodel.LdaModel(corpus=corpus, num_topics=20, update_every=1, chunksize=10000, passes=50)
lda_20.save('../models/mnist_lda_20.lda')
lda_20_topics = lda_20.show_topics(num_topics=20, num_words=20, log=True)