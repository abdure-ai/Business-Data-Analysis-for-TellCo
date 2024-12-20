import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column, bins=20, xlabel=None, ylabel='Frequency', title=None):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=bins, color='skyblue', edgecolor='black')
    plt.xlabel(xlabel if xlabel else column)
    plt.ylabel(ylabel)
    plt.title(title if title else f'Histogram of {column}')
    plt.show()

def plot_boxplot(data, column, xlabel=None, ylabel='Value', title=None):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[column], color='lightgreen')
    plt.xlabel(xlabel if xlabel else column)
    plt.ylabel(ylabel)
    plt.title(title if title else f'Boxplot of {column}')
    plt.show()

def plot_correlation_heatmap(data, corr_columns, annot=True, cmap='coolwarm', title=None):
    corr_data = data[corr_columns].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_data, annot=annot, cmap=cmap, fmt='.2f', linewidths=0.5)
    plt.title(title if title else 'Correlation Heatmap')
    plt.show()

def plot_scatter(data, x_column, y_column, xlabel=None, ylabel=None, title=None):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[x_column], y=data[y_column], color='purple')
    plt.xlabel(xlabel if xlabel else x_column)
    plt.ylabel(ylabel if ylabel else y_column)
    plt.title(title if title else f'Scatter Plot: {x_column} vs {y_column}')
    plt.show()

def plot_pairplot(data, columns, hue=None, title=None):
    sns.pairplot(data[columns], hue=hue)
    plt.suptitle(title if title else 'Pairplot', y=1.02)
    plt.show()

# Univariate Analysis (Single Variable)
def univariate_analysis(data, column):
    """
    Function to plot univariate analysis (histogram, boxplot, and descriptive statistics) for a single column.
    """
    # Plot Histogram
    plot_histogram(data, column)

    # Plot Boxplot
    plot_boxplot(data, column)

    # Print Descriptive Statistics
    print(f'Descriptive Statistics for {column}:')
    print(data[column].describe())

# Bivariate Analysis (Two Variables)
def bivariate_analysis(data, x_column, y_column):
    """
    Function to perform bivariate analysis and plot scatter plot and correlation for two variables.
    """
    # Scatter Plot
    plot_scatter(data, x_column, y_column)

    # Correlation
    correlation = data[[x_column, y_column]].corr()
    print(f'Correlation between {x_column} and {y_column}:')
    print(correlation)

# Multivariate Analysis (Multiple Variables)
def multivariate_analysis(data, columns):
    """
    Function to perform multivariate analysis and plot pairplot and correlation heatmap for multiple variables.
    """
    # Pairplot
    plot_pairplot(data, columns)

    # Correlation Heatmap
    plot_correlation_heatmap(data, columns)
