import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sn
import pandas as pd
import datetime
from aqitopm25 import ConcPM25, shutDownDate


def scatter_plot(city, year):
    df = pd.read_csv(f'./CSV/Modified/{city}-{year}.csv')

    good_data = []
    good_date = []
    moderate_data = []
    moderate_date = []
    sensitive_data = []
    sensitive_date = []
    unhealthy_data = []
    unhealthy_date = []
    very_unhealthy_data = []
    very_unhealthy_date = []
    hazardous_data = []
    hazardous_date = []

    for (year, month, date, data) in zip(df['Year'], df['Month'], df['Date'], df['median']):
        data = ConcPM25(data)
        if 0 < data <= 15:
            good_date.append(datetime.datetime(year, month, date))
            good_data.append(data)
        elif 15 < data <= 40:
            moderate_date.append(datetime.datetime(year, month, date))
            moderate_data.append(data)
        elif 40 < data <= 65:
            sensitive_date.append(datetime.datetime(year, month, date))
            sensitive_data.append(data)
        elif 65 < data <= 150:
            unhealthy_date.append(datetime.datetime(year, month, date))
            unhealthy_data.append(data)
        elif 150 < data <= 250:
            very_unhealthy_date.append(datetime.datetime(year, month, date))
            very_unhealthy_data.append(data)
        else:
            hazardous_date.append(datetime.datetime(year, month, date))
            hazardous_data.append(data)

    fig, ax = plt.subplots()

    g_ax = None
    m_ax = None
    s_ax = None
    uh_ax = None
    vuh_ax = None
    h_ax = None

    if good_data:
        g_ax = sn.scatterplot(good_date, good_data, color="green", ax=ax)
    if moderate_data:
        m_ax = sn.scatterplot(moderate_date, moderate_data, color="gold", ax=ax)
    if sensitive_data:
        s_ax = sn.scatterplot(sensitive_date, sensitive_data, color="orange", ax=ax)
    if unhealthy_data:
        uh_ax = sn.scatterplot(unhealthy_date, unhealthy_data, color="red", ax=ax)
    if very_unhealthy_data:
        vuh_ax = sn.scatterplot(very_unhealthy_date, very_unhealthy_data, color="purple", ax=ax)
    if hazardous_data:
        h_ax = sn.scatterplot(hazardous_date, hazardous_data, color="maroon", ax=ax)

    formatter = mdates.DateFormatter("%B")
    ax.xaxis.set_major_formatter(formatter)
    ax.set_xlabel("Date", fontsize=14)
    ax.set_ylabel("PM$_{2.5}$(\u03BCg/m$^3$)", fontsize=14)
    ax.set_xlim([datetime.date(year, 1, 1), datetime.date(year, 8, 1)])
    plt.title(f'{city} {year} PM2.5 Levels', fontsize=20)

    hline = plt.axhline(y=10, color='#bfbfbf', linestyle=':', label='Air Quality Guideline')
    vline = None

    labels = ['Air Quality Guideline', f'Good: {len(good_data)}', f'Moderate: {len(moderate_data)}',
              f'Unhealthy for Sensitive Groups: {len(sensitive_data)}', f'Unhealthy: {len(unhealthy_data)}',
              f'Very Unhealthy: {len(very_unhealthy_data)}', f'Hazardous: {len(hazardous_data)}']
    handles = [hline, g_ax, m_ax, s_ax, uh_ax, vuh_ax, h_ax],

    if year == 2020:
        labels = ['Air Quality Guideline', 'Initial Lockdown', f'Good: {len(good_data)}', f'Moderate: {len(moderate_data)}',
                  f'Unhealthy for Sensitive Groups: {len(sensitive_data)}', f'Unhealthy: {len(unhealthy_data)}',
                  f'Very Unhealthy: {len(very_unhealthy_data)}', f'Hazardous: {len(hazardous_data)}']
        vline = plt.axvline(x=shutDownDate(city), color='gray', linestyle='dashed', label='Initial Lockdown')
        handles = [vline, hline, g_ax, m_ax, s_ax, uh_ax, vuh_ax, h_ax],

    fig.legend(
        handles,
        labels=labels,
        bbox_to_anchor=(0.5, 0.38, 0.4, 0.5)
    )
    plt.show()


if __name__ == "__main__":
    scatter_plot('Wuhan', 2020)
