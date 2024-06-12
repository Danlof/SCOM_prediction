### Safaricom stock price prediction 
- I will be trying a few models in predicting the future stocks prices at safaricom(SCOM) using historical data. ie
    - ARIMA
    - SARIMA

- Timeseries forcasting is divided into two parts : 
    - `Univariate Timeseries forcasting`--> uses only previous values to predict its future values.( this will be our main focus here) 
    - `Multi Variate Time Series Forecasting` --> uses exogenous variables to forcast

#### step :1 Check if the series is stationary
- I will be using the `Augmented Dickey Fuller test(ADF)`  where the null hypothesis of ADF test is that the timeseries is non-stationary.
    - So if the p-value of the test < than the significance level (0.05) we reject the null hypothesis and conclude that the timeseries is indeed stationary.

#### step :2 Difference the model if it is non-stationary 
- See how the autocorrelation plot looks like. we use `plot_acf` for autocorrelation which is useful for :
    - Identifying the order of an MA process
    - Detecting seasonality in a timeseries 
    - Selecting appropriate models for timeseries analysis