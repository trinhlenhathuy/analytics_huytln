import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap_by_2_dimensions(df, dim_name_x, dim_name_y, metric, highlight, save_to_excel=0):
    df = df[[dim_name_x, dim_name_y, metric]]    
    # Sort the data by `metric` in descending order and select the top N points to highlight
    top_n = df.nlargest(highlight, metric)

    # Calculate the total number of orders to determine the size of the points
    total_Sales = df[metric].sum()
    sizes = df[metric] / total_Sales * 300

    # Create the plot with Seaborn
    plt.figure(figsize=(20, 10))

    # Plot the data points
    scatter = sns.scatterplot(
        x=df[dim_name_x],
        y=df[dim_name_y],
        size=sizes,
        hue=sizes,
        sizes=(20, 300),
        alpha=0.5,
        palette='viridis',
        legend=False
    )

    # Highlight the top N points using red rectangles (lines instead of rectangles)
    for x_value in top_n[dim_name_x]:  # Use a different variable name here
        plt.axvline(x=x_value, color='red', alpha=0.3, linewidth=2)

    # Reduce the number of labels displayed on the y-axis if there are more than 50 values
    if len(df[dim_name_y].unique()) > 50:
        step = max(1, len(df[dim_name_y].unique()) // 50)
        plt.yticks(df[dim_name_y].unique()[::step], fontsize=8)  # Reduce fontsize here
    else:
        plt.yticks(fontsize=8)  # Apply smaller fontsize when there are fewer than 50 labels

    # Customize the plot
    plt.xlabel(dim_name_x)
    plt.ylabel(dim_name_y)
    plt.title(rf'{metric} by {dim_name_x} and {dim_name_y}')

    # Display the x-axis labels, rotate 45 degrees, and reduce the font size
    plt.xticks(rotation=90, fontsize=6, color='black')

    # Create a dummy plot to add the color legend
    dummy = plt.scatter([], [], c=[], cmap='viridis', s=[], alpha=0.5)
    plt.colorbar(dummy, label=metric)

    # Display the plot
    plt.show()

    if save_to_excel == 1:
        # FILTER 2 COMLUMNS: dim_name_x và metric
        top_n_export = top_n[[dim_name_x, metric]]
        output_file = f'heatmap_highlight_{dim_name_x}_{dim_name_y}.xlsx'
        top_n_export.to_excel(output_file, index=False)
        print(f'Highlighted data exported to {output_file}')
