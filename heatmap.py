import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

def heatMap(city, year):
    df = pd.read_csv(f'./CSV/Modified/{city}-{year}.csv')
    df = df.sort_values(by=['Month', 'Date'])
    df = df.loc[df['Month'] < 8]
    colorMap = ['#008000', '#FFFF00', '#FFA500', '#FF0000', '#800080', '#800080', '#800000', '#800000', '#800000', '#800000']

    cmap = mcolors.LinearSegmentedColormap.from_list('mycmap', colorMap)

    plt.title(f'{city} {year} PM2.5 Levels', fontsize=20)
    heatmapData = pd.pivot_table(df, values='median', index=['Month'], columns='Date')
    sns.heatmap(heatmapData, annot=False, fmt='g', cmap=cmap, vmin=0, vmax=500)
    plt.savefig("output.png", bbox_inches="tight")
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)

    plt.show()


if __name__ == "__main__":
    heatMap('Wuhan', 2020)
