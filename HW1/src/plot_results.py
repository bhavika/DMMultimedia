import matplotlib.pyplot as plt
import seaborn as sns

## -------------------------- Dynamic Time Warping - Vanilla ------------------###########

k_1 = list(range(1, 27, 2))

dtw_acc_1 = [1.0, 0.998888888889, 0.985555555556, 0.985555555556,0.98, 0.98, 0.974444444444, 0.974444444444,
             0.824444444444, 0.925555555556, 0.708888888889, 0.526666666667,0.424444444444]

k_4 = list(range(1, 35, 2))

dtw_acc_4 = [0.9888, 0.9856, 0.9776, 0.9744, 0.9648, 0.9648, 0.9648, 0.9536, 0.952, 0.9488, 0.9392, 0.9328
        ,0.9248 ,0.9248 ,0.912, 0.9088 , 0.9024]

plt.figure(1)
plt.suptitle("KNN with Dynamic Time Warping")
plt.subplot(211)
plt.plot(k_1, dtw_acc_1, '-')
plt.title("Dataset 1")
plt.xlabel("k")
plt.ylabel("Accuracy")

plt.subplot(212)
plt.plot(k_4, dtw_acc_4, '-')
plt.title("DataSet 4")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.show()


fig = plt.figure()
fig.savefig('knn_dtw_1.png', dpi=400)

#### ----------------- Euclidean Distance ----------------------_######

euc_1 = list(range(1, 29, 2))
euc_acc_1 = [0.8522222222, 0.8377777778, 0.7733333333, 0.72, 0.7388888889, 0.6733333333, 0.6511111111, 0.6422222222,
             0.6422222222, 0.6233333333, 0.5044444444, 0.5033333333, 0.5122222222,0.4788888889 ]


euc_2 = list(range(1, 35, 2))
euc_acc_2 = [0.782857142857, 0.754285714286, 0.72, 0.68, 0.702857142857, 0.691428571429, 0.674285714286,
            0.662857142857, 0.68, 0.668571428571, 0.628571428571, 0.634285714286, 0.588571428571,
            0.594285714286, 0.56, 0.542857142857, 0.548571428571]

euc_3 = list(range(1, 35, 2))
euc_acc_3 = [0.51652892562, 0.504132231405, 0.46694214876, 0.46694214876, 0.429752066116,
            0.45041322314, 0.429752066116,  0.417355371901, 0.396694214876, 0.392561983471,
             0.413223140496, 0.392561983471, 0.384297520661, 0.396694214876, 0.380165289256,
             0.384297520661, 0.367768595041]


euc_4 = list(range(1, 35, 2))
euc_acc_4 = [0.7888, 0.7184, 0.7184, 0.7008, 0.6864, 0.6688, 0.6544,
            0.6448, 0.6288, 0.6016, 0.5968, 0.5808, 0.5648, 0.56,
             0.544, 0.5376, 0.5296]

euc_5 = list(range(1, 77, 2))
euc_acc_5 = [0.995457495133,
0.993835171966,
0.991726151849,
0.988968202466,
0.987345879299,
0.985885788449,
0.983939000649,
0.983290071382,
0.982803374432,
0.982154445165,
0.982154445165,
0.981343283582,
0.982316677482,
0.982316677482,
0.982965606749,
0.981667748215,
0.981829980532,
0.980856586632,
0.978747566515,
0.968202465931,
0.957819597664,
0.951979234263,
0.95165476963,
0.950843608047,
0.950843608047,
0.951492537313,
0.951330304997,
0.950843608047,
0.950843608047,
0.95068137573,
0.95019467878,
0.949545749513,
0.94873458793,
0.948572355613,
0.948410123297,
0.94873458793,
0.948896820247,
0.94873458793]


sns.set_style("darkgrid")

plt.figure(figsize=(7,7))
plt.subplot(211)
plt.suptitle("KNN with Euclidean Distance")
plt.plot(euc_1, euc_acc_1, '-')
plt.title("Dataset 1")
plt.xlabel("k")
plt.ylabel("Accuracy")

plt.subplot(212)
plt.suptitle("KNN with Euclidean Distance")
plt.plot(euc_2, euc_acc_2, '-')
plt.title("DataSet 2")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.show()

fig = plt.figure()
fig.savefig('knn_euc_1.png', dpi=400)


plt.subplot(211)
plt.suptitle("KNN with Euclidean Distance")
plt.plot(euc_3, euc_acc_3, '-')
plt.title("DataSet 3")
plt.xlabel("k")
plt.ylabel("Accuracy")

plt.subplot(212)
plt.plot(euc_4, euc_acc_4, '-')
plt.title("DataSet 4")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.show()

fig = plt.figure()
fig.savefig('knn_euc_2.png', dpi=400)

plt.subplot(111)
plt.suptitle("KNN with Euclidean Distance")
plt.plot(euc_5, euc_acc_5, '-')
plt.title("DataSet 5")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.show()


fig = plt.figure()
fig.savefig('knn_euc_3.png', dpi=400)

###-----------------Dynamic Time Warping with Window ---------------################3

dtw_win_1 = list(range(1, 27, 2))
dtw_win_accuracy_1 = [0.312222222222, 0.312222222222, 0.29, 0.308888888889 , 0.327777777778, 0.384444444444,
                      0.42666666666, 0.405555555556, 0.431111111111, 0.427777777778, 0.444444444444,
                      0.456666666667, 0.41]

dtw_win_4 = list(range(1, 35, 2))
dtw_win_accuracy_4 = [0.0864, 0.0832, 0.096, 0.0816, 0.0784,
                    0.0752, 0.0688,0.0816, 0.072, 0.0656, 0.0704, 0.0752, 0.0864,
                    0.0832, 0.0816, 0.0864, 0.0832]

plt.suptitle("KNN with Dynamic Time Warping - Window")
plt.figure(1)
plt.subplot(211)
plt.plot(dtw_win_1, dtw_win_accuracy_1, '-')
plt.title("Dataset 1")
plt.xlabel("k")
plt.ylabel("Accuracy")

plt.subplot(212)
plt.plot(dtw_win_4, dtw_win_accuracy_4, '-')
plt.title("DataSet 4")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.show()

fig = plt.figure()
fig.savefig('knn_dtww_1.png', dpi=400)

