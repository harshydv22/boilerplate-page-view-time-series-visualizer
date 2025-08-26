import pandas as pd

# Read the CSV and set the index
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
# Keep only the data between 2.5th and 97.5th percentile
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]
import matplotlib.pyplot as plt

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    fig.savefig('line_plot.png')
    return fig
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = df_grouped.plot(kind='bar', figsize=(12,6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[1,2,3,4,5,6,7,8,9,10,11,12])
    fig.savefig('bar_plot.png')
    return fig
import seaborn as sns

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    
    fig, axes = plt.subplots(1,2, figsize=(15,5))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box.sort_values('month_num'), ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    fig.savefig('box_plot.png')
    return fig
