import seaborn as sns
import matplotlib.pyplot as plt

def plot_demand_trends(df, column, save_as_pdf=False):
    sns.lineplot(data=df, x='Date', y=column)
    plt.title(f'{column} Demand Trends')
    if save_as_pdf:
        plt.savefig('reports/demand_trends_plot.pdf', dpi=300)
        print('Plot saved as demand_trends_plot.pdf')
    plt.show()

def correlation_heatmap(df):
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()