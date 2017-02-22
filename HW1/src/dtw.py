import joblib
import pandas as pd
import numpy as np
import math
from time import time
from scipy.spatial.distance import euclidean
from multiprocessing import Process

print "Loading the data"

#load into numpy arrays
train1 = np.genfromtxt(fname='../data/dataset1/train.txt')
train2 = np.genfromtxt(fname= '../data/dataset2/train.txt')
train3 = np.genfromtxt(fname='../data/dataset3/train.txt')
train4 = np.genfromtxt(fname='../data/dataset4/train.txt')
train5 = np.genfromtxt(fname='../data/dataset5/train.txt')

test1 = np.genfromtxt(fname='../data/dataset1/test.txt')
test2 = np.genfromtxt(fname='../data/dataset2/test.txt')
test3 = np.genfromtxt(fname='../data/dataset3/test.txt')
test4 = np.genfromtxt(fname='../data/dataset4/test.txt')
test5 = np.genfromtxt(fname='../data/dataset5/test.txt')

train1_df = pd.DataFrame(train1)
train2_df = pd.DataFrame(train2)
train3_df = pd.DataFrame(train3)
train4_df = pd.DataFrame(train4)
train5_df = pd.DataFrame(train5)

train1_df = train1_df.rename(columns={0: 'Label'})
train2_df = train2_df.rename(columns={0: 'Label'})
train3_df = train3_df.rename(columns={0: 'Label'})
train4_df = train4_df.rename(columns={0: 'Label'})
train5_df = train5_df.rename(columns={0: 'Label'})

test1_df = pd.DataFrame(test1)
test2_df = pd.DataFrame(test2)
test3_df = pd.DataFrame(test3)
test4_df = pd.DataFrame(test4)
test5_df = pd.DataFrame(test5)

test1_df = test1_df.rename(columns={0: 'Label'})
test2_df = test2_df.rename(columns={0: 'Label'})
test3_df = test3_df.rename(columns={0: 'Label'})
test4_df = test4_df.rename(columns={0: 'Label'})
test5_df = test5_df.rename(columns={0: 'Label'})


def LB_Keogh(P, Q, r=0):
    lbsum = 0

    for index, i in enumerate(P):
        lower_bound = min(Q[(index - r if index-r >= 0 else 0): (index + r)])
        upper_bound = max(Q[(index - r if index-r >= 0 else 0) : (index +r)])

        if i > upper_bound:
            lbsum += (i - upper_bound)**2
        elif i < lower_bound:
            lbsum += (i - lower_bound)**2
    return math.sqrt(lbsum)


# Let P and Q be the two time series

def print_distance_matrix(d):
    for i in range(len(d)):
        for j in range(len(d[i])):
            print d[i][j],
        print


def dtw(P, Q):

    D = 0;

    # Store all the computations in a list of lists

    dist_np = np.full((len(P), len(Q)), -1)

    # Start visiting every position in the distance matrix

    for i in range(len(P)):
        for j in range(len(Q)):

            # boundary case: the starting position at (0,0)
            if (i == 0) and (j == 0):
                dist_np[i,j] = euclidean(P[i], Q[j])

            elif i == 0:
                assert dist_np[i, j - 1] >= 0
                dist_np[i, j] = dist_np[i, j - 1] + euclidean(P[i], Q[j])

            elif j == 0:
                assert dist_np[i - 1, j] >= 0
                dist_np[i, j] = dist_np[i - 1, j] + euclidean(P[i], Q[j])
            else:
                # general case - paths can start from any of the 3 neighbouring points on the matrix
                # Check that the neighbouring 3 positions have been visited
                assert dist_np[i, j - 1] >= 0
                assert dist_np[i - 1, j] >= 0
                assert dist_np[i - 1, j - 1] >= 0

                # Compare all the distances of the 3 neighbouring points
                lowest_D = min(dist_np[i, j - 1], dist_np[i - 1, j], dist_np[i - 1, j - 1])
                dist_np[i, j] = lowest_D + euclidean(P[i], Q[j])

    # the last corner of the matrix is the final distance
    D = dist_np[len(P) - 1, len(Q) - 1]
    return D


def run_dtw(test, train):
    train_r, train_c = train.shape
    test_r, test_c = test.shape

    print "Creating a matrix of size", str(test_r) + "*" + str(train_r)
    distance_matrix = np.zeros((test_r, train_r))

    start = time()

    print "Starting DTW calculations"

    for i in range(len(test)):
        for j in range(len(train)):
            distance_matrix[i, j] = dtw(test[i], train[j])

    print "Elapsed time: ", time() - start

    distance_matrix_df = pd.DataFrame(distance_matrix)

    print distance_matrix_df
    joblib.dump(distance_matrix_df, 'dtw4.pkl')

    p = joblib.load('dtw4.pkl')
    print p


if __name__ == '__main__':
    p = Process(target = run_dtw, args=(test4, train4))
    p.start()
    p.join()