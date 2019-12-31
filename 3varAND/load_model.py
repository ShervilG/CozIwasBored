import pandas as pd
import numpy as np
from sklearn import * 
import pickle

model = pickle.load(open('model.sav', 'rb'))
while True:
	print("Enter values of X,Y and Z : ")
	x = int(input())
	y = int(input())
	z = int(input())
	ar = np.array([x,y,z]).reshape(1,-1)
	print(model.predict(ar))