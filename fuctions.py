import logging
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager


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



