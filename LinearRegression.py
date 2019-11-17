#Linear Regression example
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets
oof=datasets.load_diabetes()
xTrain=oof.data[:-20]
yTrain=oof.target[:-20]
xTest=oof.data[:-20]
yTest=oof.target[:-20]

x0Test=xTest[:,0]
x0Train=xTrain[:,0]
x0Test= x0Test[:,np.newaxis]
x0Train= x0Train[:,np.newaxis]
linreg=linear_model.LinearRegression()
linreg.fit(x0Train, yTrain)
y=linreg.predict(x0Test)
plt.scatter(x0Test,yTest,color='k')
print(plt.plot(x0Test,y,color='b',linewidth=3))
