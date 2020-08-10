import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sn
import pandas as pd
import datetime


class ScatterPlot(object):

    def __init__(self, file):
        self.data = pd.read_csv(file)

    def plot(self):
        ax = sn.scatterplot(x='Month', y='median', data=self.data)
        x = []
        y = self.data['Month'][2]
        #for data in self.data:
        #    year = int(data['Year'])
        #    month = int(data['Month'])
        #    date = int(data['Date'])
        #    x = x.append(datetime.datetime(year, month, date))
        # x = datetime.datetime(self.data)
        plt.show()


if __name__ == "__main__":
    sp = ScatterPlot('./CSV/Modified/CN-2020.csv')
    sp.plot()
