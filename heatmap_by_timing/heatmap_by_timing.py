import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap_by_timing(df, dim_name, metric, highlight):
    # Sort the data by `metric` in descending order and select the top N points to highlight
    top_n = df.nlargest(highlight, metric)

    # Calculate the total number of orders to determine the size of the points
    total_Sales = df[metric].sum()
    sizes = df[metric] / total_Sales * 300

    # Create the plot with Seaborn
    plt.figure(figsize=(20, 10))

    # Plot the data points
    scatter = sns.scatterplot(
        x=df['timing'],
        y=df[dim_name],
        size=sizes,
        hue=sizes,
        sizes=(20, 300),
        alpha=0.5,
        palette='viridis',
        legend=False
    )

    # Get the unique labels of `timing`
    unique_timing = df['timing'].unique()

    # Draw red rectangles to highlight the top N points
    for timing in top_n['timing']:
        plt.axvspan(
            timing, timing,
            color='red', alpha=0.3, linewidth=2
        )

    # Reduce the number of labels displayed on the y-axis if there are more than 50 values
    if len(df[dim_name].unique()) > 50:
        step = max(1, len(df[dim_name].unique()) // 50)
        plt.yticks(df[dim_name].unique()[::step], fontsize=8)  # Reduce fontsize here
    else:
        plt.yticks(fontsize=8)  # Apply smaller fontsize when there are fewer than 50 labels

    # Customize the plot
    plt.xlabel('Timing')
    plt.ylabel(dim_name)
    plt.title(f'{metric} by Timing and {dim_name}')

    # Display the x-axis labels, rotate 45 degrees, and reduce the font size
    plt.xticks(rotation=90, fontsize=6, color='black')

    # Create a dummy plot to add the color legend
    dummy = plt.scatter([], [], c=[], cmap='viridis', s=[], alpha=0.5)
    plt.colorbar(dummy, label=metric)

    # Display the plot
    plt.show()
