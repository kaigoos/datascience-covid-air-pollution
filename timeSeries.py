import pandas as pd
import datetime
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from aqitopm25 import ConcPM25, shutDownDate

def update(num, x, y1, line1):
    line1.set_data(x[:num], y1[:num])
    return line1

def timeSeries(city, year):
    df = pd.read_csv(f'./CSV/Modified/{city}-{year}.csv')
    df = df.sort_values(by=['Month', 'Date'])
    df = df.loc[df['Month'] < 8]

    x = [datetime.datetime(year, month, date) for (year, month, date) in zip(df['Year'], df['Month'], df['Date'])]
    y = [ConcPM25(data) for data in df['median']]

    # plt.plot(x, y)
    fig = plt.figure(figsize = (14,8))
    ax = plt.subplot()

    line1, = ax.plot(x, y, label = year)

    plt.xlabel('Month',fontsize = 14)
    plt.ylabel('PM2.5 (μg/m3)', fontsize = 14)
    plt.title(f'{city} {year} PM2.5 Levels', fontsize = 20)
    plt.axvline(x=shutDownDate(city), color = 'black', linestyle='dashed', label='Shutdown')

    ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line1,], interval=100)

    Formatter = mdates.DateFormatter("%B")
    ax.xaxis.set_major_formatter(Formatter)
    ax.set_xlim([datetime.date(2020, 1, 1), datetime.date(2020, 8, 1)])

    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    timeSeries('Wuhan', 2020)
    