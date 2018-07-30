import numpy as np
import csv
import datetime
import re
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

# knn model function
def knn_model (data, labels, n_samples, test_per = .15):
    # data, labels are the full data set divided to X and Y
    # n_samples dataset size
    # test_per - devision

    n_squared = int(np.floor(n_samples**.5))

    print "spliting data.."
    # split data 
    (x_train, x_test, y_train, y_test) = train_test_split(data,
        labels, test_size=test_per, random_state=42)


    print 'finding best K..'
    ### FINDING BEST K ###

    #one sample cross validate 
    (x_train, x_val, y_train, y_val) = train_test_split(x_train, y_train,
        test_size=test_per, random_state=84)

    # check k between 1 to n^.5
    potential_k_values = range(1, n_squared)

    accuracy_array = []

    # iterating on Ks 
    for potential_k in potential_k_values:
        knn_val_model = KNeighborsClassifier(n_neighbors = potential_k)
        knn_val_model.fit(x_train, y_train)

        #Returns the mean accuracy on the given test data and labels.
        accuracy = knn_val_model.score(x_val, y_val)
        accuracy_array.append(accuracy)


    # find best K
    max_accuray_k_index = np.argmax(accuracy_array)
    max_accuracy = accuracy_array[max_accuray_k_index]
    max_accuray_k = max_accuray_k_index + 1

    print 'best k is {} with accuracy {}'.format(max_accuray_k, max_accuracy)
    
    print 'training model with k = {}..'.format(max_accuray_k)

    #train the model with the relevant k
    knn_train_model = KNeighborsClassifier(n_neighbors = max_accuray_k)
    knn_train_model.fit(x_train, y_train)

    knn_pred = knn_train_model.predict(x_test)
    print 'Model accuracy :'
    # a reoport of accuracy on the test set
    return classification_report(y_test, knn_pred)


if __name__ == "__main__":
    ## load data
    digits = load_digits()

    ## print example 
    plt.gray() 
    plt.matshow(digits.images[4]) 
    plt.show() 

    # full data set length 
    n_samples, _ = digits.data.shape
    n_squared = np.floor(n_samples**.5)

    # data preperation
    partial_data = []
    partial_labels = []

    # exctract 9 and 7.
    for i in range(n_samples):
        if digits.target[i] == 9 or digits.target[i] == 7 :
            partial_data.append(digits.data[i])
            partial_labels.append(digits.target[i])

    # MNIST 9 and 7
    print knn_model(partial_data, partial_labels, len(partial_data))

    # MNIST full
    print knn_model(digits.data, digits.target, n_samples)
