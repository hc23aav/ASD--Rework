import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)

def plot_line(data, y_col='Availability'):
    """
    Plot a line chart.

    Parameters:
    - data (pd.DataFrame): The dataset.
    - y_col (str): The column for the y-axis.

    Returns:
    - None
    """
    plt.plot(data[y_col], label=y_col)
    plt.title('Exploring Trends')
    plt.xlabel('Index')
    plt.ylabel(y_col)
    plt.legend()
    plt.show()

def plot_scatter(data, x_col, y_col):
    """
    Plot a scatter plot.

    Parameters:
    - data (pd.DataFrame): The dataset.
    - x_col (str): The column for the x-axis.
    - y_col (str): The column for the y-axis.

    Returns:
    - None
    """
    plt.scatter(data[x_col], data[y_col], label=f'{x_col} vs {y_col}')
    plt.title(f'{x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def plot_histogram(data, column='Stock levels', bins=20):
    """
    Plot a histogram.

    Parameters:
    - data (pd.DataFrame): The dataset.
    - column (str): The column for which the histogram is plotted.
    - bins (int): Number of bins for the histogram.

    Returns:
    - None
    """
    plt.hist(data[column], bins=bins, edgecolor='black', label=column)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def plot_box(data, x_col, y_col):
    """
    Plot a box plot.

    Parameters:
    - data (pd.DataFrame): The dataset.
    - x_col (str): The column for the x-axis.
    - y_col (str): The column for the y-axis.

    Returns:
    - None
    """
    sns.boxplot(x=data[x_col], y=data[y_col])
    plt.title(f'{y_col} by {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def plot_pie(data, column):
    """
    Plot a pie chart.

    Parameters:
    - data (pd.DataFrame): The dataset.
    - column (str): The column for which the pie chart is plotted.

    Returns:
    - None
    """
    data[column].value_counts().plot.pie(autopct='%1.1f%%', label=column)
    plt.title(f'{column}')
    plt.ylabel('')
    plt.show()

def plot_bar(data, column):
    """
    Plot a bar chart.

    Parameters:
    - data (pd.DataFrame): The dataset.
    - column (str): The column for which the bar chart is plotted.

    Returns:
    - None
    """
    data[column].value_counts().plot(kind='bar', label=column)
    plt.title('Client Segmentation')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Load the dataset
file_path = r"C:\Users\heman\OneDrive\Desktop\supply_chain_data.csv"
data = load_data(file_path)

# Plotting examples
plot_line(data)
plot_scatter(data, 'Number of products sold', 'Revenue generated')
plot_histogram(data)
plot_box(data, 'Shipping carriers', 'Shipping costs')
plot_pie(data, 'Customer demographics')
plot_bar(data, 'Supplier name')