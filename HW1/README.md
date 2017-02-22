**Installation**

Unzip HW1_tekwani.zip
cd/HW1_tekwani
If you want to create a virtual environment, run virtualenv
To begin using the virtual environment, you must activate it. $ source tekwani/bin/activate
Now install the packages specified in requirements.txt. You can do this using pip freeze > requirements.txt (freeze the current state of the environment) pip install -r requirements.txt


**Running the solution**

The folder HW1_tekwani/data must contain all the dataset folders as they are because the code references the data directory.

I've saved the distance matrices as pickle objects.
You can download them here: https://drive.google.com/open?id=0B44mATPcQlDLNV9PRGc2OWVIdlk
Unzip the downloaded folder and copy the 'pickles' folder into HW1_tekwani.
These are loaded in the knn & dtw files as needed and this avoids 
recomputation of large matrices. 


Your directory structure should now look like
    - HW1_tekwani
        - data
            --dataset1
                -train.txt
                -test.txt
            .
            .
            .
            --dataset5
        - pickles
        - src
	- report

       
The file ```knn.py``` is the KNN implementation. 

These lines run KNN on the dataset passed to it. 
You may replace train4_df with any of the other train dataframes (similar naming style).
Also change the other parameters - similarity_matrix and datasetno.
Make sure the similarity matrix you're trying to load exists as a pickle in the pickles folder.
For DTW with warping window, the pickle naming format is dtwn_window.pkl where n is the dataset no.
For vanilla DTW, the naming format is dtwn.pkl, n is the dataset no.

```knn.py``` is loading the pickles, but you'd have to replace the parameters in the code below to run 
the right dataset & distance matrix combination.

````
for k in range(1, 35, 2):
    # last parameter is no of dataset - 1, 2 , 3 , 4 or 5
    nearest_neighbours(train_df=train1_df, similarity_matrix=dtw_1, k=k, datasetno=1)
    # (datasetno, k)
    get_accuracy(dataset_no=1, k=k)
````


``dtw.py`` contains the implementation of the simple DTW algorithm without any warping window. 
``dtw_window.py`` contains an implementation of DTW with a 20% warping window. 

Both these files will have to be passed parameters depending on which dataset is to be used. 

This code is using multiprocessing. Change the arguments below to the numpy arrays ``test1`` through ``test5`` and ``train1`` through ``train 5``. 

```
p = Process(target = run_dtw, args=(test4, train4))

```


``dtw_keogh.py`` contains my implementation of DTW with Lower Bounding  and 1-NN in an attempt to improve the performance of DTW from a processing time standpoint.

``plot_results.py`` generates the plots based on logged performance of the KNN algorithms with DTW and Euclidean distance metrics. 
 
The classification accuracies are also stored in these files: results_dtw.txt, results_dtw_window.txt, results_euclidean.txt.
The PNG images are the graphs illustrating the results. They're presented in the report but the resolution isn't very good. 

The report is in PDF format in the report folder.
