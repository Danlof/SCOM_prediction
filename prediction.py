import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller
from numpy import log

from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from sklearn.metrics import mean_squared_error

# load the data 
df = pd.read_csv("/media/danlof/dan_files/data_science_codes/Timeseries/arima/HistoricalPrices.csv")
df.head()

# preprocessing 
df.columns = df.columns.str.strip().str.lower()

# keep the last 5 days for testing 
SCOM_train = df[['date','close']][:-5]
SCOM_test = df[['date','close']][-5:]
print(SCOM_test)

# prediction methods for a random walk
# method 1: using mean
mean = np.mean(SCOM_train['close'])
SCOM_test.loc[:,'pred_mean'] = mean
mean

# method 2 : last known value 
last_value = SCOM_train['close'].iloc[-1]
SCOM_test.loc[:,'pred_last'] = last_value
last_value

# method3 : using drift
deltaX = len(SCOM_train)
deltaY = last_value - SCOM_train['close'][0]# Remember to subtract the initial value of the training set

drift = deltaY / deltaX
x_values = np.arange(3998,4003,1)

pred_drift = drift*x_values + SCOM_train['close'].iloc[0]
SCOM_test.loc[:,'pred_drift'] = pred_drift
SCOM_test

# performance check
SCOM_mse_mean = mean_squared_error(SCOM_test['close'], SCOM_test['pred_mean'])
SCOM_mse_last = mean_squared_error(SCOM_test['close'], SCOM_test['pred_last'])
SCOM_mse_drift = mean_squared_error(SCOM_test['close'], SCOM_test['pred_drift'])
print(SCOM_mse_mean,SCOM_mse_last,SCOM_mse_drift)

# plot the above predictions 
fig ,ax = plt.subplots()

ax.plot(SCOM_train['close'],'b-')
ax.plot(SCOM_test['close'],'b-')
ax.plot(SCOM_test['pred_mean'],'r-.',label='Mean')
ax.plot(SCOM_test['pred_last'],'g--',label='Last value')
ax.plot(SCOM_test['pred_drift'],'k:',label='Drift')

ax.axvspan(3998,4002,color='#808080',alpha=0.2)
ax.legend(loc=2)
ax.set_xlabel('Timesteps')
ax.set_ylabel('Value')

plt.xlim(3980,4002)
plt.tight_layout()

# forecast the next timestep
df_shift = df.shift(periods=1)
mse_one_step = mean_squared_error(SCOM_test['close'],df_shift['close'].iloc[3998:])

print("This is mse for one step:",mse_one_step)

# plot next steps over the test set and compare its mse

fig, ax = plt.subplots()
ax.plot(df['close'],'b-',label='actual')
ax.plot(df_shift['close'].iloc[3998:],'r-',label='forecast')

ax.axvspan(3998,4002,color='#808080', alpha=0.2)
ax.legend(loc='best')
ax.set_xlabel('Timesteps')
ax.set_ylabel('Value')

plt.xlim(3990,4002)
plt.ylim(5,30)
plt.tight_layout()
