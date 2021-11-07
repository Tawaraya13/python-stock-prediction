from PySimpleGUI.PySimpleGUI import Print
import numpy as np  
import matplotlib.pyplot as mpl
import pandas as pd
import get as gt
#from sklearn.preprocessing import scale
from TFANN import ANNR

#stock_data = pd.read_csv('output.txt', sep=" ",header=None)

#reads data from the file and ceates a matrix with only the dates and the prices 
#stock_data = np.loadtxt('ZBH_5y.csv', delimiter=",", skiprows=1, usecols=(1, 2))
#scales the data to smaller values
#stock_data=scale(stock_data)
#gets the price and dates from the matrix
#prices = stock_data.get("2. high")
#dates = stock_data.get("date")

#dates = stock_data[:, 0].reshape(-1, 1)
#creates a plot of the data and then displays it
#mpl.plot(dates[:, 0], prices[:, 0])
#mpl.show()

#initialize data



#Number of neurons in the input, output, and hidden layers
input = 1
output = 1
hidden = 50
#array of layers, 3 hidden and 1 output, along with the tanh activation function 
layers = [('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'), ('F', output)]
#construct the model and dictate params
mlpr = ANNR([input], layers, batchSize = 256, maxIter = 20000, tol = 0.2, reg = 1e-4, verbose = True)
data = gt.getStockAlpha('idx')
#number of days for the hold-out period used to access progress


stock_data = pd.read_csv('output.csv' )
#gets the price and dates from the matrix
prices = stock_data.get("2. high")
dates = stock_data.columns[1]
holdDays = 5
totalDays = len(stock_data.index)
#fit the model to the data "Learning"
predictdata = mlpr.fit(dates[0:(totalDays-holdDays)], prices[0:(totalDays-holdDays)])
dataplot = predictdata.get_figure()


# def predict(data):
#     stock_data = pd.read_csv('output.txt', sep=" ",header=None)
#     #gets the price and dates from the matrix
#     prices = stock_data.get("2. high")
#     dates = stock_data.get("date")
#     holdDays = 5
#     totalDays = len(data.date)
#     #fit the model to the data "Learning"
#     predictdata = mlpr.fit(dates[0:(totalDays-holdDays)], prices[0:(totalDays-holdDays)])
#     dataplot = predictdata.get_figure()
#     return dataplot