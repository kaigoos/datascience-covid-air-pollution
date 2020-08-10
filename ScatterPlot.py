import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sn
import pandas as pd
import datetime
from aqitopm25 import ConcPM25


class ScatterPlot(object):

    def __init__(self, file):
        self.data = pd.read_csv(file)

    def plot(self):
        x = [datetime.datetime(year, month, date) for (year, month, date) in zip(self.data['Year'], self.data['Month'], self.data['Date'])]
        y = [ConcPM25(data) for data in self.data['median']]

        #ax = sn.scatterplot(x, self.data['median'])
        ax = sn.scatterplot(x, y)
        formatter = mdates.DateFormatter("%B")
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlim([datetime.date(2020, 1, 1), datetime.date(2020, 8, 1)])

        plt.show()


if __name__ == "__main__":
    sp = ScatterPlot('./CSV/Modified/Portland-2020.csv')
    sp.plot()
