import pandas as pd
import numpy as np
import joblib
from scipy.spatial.distance import euclidean
from sklearn.metrics import accuracy_score


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



# print train1_df['Label'].unique() #1, 2, 3
# print train2_df['Label'].unique() # 1 to 7
# print train3_df['Label'].unique() # 1 to 6
#print train4_df['Label'].unique() #1 to 15
#print train5_df['Label'].unique() # 1 and -1


# Works directly with DataFrames
def similarity_matrix_euclidean(train_df, test_df):
    train = train_df.ix[:, 1:]
    test = test_df.ix[:, 1:]

    test_array = np.array(test)
    train_array = np.array(train)

    m, n = test_array.shape
    a, b = train_array.shape

    print m, n
    print a, b

    similarity_matrix = np.zeros((m, a))

    for i in range(len(test_array)):
        for j in range(len(train_array)):
            similarity_matrix[i][j] = euclidean(test_array[i], train_array[j])
    sim_df = pd.DataFrame(similarity_matrix)
    return sim_df

# sim1_df = similarity_matrix_euclidean(train1_df, test1_df)
# sim2_df = similarity_matrix_euclidean(train2_df, test2_df)
# sim3_df = similarity_matrix_euclidean(train3_df, test3_df)
# sim4_df = similarity_matrix_euclidean(train4_df, test4_df)
# sim5_df = similarity_matrix_euclidean(train5_df, test5_df)
#
# joblib.dump(sim1_df, '../pickles/sim1.pkl')
# joblib.dump(sim2_df, '../pickles/sim2.pkl')
# joblib.dump(sim3_df, '../pickles/sim3.pkl')
# joblib.dump(sim4_df, '../pickles/sim4.pkl')
# joblib.dump(sim5_df, '../pickles/sim5.pkl')

#
# sim1 = joblib.load('../pickles/sim1.pkl')
# sim2 = joblib.load('../pickles/sim2.pkl')
# sim3 = joblib.load('../pickles/sim3.pkl')
# sim4 = joblib.load('../pickles/sim4.pkl')
# sim5 = joblib.load('../pickles/sim5.pkl')

sim_dtw_1 = joblib.load('../pickles/dtw4.pkl')

sim_dtw_df = pd.DataFrame(sim_dtw_1)


def get_review(train_df, train_case):
    return train_df.iloc[train_case].Label


def nearest_neighbours(train_df, similarity_matrix, k, datasetno):
    neighbours = pd.DataFrame(similarity_matrix.apply(lambda s: s.nsmallest(k).index.tolist(), axis=1))
    neighbours = neighbours.rename(columns={0: 'nbr_list'})
    neighbours['test_case_id'] = neighbours.index.values

    # getting the scores of each train neighbour from the train dataframe
    nbr_scores = []

    # creating a list of lists containing the sentiment scores for each set of train neighbours
    # [0, 1, 2, 3, 4] -> [1, 1, 1, 1, 1] from train data set

    test_scores_ref = []

    for i in range(neighbours.shape[0]):  # row
        for j in range(len(neighbours['nbr_list'].iloc[i])):  # element
            a = neighbours['nbr_list'].iloc[i][j]
            nbr_scores.append(get_review(train_df, int(a)))

    test_scores_ref = [nbr_scores[i:i + k] for i in range(0, len(nbr_scores), k)]
    test_scores_series = pd.DataFrame(test_scores_ref)

    test_scores_series.columns = [str(col) + '_x' for col in test_scores_series.columns]

    choices = list(train_df['Label'].unique())
    choices.sort()
    test_scores_series['Answer'] = test_scores_series.apply(lambda y: y.value_counts().idxmax(), axis=1)
    write_submission_file(test_scores_series, k, datasetno)


def write_submission_file(test_scores_series, k, datasetno):
    test_scores_series.to_csv(str.format('submission_{}_{}.txt', datasetno, k), sep='\n', mode='a', columns=['Answer'],
                              header=False, index=False)


def get_accuracy(dataset_no, k):
    datasets = [test1_df, test2_df, test3_df, test4_df, test5_df]
    y_true = datasets[dataset_no-1]['Label']
    y_pred = pd.read_csv(str.format('submission_{}_{}.txt', dataset_no, k), header=None)
    print "Dataset no", dataset_no
    print k,",", accuracy_score(y_true, y_pred)


for k in range(1, 35, 2):
    nearest_neighbours(train4_df, sim_dtw_df, k, 4)
    get_accuracy(4, k)

