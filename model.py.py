# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QEqw06um2ez4ujb-4mZ5z2cMuTABECBf

#End To End Machine Learning Model Project Implementaion with Dockers ,Github actions And Deployment

Import dependencies
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""##Lets load the Boston House Price Dataset

https://www.kaggle.com/datasets/fedesoriano/the-boston-houseprice-data url
"""

# import the function to load the Boston housing dataset
#  creating the dataframe with loaded csv file
# convertin the csv file into dataframe using pandas library
df=pd.read_csv('boston.csv')

# print the first 5 rows of the dataset
df.head()

# checking the shape of the dataset
df.shape
print("the number of rows in the dataset : ",df.shape[0])
print("the number of columns in the dataset : ",df.shape[1])

# creating a copy of dataset
df1=df.copy()
# df1.head()

# lets change the target name on the dataset into Price

df.columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT', 'Price']

# lets check the name of the target or price column
df.head()

# Getting the total information about the dataset
df.info()

"""obsevation : In the above information of the dataset it says that the dataset has the 14 columns ,506 rows.the dataset has all columns are the same datatype  as 12 (float) and 2(int) datatypes .the total memory required for the dataset is 55.5 kb."""

# checking the missing values in the dataset
df.isnull().sum()

"""obsevation : the dataset have no missng values so we can proceed our next process."""

# summarizing the stats of the dataset
df.describe()

"""obsevation: The statistics of the dataset is given on above ,it says the statistics about the dataset of only numeric columns in the dataset.it gives the entire statistics informaion about the data like pecentile ,min,max, counts of the columns data with standard deviavtion ,mean ,median,and max values of data.

Exploratory Data Analysis
"""

# correlation
df.corr()

"""## Correlation

In this we have check the two types of correlation

1.correlation between  independent variables(multi colliniarity)

2.correlation between  independent and dependent variables

Obsevation : The main part of the Exploratory Data Analysis is that the correlation between the indpendent and dependent variables.

1.Positve Correlation : In this, the relation between two variables are highly positve .positive correlation is defined as the if variable of x increrase the other variable of y also increase.

2.Negitive Correlation : It is defined as ,if the relation between two variables is negitve.if the variable of x is increases the other y variable is decreases.

3.Zero Correlation : It is defined as,if the realtion between two variables is near to zero.if the variable of x is increases the other variable has no change in their data.

whenever we are doing an Regression Problem we must check the correlation and the colliniarity of the varibles.

if the correlation between the independent and dependent varible is good we have to place them in dataset.

If the correlation between the two variables is not good in the dataset either it will be independemnt or dependent variables we have to remove variables from the dataset. so our model will predict with good accuracy.

If the colliniarity between two independent variable is high we have two remove the any one variable from the dataset.it will use for good accuracy prediction.
"""

# we can check the correlation by using the seaborn ,using pairplot it gives the scatterplots betweeen variables

import seaborn as sns
sns.pairplot(df)

"""Obsevation : The above graph of pairplot is says the correlation between the independent and dependent variables.
based on above plots we may not anlayse the  data detaily so we can use seperatly the scatterplots for better understandig the correlation between the varialbles.
"""

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),annot=True)

plt.scatter(df['CRIM'],df['Price'])
plt.xlabel('CRIM')
plt.ylabel('Price')

"""Obsevation : the correlation betwenn CRIM and Price is negitive correaltion."""

plt.scatter(df['RM'],df['Price'])
plt.xlabel('RM')
plt.ylabel('Price')

"""Obsevation : In this the correlation between the RM and Price is positive .it's says that the correlation is high."""

# we can use regressionplot for the correlation

import seaborn as sns
sns.regplot(x='RM',y='Price',data=df)

"""Obsevation : so we create a regression plot using regplot. in the above ploting we can create a simple linear regresion line between the points.that says it has the positve correlation between the two variables."""

# regression plot between Price and LSTAT
sns.regplot(x='LSTAT',y='Price',data=df)

"""Obsevation : the graph says that the correlation between LSTAT and Price the data is highly negitive ."""

# lets plot some other graph that having the zero correlation
sns.regplot(x='CHAS',y='Price',data=df)

"""Obsevation : the above Graph is having the less or zero correlation betwen the CHAS and Price variables features.

##Creating the dependent and Independent features
"""

x=df.iloc[:,:-1] #independent variable features
y=df.iloc[:,-1] # dependent variable feature

x # independent features

y # it is our dependent feature column of Price

"""##Spliting the dataset Train And Test split"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

# print the test data
x_test

# print the train data
x_train

# print the shapes  of the data x_train and x_test
print("the shape of the x_train data : ",x_train.shape)
print("the shape of the x_test data : ",x_test.shape)

"""##standardization

Before creating the model we have to do the standardscaler or standardization.

1.what is standardization?

it is defined as the scaling the data. the data is having different types of variables and different types of scales . so here we can convert the data into some range by using the standardscaler. so whenever we are using the standardscaler the internal process is happing Z scores formula will apply to the dataset.


1.why we need to do standardization?

The reason the standardization is the variable features having the different types of numeric values so we can convert the values into some particular range by using the standardization that the model will understand and perform the prediction with good accuracy.


Obsevation : In linear regression we use the gradient decent, so our main aim is to reach the gllobal minima and to come to global minima make sure that all our independent features units should in the same  scale beacuse of that the convergence will happen.
"""

# standardize the dataset
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)

x_test=scaler.transform(x_test)

# print the x_train the after doing the standardization
x_train

# print the x_test the after doing the standardization
x_test

"""Obsevation : The transformation of the data is sucessfuylly completed

#Model Training

importing the linear regression model
"""

from sklearn.linear_model import LinearRegression

# create the model
regression=LinearRegression()

# fit the modle with train data
regression.fit(x_train,y_train)

"""Obsevation : The model has been created ,fit and trained with train data sucessfully"""

# print the coefficents and the intercept
print(regression.coef_)

# print the intercept
print(regression.intercept_)

# we will know the model on which parameters the model has been trained
regression.get_params()

# prediction with test data on model
reg_pred=regression.predict(x_test)

reg_pred

"""Obsevation : the model has predicted the x_test data sucessfully now we can compare the predicton values with the actual data.

##Assumptions
"""

# ploting the scatter plot for the prediction
plt.scatter(y_test,reg_pred)

"""Obsetvation : the above graph is says that the ploting is linear that means that the data is of prediction by the model is done with good accuracy."""

# Residuals
residuals=y_test-reg_pred

residuals # residuals means the error

# ploting the residuals

sns.displot(residuals,kind='kde')

"""Observation : the graph says this is a normal distribution curve but also having the outliers at data .but the most of the data is aligned in the range between -10 to 10

"""

# scatter plot with respect to prediction and residuals
plt.scatter(reg_pred,residuals)

"""Observation : the data is uniformly disributed based on the above graph.so our data is evenly distributed in the plot.

##PERFORMANCE METRICS
"""

# importing the dependencies

from sklearn.metrics import mean_absolute_error,mean_squared_error

print("the mean absloute error is : ",mean_absolute_error(y_test,reg_pred))
print("the mean squared error is : ",mean_squared_error(y_test,reg_pred))
print(np.sqrt(mean_squared_error(y_test,reg_pred)))

"""R square and Adjusted R square"""

# lets import the metrics
from sklearn.metrics import r2_score
score=r2_score(y_test,reg_pred)
print(score)

"""Observation : the R square value is 71% so that our machine is a  good model.now we can find the adjusted R square value but for the adjusted R square value has no libraray to find the metrics so we can use math intition for finding the metrics or accuracuy of adjusted R square value. one more point is that the adjusted R square value is always less than the R square value.

R square value = 1-SSR/SST

Adjusted R square value = 1-[(1-r2)*(n-1)/(n-k-1)]
"""

# adjusted R square value
1-(1-score)*(len(y_test)-1)/(len(y_test)-x_test.shape[1]-1)

"""Observation : the R2 values is greater than the adjusted R2 value.

##Pickiing the model file for the deployment
"""

# picking the modle
import pickle

pickle.dump(regression,open('regmodel.pkl','wb'))

# creating the pickle model and loading
pickle_model=pickle.load(open('regmodel.pkl','rb'))

# predicting the data
pickle_model.predict(x_test[0].reshape(1,-1))

































