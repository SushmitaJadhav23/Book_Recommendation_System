import numpy as np
import pandas as pd


# Removing the first row from a dataframe
def remove_n_Row(n, df):
    """
    
    :param n: first n rows to be removed
    :param df: dataframe
    """
    df = df.iloc[n+1:]
    return df



# Create a function to change the data type to "int"
def to_int(x):
    """


    :param x: the column that needs to be operated
    :return: int format of column
    """
    try:
        x = int(x)
    except:
        x = np.nan
    return x

