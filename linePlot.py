import pandas as pd
import datetime
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from aqitopm25 import ConcPM25

def linePlot(city):
    df = pd.read_csv(f'./CSV/Modified/{city}-2020.csv')
    df = df.sort_values(by=['Month', 'Date'])
    df = df.loc[df['Month'] < 8]

    x = [datetime.datetime(year, month, date) for (year, month, date) in zip(df['Year'], df['Month'], df['Date'])]
    y = [ConcPM25(data) for data in df['median']]

    plt.plot(x, y)
    ax = plt.subplot()

    plt.xlabel('Date',fontsize = 14)
    plt.ylabel('PM2.5 (μg/m3)', fontsize = 14)
    plt.title(f'{city} PM2.5 Levels', fontsize = 20)

    Formatter = mdates.DateFormatter("%B")
    ax.xaxis.set_major_formatter(Formatter)
    ax.set_xlim([datetime.date(2020, 1, 1), datetime.date(2020, 8, 1)])

    plt.grid()
    plt.show()


if __name__ == "__main__":
    linePlot('Beijing')
    