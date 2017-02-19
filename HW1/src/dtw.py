import joblib
import pandas as pd
import numpy as np
import math
from time import time


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


# Let P and Q be the two time series

def print_distance_matrix(d):
    for i in range(len(d)):
        for j in range(len(d[i])):
            print d[i][j],
        print


def local_distance(p_i, q_j):
    return math.sqrt(pow(p_i - q_j, 2))


def dtw(P, Q):

    D = 0;

    # Store all the computations in a list of lists

    dist_np = np.full((len(P), len(Q)), -1)

    # Start visiting every position in the distance matrix

    for i in range(len(P)):
        for j in range(len(Q)):

            # boundary case: the starting position at (0,0)
            if (i == 0) and (j == 0):
                dist_np[i,j] = local_distance(P[i], Q[j])

            elif i == 0:
                assert dist_np[i, j - 1] >= 0
                dist_np[i, j] = dist_np[i, j - 1] + local_distance(P[i], Q[j])

            elif j == 0:
                assert dist_np[i - 1, j] >= 0
                dist_np[i, j] = dist_np[i - 1, j] + local_distance(P[i], Q[j])
            else:
                # general case - paths can start from any of the 3 neighbouring points on the matrix
                # Check that the neighbouring 3 positions have been visited
                assert dist_np[i, j - 1] >= 0
                assert dist_np[i - 1, j] >= 0
                assert dist_np[i - 1, j - 1] >= 0

                # Compare all the distances of the 3 neighbouring points
                lowest_D = min(dist_np[i, j - 1], dist_np[i - 1, j], dist_np[i - 1, j - 1])
                dist_np[i, j] = lowest_D + local_distance(P[i], Q[j])

    # the last corner of the matrix is the final distance
    D = dist_np[len(P) - 1, len(Q) - 1]
    return D


distance_matrix = np.zeros((242, 200))

start = time()

for i in range(len(test3)):
    for j in range(len(train3)):
        distance_matrix[i, j] = dtw(test3[i], train3[j])

print "Elapsed time: ", time() - start

joblib.dump(distance_matrix, 'dtw3.pkl')

p = joblib.load('dtw3.pkl')
print p
print type(p)

