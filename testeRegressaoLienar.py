import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import scipy as scp
import matplotlib.pyplot as plt

#https://www.freecodecamp.org/news/data-science-with-python-8-ways-to-do-linear-regression-and-measure-their-speed-b5577d75f8b/

#Teste com statsmodels.ols
X = [5,12,25,35,45,55]
y = [5,20,14,32,22,38]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()

# Inspect the results
print(results.summary())

#Teste com statsmodels.ols


exit()
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

exit()

#Teste com scipy.optimize.curve_fit
def func(x,a,b,c):
    return a * np.exp(-b * x) + c

x = np.array([5,12,25,35,45,55])
y = np.array([5,20,14,32,22,38])

result = scp.optimize.curve_fit(func,x,y )
print(result)
#Teste com scipy.optimize.curve_fit


#Teste com scipy.stats.linregress
x = np.array([5,12,25,35,45,55])
y = np.array([5,20,14,32,22,38])

result = scp.linregress(y,x)
print(result)

#Teste com scipy.stats.linregress



exit()
#Teste com numpy.polyfit
x = np.array([5,12,25,35,45,55])
y = np.array([5,20,14,32,22,38])

result = np.polyfit(y,x,1)
print(result)
#Teste com numpy.polyfit




#regresãao com sklearn
x = np.array([5,12,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

print(x)
print(y)

model = LinearRegression()

resultado = model.fit(x,y)

r_sq = model.score(x,y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

x = [5,12,25,35,45,55]
y = [5,20,14,32,22,38]

t1 = scp.linregress(y,x)
print(t1)

#Regresssão com statsmodels
"""
x = [5,12,25,35,45,55]
y = [5,20,14,32,22,38]
#sm.add_constant(x)
modelNov = sm.OLS(x,y).fit()
print(modelNov.summary())
"""

