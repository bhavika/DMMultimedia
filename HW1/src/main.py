import pandas as pd
import numpy as np
import os


# for root, dirs, files in os.walk("../data/"):
#     for f in files:
#         fullpath = os.path.join(root, f)
#         print fullpath
#         with open(fullpath, 'r+b') as r:
#             with open(fullpath, 'r+b') as w:
#                 for line in r:
#                     line = line.lstrip()
#                     w.write(line)


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



# print train1_df['Label'].unique() #1, 2, 3
# print train2_df['Label'].unique() # 1 to 7
# print train3_df['Label'].unique() # 1 to 6
#print train4_df['Label'].unique() #1 to 15
#print train5_df['Label'].unique() # 1 and -1
