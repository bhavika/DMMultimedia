import joblib
import pandas as pd
import numpy as np
import math
from time import time
import subprocess

subprocess.call(['speech-dispatcher'])


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


def local_distance(p_i, q_j):
    return math.sqrt(pow(p_i - q_j, 2))


# w is the warping window expressed as an integer
def dtw(P, Q, w):

    D = 0;

    w = max(w, abs(len(P) - len(Q)))

    # Store all the computations in a list of lists

    dist_np = np.full((len(P), len(Q)), -1)

    # Start visiting every position in the distance matrix

    for i in range(len(P)):
        for j in range(max(1, i-w), min(len(Q), i+w)):

            # boundary case: the starting position at (0,0)
            lowest_D = local_distance(P[i-1], Q[j-1])
            dist_np[i, j] = lowest_D + min(dist_np[i-1, j], dist_np[i, j-1], dist_np[i-1, j-1])

    # the last corner of the matrix is the final distance
    D = dist_np[len(P) - 1, len(Q) - 1]
    return D


distance_matrix = np.zeros((6164, 1000))
m, n = test5.shape

w = math.ceil(0.2 * n)

start = time()

for i in range(len(test5)):
    for j in range(len(train5)):
        distance_matrix[i, j] = dtw(test5[i], train5[j], int(w))

print "Elapsed time: ", time() - start

joblib.dump(distance_matrix, 'dtw5_window.pkl')

p = joblib.load('dtw5_window.pkl')
print p

subprocess.call(['spd-say', '"Process finished."'])


training = [train1, train2, train3, train4, train5]
test = [test1, test2, test3, test4, test5]
warp_window = []

for i in range(len(training)):
    m, n = training[i].shape
    w = math.ceil(0.2 * n)
    warp_window.append(w)


print warp_window