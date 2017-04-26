from scipy.io import loadmat, mmwrite
import numpy as np
import logging
from sklearn.decomposition import LatentDirichletAllocation as lda
import pickle
import matplotlib.pyplot as plt

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

mnist = loadmat('../data/mnist_all.mat')

mnist_list = []

for i in range(10):
    mnist_list.append(mnist['test'+str(i)])
    #mnist_list.append(mnist_all['train'+str(i)])

mnist_list = np.vstack(mnist_list)

lda_10 = lda(n_topics=10, learning_method='batch', max_iter=10, n_jobs=3)
lda_20 = lda(n_topics=20, learning_method='batch', max_iter=50, n_jobs=3)
lda_50 = lda(n_topics=50, learning_method='batch', max_iter=50, n_jobs=3)

models = {'lda_10': lda_10, 'lda_20':lda_20, 'lda_50':lda_50}

# Store the model's output in a dictionary
models_out = {}


def topic_models(models):
    for k, v in models.iteritems():
        print models[k]
        models_out[k] = models[k].fit(mnist_list)


def save_topickle(path, model_results):
    with open(path, 'wb') as out:
        pickle.dump(model_results, out, protocol=pickle.HIGHEST_PROTOCOL)


def create_plots(model, words, n_iter):
    for topic_idx, topic in enumerate(model.components_):

        # Initialize a list with the original number of pixels
        pix = [0] * 784
        pixel_id = []
        for i in topic.argsort()[:-words-1:-1]:
            pixel_id.append(i)

        # paint it black
        for p in pixel_id:
            pix[p] = 255

        pix = np.array(pix).reshape(28, 28)
        plt.title('Topic %d, Iteration %d' % (topic_idx, n_iter))
        plt.imshow(pix, cmap='gray')
        plt.savefig('../models/Top%d-Iter%d' % (topic_idx, n_iter))


topic_models(models)
save_topickle('../models/mnist_lda.pickle', models_out)

with open('../models/mnist_lda.pickle', 'rb') as f:
    r = pickle.load(f)
    for k, v in r.iteritems():
        create_plots(v, 50, v.max_iter)