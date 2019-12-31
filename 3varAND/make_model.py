import pandas as pd
import numpy as np
from sklearn import datasets, linear_model, metrics 
import pickle

data = pd.read_csv('data.csv')
data = data.values
X = data[:,0:3]
Y = data[:,3]

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=1) 
reg = linear_model.LinearRegression()  
reg.fit(X_train, y_train) 

filename = 'model.sav'
pickle.dump(reg, open(filename, 'wb'))