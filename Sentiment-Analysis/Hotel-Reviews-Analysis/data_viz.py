import pandas as pd
import matplotlib.pyplot as plt

def bar_chart(df, col, top_n = 10):
    '''
    Create a bar chart to visualize top values of a specific column by average value

    Args:
        df (pd.DataFrame): dataframe
        col (str): the column to visualize
        top_n (int): the number of top values to display (default is 10).
    '''
    char_bar = df.groupby([col])[['Name', 'Rating(Out of 10)']].mean().reset_index()
    char_bar = char_bar.sort_values(by=("Rating(Out of 10)"), ascending = False)

    # Select the top values
    top = char_bar.head(top_n)

    plt.figure(figsize=(12, 8))
    plt.barh(top[col], top["Rating(Out of 10)"], color='lightblue')

    plt.xlabel(col)
    plt.ylabel("Rating(Out of 10)")
    plt.title(f"Top {top_n} {col} by Rating (Out of 10)")

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.xticks() 
    plt.yticks()
    plt.tight_layout()

    plt.show()


