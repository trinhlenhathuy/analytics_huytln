# pareto.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_pareto_chart(df, dim_name, metric):
    df_pareto = prepare_pareto_data(df, f'{dim_name}', f'{metric}')
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.bar(df_pareto.index + 1, df_pareto[f'{metric}'], color='C0')
    ax1.set_xlabel(f'{dim_name}')
    ax1.set_ylabel(f'{metric}', color='C0')
    ax1.tick_params(axis='y', labelcolor='C0')
    ax1.set_xticks(df_pareto.index + 1)
    ax1.set_xticklabels(df_pareto[f'{dim_name}'], rotation=90, fontsize=5)
    ax2 = ax1.twinx()
    ax2.plot(df_pareto.index + 1, df_pareto['cumulative_percent'], color='C1', marker='o', ms=2)
    ax2.set_ylabel('Cumulative Percent', color='C1')
    ax2.tick_params(axis='y', labelcolor='C1')
    ax2.axhline(80, color='gray', linestyle='--', lw=1)
    ax2.axhline(95, color='gray', linestyle='--', lw=1)
    index_80 = (df_pareto['cumulative_percent'] >= 80).idxmax() + 1
    index_95 = (df_pareto['cumulative_percent'] >= 95).idxmax() + 1
    ax2.plot([index_80, index_80], [0, 80], color='gray', linestyle='--', lw=1)
    ax2.plot([index_95, index_95], [0, 95], color='gray', linestyle='--', lw=1)
    prod_at_80 = df_pareto.iloc[index_80 - 1][dim_name]
    prod_at_95 = df_pareto.iloc[index_95 - 1][dim_name]
    ax2.text(index_80, 80, f'{prod_at_80}: 80%', color='C1', ha='left')
    ax2.text(index_95, 95, f'{prod_at_95}: 95%', color='C1', ha='right')
    plt.title(f'Biểu đồ Pareto của {dim_name} và {metric}')
    total_sales_to_80 = df_pareto.iloc[:index_80][metric].sum().round()
    total_skus_to_80 = index_80
    total_sales_to_95 = df_pareto.iloc[:index_95][metric].sum().round()
    total_skus_to_95 = index_95
    total_skus = len(df_pareto)
    table_data = [
        ["80%", total_sales_to_80, total_skus_to_80, f'{total_skus_to_80/total_skus:.2%}'],
        ["95%", total_sales_to_95, total_skus_to_95, f'{total_skus_to_95/total_skus:.2%}']
    ]
    column_labels = ["Level", f"{metric}", f"Total {dim_name} to X%", f"Percent of {dim_name}"]
    table = plt.table(cellText=table_data, colLabels=column_labels, cellLoc='center', loc='center', bbox=[0.4, 0.2, 0.55, 0.2])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.subplots_adjust(bottom=0.35)
    plt.show()

def prepare_pareto_data(df, dim_name, metric):
    df.columns = [dim_name, metric]
    df = df.sort_values(by=metric, ascending=False)
    total_count = df[metric].sum()
    df['cumulative_percent'] = (df[metric].cumsum() / total_count) * 100
    df = df.sort_values(by=[metric, 'cumulative_percent'], ascending=[False, True]).reset_index(drop=True)
    return df
