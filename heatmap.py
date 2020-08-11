import pandas as pd
import datetime
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import seaborn as sns
from aqitopm25 import ConcPM25, shutDownDate

def linePlot(city, year):
    df = pd.read_csv(f'./CSV/Modified/{city}-{year}.csv')
    df = df.sort_values(by=['Month', 'Date'])
    df = df.loc[df['Month'] < 8]

    # x = [datetime.datetime(year, month, date) for (year, month, date) in zip(df['Year'], df['Month'], df['Date'])]
    # y = [ConcPM25(data) for data in df['median']]

    colorMap = ['#008000', '#FFFF00', '#FFA500', '#FF0000', '#800080', '#800080', '#800000', '#800000', '#800000', '#800000']

    green_patch = mpatches.Patch(color='green', label='Good')
    yellow_patch = mpatches.Patch(color='yellow', label='Moderate')
    orange_patch = mpatches.Patch(color='orange', label='Unhealthy for Sensitive Groups')
    red_patch = mpatches.Patch(color='red', label='Unhealthy')
    purple_patch = mpatches.Patch(color='purple', label='Very Unhealthy')
    maroon_patch = mpatches.Patch(color='maroon', label='Hazardous')

    cmap = mcolors.LinearSegmentedColormap.from_list('mycmap', colorMap)
    plt.legend(handles=[green_patch, yellow_patch, orange_patch, red_patch, purple_patch, maroon_patch])

    plt.title(f'{city} {year} PM2.5 Levels', fontsize = 20)
    heatmapData = pd.pivot_table(df, values='median', index=['Month'], columns='Date')
    sns.heatmap(heatmapData, annot=False, fmt='g', cmap=cmap, vmin=0, vmax=500)

    plt.show()


if __name__ == "__main__":
    linePlot('Wuhan', 2020)
    