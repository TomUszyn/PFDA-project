import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np




# Configure the logger to include timestamps
logging.basicConfig(level=logging.INFO, filename="warnings.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Log warnings with timestamps
def logWarning(message, category, filename, lineno, file=None, line=None):
    """
    Custom warning handler that logs warnings to a file with a timestamp.

    Parameters:
    - message (str): The warning message.
    - category (Warning): The class of the warning (e.g., UserWarning, DeprecationWarning).
    - filename (str): The name of the source file where the warning was triggered.
    - lineno (int): The line number where the warning was triggered.
    - file (file-like object, optional): The file where the warning is being triggered (usually None).
    - line (str, optional): The line of code where the warning was triggered (usually None).
    
    The function logs the warning message along with its category, filename, and line number to a log file.
    """
    logging.info(f'{filename}:{lineno}: {category.__name__}: {message}') 

# Set filter to log warnings
#warnings.showwarning = logWarning




# Function to flatten multi-index columns into single-level columns and rename 'Date' to 'Datetime' to match the other datasets
def flattenColumns(df):
    """ Flatten multi-index columns into single-level columns """
    if 'Date' in df.columns:
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
    
    # Flatten multi-index columns to single level
    df.columns = ['Datetime' if isinstance(col, tuple) and col[0] == 'Datetime' 
                  else '_'.join(col).strip() for col in df.columns]




# Function to normalize the data using z-score normalization    
def plotClosePrices(df, title='Close Prices'):
    """
    Function to plot 'Close' prices for a given DataFrame.
    
    Parameters:
    - df: DataFrame to plot.
    - title: Title for the plot (default is 'Close Prices').
    """
    # Ensure the index is in datetime format
    df.index = pd.to_datetime(df.index, errors='coerce')

    # Filter columns that contain '_Close'
    columnsToPlot = [col for col in df.columns if '_Close' in col]
    
    # Determine the appropriate datetime format based on the data
    datetime_format = '%Y-%m-%d'
    if any(df.index.minute):  # If there are non-zero minutes, include time
        datetime_format = '%Y-%m-%d %H:%M'

    # Plot the selected columns
    plt.figure(figsize=(12, 6))
    for column in columnsToPlot:
        plt.plot(df.index, df[column], label=column)
    
    # Customize plot appearance
    plt.xlabel('Datetime', fontsize=12, fontweight='bold')
    plt.ylabel('Normalised Close Price', fontsize=12, fontweight='bold')

    # Set the title passed in the parameter
    plt.title(title, fontsize=14, fontweight='bold', pad=20)

    plt.xticks(rotation=45, fontsize=10)
    # Format x-axis dynamically based on the data
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(datetime_format))
    
    plt.grid(True)

    # Customize the legend as you requested
    plt.legend(loc='upper left', bbox_to_anchor=(1.003, 1), title='Currency Pairs',     
               frameon=False, fancybox=True, shadow=True, fontsize=8, 
               title_fontproperties=font_manager.FontProperties(weight='bold', size=11), labelspacing=1.5)
    
    # Show plot
    plt.tight_layout()
    plt.show()

# Example usage
# plotClosePrices(normalisedZscore2y, title='Historical Close Prices for Currencies')




def descriptiveStatisticsWithSource(df, columns, analysisType):
    """
    Calculate descriptive statistics for specified columns in a DataFrame and include the source of the data.

    Parameters:
    - df: DataFrame to analyze.
    - columns: List of column names to calculate statistics for.
    - analysisType: String indicating the source of the data.

    Returns:
    - A DataFrame with descriptive statistics, including the source column.
    """
    results = []
    for column in columns:
        if column in df.columns:
            # Collect statistics
            stats = {
                'column': column,
                'source': analysisType,  # Add source information
                'description': (
                    "Exchange rate of USD to EUR" if "USDEUR" in column else
                    "Exchange rate of GBP to EUR" if "GBPEUR" in column else
                    "Exchange rate of BTC to EUR" if "BTC-EUR" in column else
                    f"Statistics for {column}"
                ),
                'median': df[column].median(),
                'mean': df[column].mean(),
                'standardDeviation': df[column].std(),
                'range': df[column].max() - df[column].min()
            }
            results.append(stats)
        else:
            print(f"Column '{column}' not found in the DataFrame.")

    # Create a DataFrame for the results
    return pd.DataFrame(results)
# Example usage
# descriptiveStatisticsWithSource(normalisedZscore2y, ['USDEUR_Close', 'GBPEUR_Close', 'BTC-EUR_Close'], 'Exchange Rates')




# Function to plot a correlation matrix heatmap for specific columns in a DataFrame
def plotCorrelationMatrix(df, columns, title='Correlation Matrix'):
    """
    Function to plot a correlation matrix heatmap for specific columns in a DataFrame.
    
    Parameters:
    - df: DataFrame containing the data.
    - columns: List of column names to calculate the correlation matrix.
    - title: Title for the heatmap (default: 'Correlation Matrix').
    """
    # Compute correlation matrix for the specified columns
    correlation_matrix = df[columns].corr()

    # Plot the heatmap
    plt.figure(figsize=(8, 6))  # Adjust size for better visibility
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, linewidths=0.5)
    
    # Set the title for the plot
    plt.title(title)
    plt.show()

# Example usage
# plotCorrelationMatrix(normalisedZscore2y, ['USDEUR_Close', 'GBPEUR_Close', 'BTC-EUR_Close'], title='Correlation Matrix of Exchange Rates')





# Function to plot the distribution of the specified columns in a DataFrame
def plotOriginalAndRollingAverages(df, columns, windowSizes=[7, 30], title='Original vs Rolling Averages'):
    """
    Function to plot the original 'Close' prices and rolling averages for specified columns.
    
    Parameters:
    - df: DataFrame containing the data.
    - columns: List of column names to plot the rolling averages.
    - window_sizes: List of window sizes for rolling averages to compare (default: [7, 30]).
    - title: Title for the plot (default: 'Original vs Rolling Averages').
    """
    # Plot the original 'Close' prices
    plt.figure(figsize=(20, 8))
    
    # Loop through each column to plot the original and rolling averages
    for column in columns:
        # Plot the original values
        plt.plot(df.index, df[column], label=f'{column} Original', alpha=0.7)
        
        # Loop through the different window sizes to plot rolling averages
        for window in windowSizes:
            rollAvg = df[column].rolling(window=window).mean()
            plt.plot(df.index, rollAvg, label=f'{column} {window}-Day Rolling', linestyle='--', linewidth=2)
    
    # Customize plot appearance
    plt.xlabel('Datetime')
    plt.ylabel('Close Price')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    
    # Customize the legend as per your request
    plt.legend(loc='upper left', bbox_to_anchor=(1.003, 1), title='Currency Pairs',     
               frameon=False, fancybox=True, shadow=True, fontsize=8, 
               title_fontproperties=plt.matplotlib.font_manager.FontProperties(weight='bold', size=11), labelspacing=1.5)
    
    # Display the plot
    plt.tight_layout()
    plt.show()

# Example usage for a DataFrame with 'Close' prices and a range of window sizes
# plotOriginalAndRollingAverages(normalisedZscore2y, 
#                                columns=['USDEUR=X_Close', 'GBPEUR=X_Close', 'BTC-EUR_Close'], 
#                                windowSizes=[30],  # Single window size, can be [7], [30], or any custom list
#                                title='Original vs Rolling Averages for Exchange Rates')





# Function to plot the distribution of the specified columns in a DataFrame
def decomposeTimeSeries(df, column, period=12, title='Time-Series Decomposition'):
    """
    Function to decompose time series into trend, seasonality, and residuals for a specified column.
    
    Parameters:
    - df: DataFrame containing the data.
    - column: Name of the column to decompose.
    - period: Periodicity of the seasonality (e.g., 12 for monthly data in a year).
    - title: Title for the plot (default is 'Time-Series Decomposition').
    """
    # Decompose the time series for the column
    decomposition = sm.tsa.seasonal_decompose(df[column], model='additive', period=period)
    
    # Plot the decomposition components
    plt.figure(figsize=(14, 10))
    
    plt.subplot(411)
    plt.plot(df.index, df[column], label=f'{column} Original', color='blue')
    plt.title(f'{column} - Original')
    
    plt.subplot(412)
    plt.plot(df.index, decomposition.trend, label='Trend', color='orange')
    plt.title(f'{column} - Trend')
    
    plt.subplot(413)
    plt.plot(df.index, decomposition.seasonal, label='Seasonality', color='green')
    plt.title(f'{column} - Seasonal')
    
    plt.subplot(414)
    plt.plot(df.index, decomposition.resid, label='Residuals', color='red')
    plt.title(f'{column} - Residuals')
    
    plt.tight_layout()
    plt.suptitle(f'{title} for {column}', fontsize=16, y=1.05)
    plt.show()

# Example usage for a single currency pair, e.g., 'USDEUR=X_Close'
# decomposeTimeSeries(normalisedZscore2y, 
#                     column='USDEUR=X_Close', 
#                     period=365,  # Use 365 for yearly seasonality
#                     title='Time-Series Decomposition')




# Function to plot the distribution of the specified columns in a DataFrame
def plotVolatility(volatility, title):
    fig, ax = plt.subplots(figsize=(12, 6))
    volatility.plot(kind='bar', ax=ax, width=0.8)
    
    # Format the x-axis to show only 'yyyy-mm-dd'
    ax.set_xticklabels(volatility.index.strftime('%Y-%m-%d'), rotation=45)
    plt.title(f'{title} Volatility (Normalized Data)')
    plt.ylabel('Standard Deviation (Normalized)')
    plt.xlabel('Time')
    # Customize the legend as per your request
    plt.legend(loc='upper left', bbox_to_anchor=(1.003, 1), title='Currency',     
               frameon=False, fancybox=True, shadow=True, fontsize=8, 
               title_fontproperties=plt.matplotlib.font_manager.FontProperties(weight='bold', size=11), labelspacing=1.5)
    
    #plt.legend(title='Currency')
    plt.tight_layout()
    plt.show()
    
# Example usage
# plotVolatility(monthlyVolatility, title='Monthly')




# Function to plot forecasted close prices using a simple linear regression model
def forecastClosePrices(dataFrame, forecastColumn, forecastDays=30):
    """
    Forecast future close prices using a simple linear regression model
    and plot both historical data and the regression line for all data.

    Parameters:
    - dataFrame: pandas.DataFrame
        The input data with historical prices. The index should be datetime.
    - forecastColumn: str
        The column name containing the close prices to forecast.
    - forecastDays: int, optional (default=30)
        The number of future days to forecast.
    """
    # Convert the index to datetime if it's not already
    dataFrame.index = pd.to_datetime(dataFrame.index)

    # Create a simple integer column 'daysSinceStart' representing the number of days since the start
    dataFrame['daysSinceStart'] = (dataFrame.index - dataFrame.index.min()).days

    # Prepare the data for the linear regression model
    xValues = dataFrame[['daysSinceStart']]  # Features (daysSinceStart)
    yValues = dataFrame[forecastColumn]  # Target (close prices)

    # Initialize and train the linear regression model
    regressionModel = LinearRegression()
    regressionModel.fit(xValues, yValues)

    # Forecast future days (next forecastDays)
    lastDay = dataFrame['daysSinceStart'].max()  # Last day in the dataset
    futureDays = np.array([lastDay + i for i in range(1, forecastDays + 1)]).reshape(-1, 1)
    forecastValues = regressionModel.predict(futureDays)

    # Generate forecasted dates
    forecastDates = pd.date_range(dataFrame.index[-1] + pd.Timedelta(days=1), periods=forecastDays, freq='D')

    # Create the regression line for only historical data
    historicalPredictions = regressionModel.predict(xValues)

    # Plot the historical data, regression line, and forecasted data
    plt.plot(dataFrame.index, dataFrame[forecastColumn], label='Historical Data', color='blue')
    plt.plot(dataFrame.index, historicalPredictions, label='Regression Line (Historical Data)', color='green', linestyle='--')
    plt.plot(forecastDates, forecastValues, label='Forecasted Data', color='red', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'{forecastColumn} Forecast with Regression Line')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
# Example usage
# forecastClosePrices(normalisedZscore2y, forecastColumn='USDEUR=X_Close', forecastDays=30)
