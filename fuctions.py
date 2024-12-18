import logging
import pandas as pd

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