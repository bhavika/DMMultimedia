import pandas as pd
import numpy as np
import math
from sklearn.metrics import accuracy_score
from scipy.spatial.distance import euclidean
import joblib


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
        upper_bound = max(Q[(index - r if index-r >= 0 else 0) : (index + r)])

        if i > upper_bound:
            lbsum += (i - upper_bound)**2
        elif i < lower_bound:
            lbsum += (i - lower_bound)**2
    return math.sqrt(lbsum)


# P and Q are individual time series - not numpy arrays or dataframes
def dtw(P, Q):

    D = 0;

    # Store all the computations in a numpy array

    dist_np = np.full((len(P), len(Q)), -1)

    # Start visiting every position in the distance matrix

    for i in range(len(P)):
        for j in range(len(Q)):

            # boundary case: the starting position at (0,0)
            if (i == 0) and (j == 0):
                dist_np[i,j] = euclidean(P, Q)

            elif i == 0:
                assert dist_np[i, j - 1] >= 0
                dist_np[i, j] = dist_np[i, j - 1] + euclidean(P, Q)

            elif j == 0:
                assert dist_np[i - 1, j] >= 0
                dist_np[i, j] = dist_np[i - 1, j] + euclidean(P, Q)
            else:
                # general case - paths can start from any of the 3 neighbouring points on the matrix
                # Check that the neighbouring 3 positions have been visited
                assert dist_np[i, j - 1] >= 0
                assert dist_np[i - 1, j] >= 0
                assert dist_np[i - 1, j - 1] >= 0

                # Compare all the distances of the 3 neighbouring points
                lowest_D = min(dist_np[i, j - 1], dist_np[i - 1, j], dist_np[i - 1, j - 1])
                dist_np[i, j] = lowest_D + euclidean(P, Q)

    # the last corner of the matrix is the final distance
    D = dist_np[len(P) - 1, len(Q) - 1]
    return D


def knn_df(train_df, test_df, w, truth_labels):

    y_pred = []
    for idx, k in test_df.iterrows():
        best_so_far = np.inf
        nearest_neighbour = []

        for i, j in train_df.iterrows():
            if LB_Keogh(k, j, w) < best_so_far:
                D = dtw(k, j)
                if D < best_so_far:
                    best_so_far = D
                    nearest_neighbour.append(i)
                    lbl = truth_labels.iloc[i]
                    print "idx", idx, "label", lbl
        y_pred.append(lbl)

    y = pd.DataFrame(y_pred)
    joblib.dump(y, 'keogh_predictions.pkl')


print knn_df(train1_df.ix[:, train1_df.columns != 'Label'], test1_df.ix[:, test1_df.columns != 'Label'], 4 , train1_df['Label'])

