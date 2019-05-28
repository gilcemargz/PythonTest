import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import scipy as scp
import scipy.stats as scpstats
import matplotlib.pyplot as plt

#Teste com numpy.linalg.lstsq
x = np.array([5,12,25,35,45,55])
y = np.array([5,20,14,32,22,38])
A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A,y)[0]
result = np.linalg.lstsq(A,y)
print(m, c)
print(result)
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()
#Teste com numpy.linalg.lstsq

#Teste com scipy.stats.linregress
x = np.array([5,12,25,35,45,55])
y = np.array([5,20,14,32,22,38])

result = scpstats.linregress(y,x)
print(result)