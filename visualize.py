import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data=pd.read_csv('data.csv')
print(data.head())

plot=plt.figure().gca(projection='3d')
plot.scatter(data['canny'],data['fft'],data['result'])
plot.set_xlabel('Canny')
plot.set_ylabel('FFT')
plot.set_zlabel('Result')
plt.show()