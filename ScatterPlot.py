import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sn
import pandas as pd
import datetime
import os
from aqitopm25 import ConcPM25


class ScatterPlot(object):

    def __init__(self, file):
        self.data = pd.read_csv(file)
        self.name= file

    def plot(self):

        good_data = []
        good_date = []
        moderate_data = []
        moderate_date =[]
        sensitive_data = []
        sensitive_date = []
        unhealthy_data = []
        unhealthy_date = []
        very_unhealthy_data = []
        very_unhealthy_date = []
        hazardous_data = []
        hazardous_date = []

        for (year, month, date, data) in zip(self.data['Year'], self.data['Month'], self.data['Date'], self.data['median']):
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

        if good_data:
            sn.scatterplot(good_date, good_data, color="green", ax=ax)
        if moderate_data:
            sn.scatterplot(moderate_date, moderate_data, color="gold", ax=ax)
        if sensitive_data:
            sn.scatterplot(sensitive_date, sensitive_data, color="orange", ax=ax)
        if unhealthy_data:
            sn.scatterplot(unhealthy_date, unhealthy_data, color="red", ax=ax)
        if very_unhealthy_data:
            sn.scatterplot(very_unhealthy_date, very_unhealthy_data, color="purple", ax=ax)
        if hazardous_data:
            sn.scatterplot(hazardous_date, hazardous_data, color="darkred", ax=ax)

        formatter = mdates.DateFormatter("%B")
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel("Date")
        ax.set_ylabel("PM2.5(\u03BCg/m$^3$)")
        ax.set_xlim([datetime.date(2020, 1, 1), datetime.date(2020, 8, 1)])
        base = os.path.basename(self.name)
        title = os.path.splitext(base)[0]
        plt.title(f'{title} PM2.5 Levels')

        plt.show()


if __name__ == "__main__":
    sp = ScatterPlot('./CSV/Modified/Wuhan-2020.csv')
    sp.plot()
