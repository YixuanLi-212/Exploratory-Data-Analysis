import pandas as pd
import colorama
from colorama import Fore, Style

def remove_duplicates(df):
    duplicated_rows = df[df.duplicated()]
    if not duplicated_rows.empty:
        num_duplicates = len(duplicated_rows)
        print(f"Found {num_duplicates} duplicated row(s). Removing them...")
        df = df.drop_duplicates()
        print(f"{num_duplicates} duplicated row(s) removed.")
    else:
        print("No duplicated rows found. No changes were made.")
    return df

def data_report(df, verbose=False):
    report = {}
  
    df = remove_duplicates(df)

    # Get the raw dataset info
    report['Raw Dataframe Info'] = {
        'Row_num of the dataset': df.shape[0],
        'Col_num of the dataset': df.shape[1],
        'Size of the dataset': df.size
    }

    # Dataframe Info
    info = df.info()
    report['Dataframe Info'] = info

    # Null Data
    null_data = df.isna().sum()
    report['Null Data'] = null_data

    # Number of Unique Values
    unique_values = df.nunique()
    report['Number of Unique Values'] = unique_values

    # Fill null values in 'Rating(Out of 10)' column with 0
    df['Rating(Out of 10)'].fillna(0, inplace=True)

    # Filter rows with non-numeric values in 'Rating(Out of 10)' column
    df = df[pd.to_numeric(df['Rating(Out of 10)'], errors='coerce').notna()]

    # Convert 'Rating(Out of 10)' column to numeric
    df['Rating(Out of 10)'] = pd.to_numeric(df['Rating(Out of 10)'], errors='coerce')

    # Data features
    report['Data Features'] = df.describe(include='all')

    # Ratings Info
    ratings_info = df['Rating(Out of 10)'].value_counts()
    report['Ratings Info'] = ratings_info
    report['Highest Rating'] = df['Rating(Out of 10)'].max()
    report['Lowest Rating'] = df['Rating(Out of 10)'].min()
    report['Overall Average Rating'] = df['Rating(Out of 10)'].mean()
    report['Hotel Average Ratings'] = df.groupby('Name')['Rating(Out of 10)'].mean().reset_index()

    # Calculate average rating by 'Area'
    report['Area Average Ratings'] = df.groupby('Area')['Rating(Out of 10)'].mean().reset_index()

    # Print the report
    print('-' * 20 + f'{Fore.RED}DATAFRAME INFO{Style.RESET_ALL}' + '-' * 20)
    for section, data in report.items():
        print(f'{Fore.BLUE}##{section}##{Style.RESET_ALL}')
        if isinstance(data, pd.DataFrame):
            print(data)
        elif isinstance(data, pd.Series):
            print(data.to_string())
        elif isinstance(data, dict):
            for key, value in data.items():
                print(f"{key}: {value}")

