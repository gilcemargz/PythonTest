import numpy as np
from sklearn.linear_model import LinearRegression
#import statsmodels.api as sm
import scipy.stats as scp


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

