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

    plt.figure(figsize=(10, 6))
    plt.bar(top[col], top["Rating(Out of 10)"], width = 5, color='lightblue')

    plt.xlabel(col)
    plt.ylabel("Rating(Out of 10)")
    plt.title(f"Top {top_n} {col} by Rating (Out of 10)")

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=12) 
    plt.yticks(fontsize=12) 
    plt.tight_layout()

    plt.show()


