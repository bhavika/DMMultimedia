from scipy.io import loadmat, mmwrite
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix

mnist = loadmat('../data/binaryalphadigs.mat')

nims = mnist['dat'].size
nimsx = 39
nimsy = 36
nx = 16
ny = 20
W = 320


def convert_to_bow(dataset):
    """
    This is a Python port of the convertimstocounts Matlab method
    in the topictoolbox - http://psiexp.ss.uci.edu/research/programs_data/exampleimages2.html
    :param dataset: a dictionary (a mat file read in with scipy)
    :return: w, d, c - lists containing words, docs and counts
    """

    nims = dataset['dat'].size

    nnz = 0
    ii = 0
    w = []
    d = []
    c = []

    # for each character

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

w, d, c = convert_to_bow(mnist)