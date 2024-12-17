import pandas as pd
import os

def load_data(file):
    # Determine file extension
    _, ext = os.path.splitext(file.name)
    if ext.lower() in ['.xls', '.xlsx']:
        df = pd.read_excel(file)  # Use read_excel for Excel files
    else:
        # If CSV, attempt reading as CSV
        # If you still get encoding issues, try specifying encoding='latin1' or 'utf-8-sig'
        df = pd.read_csv(file, encoding='latin1')
    return df


def filter_data(df, start_date=None, end_date=None, category_column=None, category_values=None):
    # Example filters on date range and categorical values
    if start_date:
        df = df[df['date'] >= start_date]
    if end_date:
        df = df[df['date'] <= end_date]
    if category_column and category_values:
        df = df[df[category_column].isin(category_values)]
    return df

def get_summary_statistics(df):
    return df.describe()
