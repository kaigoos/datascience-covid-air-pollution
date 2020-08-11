import pandas as pd
import datetime
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from aqitopm25 import ConcPM25, shutDownDate

def timeSeries(city, year1, year2 = None):
    # Retrieve dataframe, sort the values by month and day, then omit the data after July
    df1 = pd.read_csv(f'./CSV/Modified/{city}-{year1}.csv')
    df1 = df1.sort_values(by=['Month', 'Date'])
    df1 = df1.loc[df1['Month'] < 8]

    fig = plt.figure(figsize = (14,8))
    ax = plt.subplot()

    x1 = [datetime.date(2020, month, date) for (month, date) in zip(df1['Month'], df1['Date'])]
    y1 = [ConcPM25(data) for data in df1['median']]     # Convert to microgram/cubic meter
    line1, = ax.plot(x1, y1, label = year1)

    if(year2 != None):
        df2 = pd.read_csv(f'./CSV/Modified/{city}-{year2}.csv')
        df2 = df2.sort_values(by=['Month', 'Date'])
        df2 = df2.loc[df2['Month'] < 8]

        x2 = []

        for (month, day) in zip(df2['Month'], df2['Date']):
            date = datetime.date(2020, month, day)
            x2.append(date)
        y2 = [ConcPM25(data) for data in df2['median']]
        line2, = ax.plot(x2, y2, label = year2)

    plt.xlabel('Month',fontsize = 14)
    plt.ylabel('PM$_{2.5}$ (μg/m$^3$)', fontsize = 14)

    if(year2 != None):
        plt.title(f'{city} {year1} & {year2} PM2.5 Levels', fontsize = 20)
    else:
        plt.title(f'{city} {year1} PM2.5 Levels', fontsize = 20)

    # Only display shutdown date if one of the years is 2020
    if (str(year1) == '2020' or str(year2) == '2020'):    
        plt.axvline(x=shutDownDate(city), color = 'black', linestyle='dashed', label='Initial Lockdown')
    plt.axhline(y=10, color='#bfbfbf', linestyle=':', label='Air Quality Guideline')

    def update(num):
        line1.set_data(x1[:num], y1[:num])
        if(year2 != None):
            line2.set_data(x2[:num], y2[:num])

    # Animate call
    ani = animation.FuncAnimation(fig, update, len(x1), interval=100)

    # Format dates to include month names
    Formatter = mdates.DateFormatter("%B")
    ax.xaxis.set_major_formatter(Formatter)
    ax.set_xlim([datetime.date(2020, 1, 1), datetime.date(2020, 8, 1)])

    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    timeSeries('Wuhan', 2020, 2019)
