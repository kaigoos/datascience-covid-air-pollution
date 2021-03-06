import pandas as pd
import datetime
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from aqitopm25 import ConcPM25, shutDownDate


def linePlot(city, year, year2=None):
    # Retrieve dataframe, sort the values by month and day, then omit the data after July
    df = pd.read_csv(f'./CSV/Modified/{city}-{year}.csv')
    df = df.sort_values(by=['Month', 'Date'])
    df = df.loc[df['Month'] < 8]

    x = [datetime.datetime(2020, month, date) for (month, date) in zip(df['Month'], df['Date'])]
    y = [ConcPM25(data) for data in df['median']]   # Convert to microgram/cubic meter

    plt.plot(x, y, label=year)
    ax = plt.subplot()

    if year2 != None:
        df2 = pd.read_csv(f'./CSV/Modified/{city}-{year2}.csv')
        df2 = df2.sort_values(by=['Month', 'Date'])
        df2 = df2.loc[df2['Month'] < 8]

        x_prev = [datetime.datetime(2020, month, date) for (month, date) in zip(df2['Month'], df2['Date'])]
        y_prev = [ConcPM25(data) for data in df2['median']]
        plt.plot(x_prev, y_prev, label=year2)

    plt.xlabel('Month',fontsize = 14)
    plt.ylabel('PM$_{2.5}$(\u03BCg/m$^3$)', fontsize = 14)

    if year2 != None:
        plt.title(f'{city} {year} & {year2} PM2.5 Levels', fontsize = 20)
    else:
        plt.title(f'{city} {year} PM2.5 Levels', fontsize = 20)

    # Only display shutdown date if one of the years is 2020
    if (str(year) == '2020' or str(year2) == '2020'):
        plt.axvline(x=shutDownDate(city), color='black', linestyle='dashed', label='Initial Lockdown')
    plt.axhline(y=10, color='#bfbfbf', linestyle=':', label='Air Quality Guideline')

    # Format dates to include month names
    Formatter = mdates.DateFormatter("%B")
    ax.xaxis.set_major_formatter(Formatter)
    ax.set_xlim([datetime.date(2020, 1, 1), datetime.date(2020, 8, 1)])

    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    linePlot('Wuhan', 2020, 2019)
