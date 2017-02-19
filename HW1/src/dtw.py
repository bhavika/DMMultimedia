import joblib
import pandas as pd
import numpy as np
import math
from time import time

#load into numpy arrays
train1 = np.genfromtxt(fname='../data/dataset1/train.txt')
test1 = np.genfromtxt(fname='../data/dataset1/test.txt')

train1_df = pd.DataFrame(train1)
test1_df = pd.DataFrame(test1)
test1_df = test1_df.rename(columns={0: 'Label'})


# Let P and Q be the two time series

def print_distance_matrix(d):
    for i in range(len(d)):
        for j in range(len(d[i])):
            print d[i][j],
        print


def local_distance(p_i, q_j):
    return math.sqrt(pow(p_i - q_j, 2))


def dtw(P, Q):
    # the distance to be calculated

    D = 0;

    # Store all the computations in a list of lists
    distance_matrix = []
    for i in range(len(P)):
        row = []
        for j in range(len(Q)):
            row.append(-1)
        distance_matrix.append(row)

        # Start visiting every position in the distance matrix

    for i in range(len(P)):
        for j in range(len(Q)):

            # boundary case: the starting position at (0,0)
            if (i == 0) and (j == 0):
                distance_matrix[i][j] = local_distance(P[i], Q[j])

            elif (i == 0):
                assert distance_matrix[i][j - 1] >= 0
                distance_matrix[i][j] = distance_matrix[i][j - 1] + local_distance(P[i], Q[j])

            elif (j == 0):
                assert distance_matrix[i - 1][j] >= 0

                distance_matrix[i][j] = distance_matrix[i - 1][j] + local_distance(P[i], Q[j])
            else:

                # general case - paths can start from any of the 3 neighbouring points on the matrix

                # Check that the neighbouring 3 positions have been visited

                assert distance_matrix[i][j - 1] >= 0
                assert distance_matrix[i - 1][j] >= 0
                assert distance_matrix[i - 1][j - 1] >= 0

                # Compare all the distances of the 3 neighbouring points
                lowest_D = min(distance_matrix[i][j - 1], distance_matrix[i - 1][j], distance_matrix[i - 1][j - 1])
                print lowest_D
                distance_matrix[i][j] = lowest_D + local_distance(P[i], Q[j])

    # the last corner of the matrix is the final distance
    D = distance_matrix[len(P) - 1][len(Q) - 1]
    return D


distance_matrix = np.zeros((900, 30))

start = time()

for i in range(len(test1)):
    for j in range(len(train1)):
        distance_matrix[i][j] = dtw(test1[i], train1[j])

print "Elapsed time: ", time() - start

joblib.dump(distance_matrix, 'dtw1.pkl')

p = joblib.load('dtw1.pkl')
print p
print type(p)