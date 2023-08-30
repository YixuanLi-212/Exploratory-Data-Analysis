import pandas as pd
import numpy as np
import colorama
from colorama import Fore, Style


def data_report(df, verbose=False):
    # Get the raw dataset info
    print('-'*20+f'{Fore.RED}RAW DATAFRAME INFO{Style.RESET_ALL}'+'-'*20)
    print(f'Row_num of the dataset: {df.shape[0]}',"|",f'Col_num of the dataset: {df.shape[1]}')
    print(f'Size of the dataset: {df.size}')
    print(f'Num of duplicates: {str(df.duplicated().sum())}')
    print('## Dataframe Info ##')
    print(df.info())
    print('## Null Data ##')
    print(df.isna().sum())
    print('## Number of Unique Values ##')
    print(df.nunique())

    # Data features
    print('-'*20+f'{Fore.BLUE}DATA FEATURES{Style.RESET_ALL}'+'-'*20)
    print(df.describe(include='all'))
    print('## Ratings Info ##')
    print(df['Rating(Out of 10)'].value_counts())

    
    



