### Safaricom stock price prediction 
- I will be trying a few models in predicting the future stocks prices at safaricom(SCOM) using historical data. 
- Timeseries forecasting is divided into two parts : 
    - `Univariate Timeseries forcasting`--> uses only previous values to predict its future values.( this will be our main focus here) 
    - `Multi Variate Time Series Forecasting` --> uses exogenous variables to forecast

#### step :1 Check if the series is stationary
- I will be using the `Augmented Dickey Fuller test(ADF)`  where the null hypothesis of ADF test is that the timeseries is non-stationary.
    - So if the p-value of the test < than the significance level (0.05) we reject the null hypothesis and conclude that the timeseries is indeed stationary.

#### step :2 Difference the model if it is non-stationary 
- use `diff_close = np.diff(df['close'], n=2)` to difference twice;
- Then plot the autocorrelation plot. we use `plot_acf` for autocorrelation function plot.

#### step :3 solution from the ACF plot
- There is no significant coefficients from the plot. By chance only at lag 1 and 3 are significant but the others are not.
- Hence we can conclude that the closing price of SCOM can be approximated by a random walk process.

#### step :4 forecasting a random walk