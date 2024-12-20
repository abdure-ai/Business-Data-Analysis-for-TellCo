import pandas as pd
import numpy as np

def handle_missing_values(df):
    """
    Handles missing values in the DataFrame.
    Numeric columns: Replace with mean.
    Categorical columns: Replace with mode.
    """
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mode()[0])
    return df

def handle_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()

def handle_outliers(df, num_cols):
    """
    Handles outliers in the numeric columns using the IQR method.
    Replaces outliers with the nearest bound value.
    """
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.where(df[col] < lower_bound, lower_bound,
                           np.where(df[col] > upper_bound, upper_bound, df[col]))
    return df

def convert_data_types(df):
    """
    Converts data types where possible.
    Numeric data stored as objects are converted to proper numeric types.
    """
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                pass  # Keep as object if conversion fails
    return df

def clean_column_names(df):
    """
    Cleans column names by:
    - Stripping whitespace
    - Converting to lowercase
    - Replacing spaces with underscores
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def clean_dataframe(df):
    """
    Orchestrates the cleaning process by calling individual functions.
    """
    # Identify numeric columns
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Apply cleaning steps
    df = handle_missing_values(df)
    df = handle_duplicates(df)
    df = handle_outliers(df, num_cols)
    df = convert_data_types(df)
    df = clean_column_names(df)
    
    return df
