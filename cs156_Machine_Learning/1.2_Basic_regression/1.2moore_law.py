import numpy as np
import csv
import datetime
import re
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cross_validation import train_test_split

date = []
base_rate = []

benchmark = '130.li' 
relevant_cpu = 'cpu95'

# import data
datafile = open("1.2_CPU_data/benchmarks.txt", "rb")
datareader = csv.reader(datafile, delimiter=',')

# data preperation
for row in datareader:

    if row[1] == benchmark : 
        if row[0][0:5] == relevant_cpu :
            noisy_date = row[0]

            # date cleaning - coverting to epoch
            date_string = re.search('-(.*)-', noisy_date, re.IGNORECASE).group(1)
            
            if date_string[0] == '1' or date_string[0] == '2':
                date_object = datetime.datetime.strptime(date_string, "%Y%m%d").strftime('%s')
                date.append(int(date_object))
            else:
                date_object = datetime.datetime.strptime(date_string, "%y%m%d").strftime('%s')
                date.append(int(date_object))


            base_rate.append(float(row[2]))

## data organization col to row
date = np.array(date).reshape(-1, 1)
base_rate = np.array(base_rate).reshape(-1, 1)

# log the base rate: converting the exponent to potentialyl linear
base_rate = np.log10(base_rate)

# size of the dataset
n_samples =  len(base_rate)


#train and test data 
test_per = .15

(x_moore_train, x_moore_test, y_moore_train, y_moore_test) = train_test_split(date,
    base_rate, test_size=test_per, random_state = 22)

# linear regression object
regr = linear_model.LinearRegression()

# train
regr.fit(x_moore_train, y_moore_train)

# predict
y_moore_pred = regr.predict(x_moore_test)

coeff = regr.coef_[0][0]
mse = mean_squared_error(y_moore_test, y_moore_pred)
r2 = r2_score(y_moore_test, y_moore_pred)
# print 'mse: ', mse
# print 'r^2: ', r2
moores_coef =  10**(coeff*(60*60*24*365))


plt.title('linear regression; Moore\'s law')

plt.scatter(x_moore_test, y_moore_test,  color='lightblue')
plt.plot(x_moore_test, y_moore_pred, color='darkblue', linewidth=2, label='$linear coefficient$ = {} \n$r^2$ = {} \n$MSE$ = {}'.format(round(moores_coef, 4), round(r2, 4), round(mse, 4) ))
plt.xlabel("Time (epoch)")
plt.ylabel("base rate")
plt.legend(loc = 'lower right')
plt.show()


'''
Moore\'s law states an exponential growth in the number of transistors on integrated circuit chips

The above model demonstrates Moore\'s law on a given benchmark, 130.li.

A linear fit with an r^2 = .7 reflect a high fit to the linear model, hence a high fit to the exponential growth.
The model predicts a yearly growth of 1.6. 
'''
