import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(20.0,10.0)
#Reading File
data=pd.read_csv('slr06.csv')


print(data.shape)
print(data.head())
X=data["X"].values
Y=data['Y'].values
#Mean X and Y
mean_x=np.mean(X)
mean_y=np.mean(Y)
print('Mean x:%f Mean Y:%f'%(mean_x,mean_y))

#Total Number of values
n=len(X)
print('Count',n)

#To Calculate m and c
numer=0
denom=0
for i in range(n):
    numer+=(X[i]-mean_x)*(Y[i]-mean_y)
    denom+=(X[i]-mean_x)**2
m=numer/denom
c=mean_y-(m*mean_x)

#Pirnt coefficients
print("m = %f, c = %f"%(m,c))
print("y = %fx + %f"%(m,c))

#Plotting values and Regression line
max_x=np.max(X)+100
min_x=np.min(X)-100
print("min(X):%f"%min_x)
print("max(X):%f"%max_x)
#max_x=10
#min_x=1000
#Calculating Line values x and y
x=np.linspace(min_x,max_x,50)#inespace(starting_value,EndingValue,No of values between Start and End)
y=(m*x)+c
print("Y_value:")
print(y)

#plotting Line
plt.plot(x,y,color='red',label='RegressionLine')
#plotting scatter values
plt.scatter(X,Y,c='blue',label='Scatter Plot')

plt.xlabel('number of claims')
plt.ylabel(' total payment of claims')
#plt.legend()
plt.show()


