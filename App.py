from tkinter import Tk, Button, Label, StringVar, OptionMenu
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from linePlot import linePlot
from heatmap import heatMap
from ScatterPlot import scatter_plot
from timeSeries import timeSeries

import numpy as np

class MainWindow(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.city = ''
        self.graph = ''
        self.year = None
        self.year2 = None

        self.wm_title("Air Quality Comparisons")
        self.attributes('-topmost', True)

        self.mainWidgets()

    def mainWidgets(self):
        cityLabel = Label (self, text="City:")
        cityLabel.grid(row = 0, column = 0)

        cityNames = ['Beijing', 'Los_Angeles', 'Madrid', 'New_Delhi', 'New_York', 'Portland', 'Rome', 'Wuhan']
        dropDownCity = StringVar(self)
        dropDownCity.set(cityNames[0]) # default value
        dropDownCityButton = OptionMenu(self, dropDownCity, *cityNames)
        dropDownCityButton.grid(row = 0, column = 1)

        graphLabel = Label (self, text="Graph:")
        graphLabel.grid(row = 1, column = 0)

        graphNames = ['Heatmap', 'Line', 'Scatter', 'Time-Series']
        dropDownGraph = StringVar(self)
        dropDownGraph.set(graphNames[0]) # default value
        dropDownGraphButton = OptionMenu(self, dropDownGraph, *graphNames)
        dropDownGraphButton.grid(row = 1, column = 1)

        yearLabel = Label (self, text="Year 1:")
        yearLabel.grid(row = 2, column = 0)

        years = [2015, 2016, 2017, 2018, 2019, 2020]
        dropDownYear = StringVar(self)
        dropDownYear.set(years[0]) # default value
        dropDownYearButton = OptionMenu(self, dropDownYear, *years)
        dropDownYearButton.grid(row = 2, column = 1)

        year2Label = Label (self, text="Year 2:")
        year2Label.grid(row = 3, column = 0)

        year2 = [None, 2015, 2016, 2017, 2018, 2019, 2020]
        dropDownYear2 = StringVar(self)
        dropDownYear2.set(year2[0]) # default value
        dropDownYearButton2 = OptionMenu(self, dropDownYear2, *year2)
        dropDownYearButton2.grid(row = 3, column = 1)

        submitButton = Button(self, text="Submit", command=lambda: self.printGraph(dropDownCity, dropDownGraph, dropDownYear, dropDownYear2))
        submitButton.grid(row = 4, column = 0)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.grid(row = 4, column = 1)

        # self.printGraph()

    def printGraph(self, city, graph, year, year2):
        self.city = city.get()
        self.graph = graph.get()
        self.year = year.get()
        if(year2.get() != 'None'):
            self.year2 = year2.get()
        else:
            self.year2 = None

        if(self.graph == 'Heatmap'):
            heatMap(self.city, self.year)
        elif(self.graph == 'Line'):
            linePlot(self.city, self.year, self.year2)
        elif(self.graph == 'Scatter'):
            scatter_plot(self.city, self.year)
        elif(self.graph == 'Time-Series'):
            timeSeries(self.city, self.year, self.year2)
        
        # fig = Figure(figsize=(5, 4), dpi=100)
        # t = np.arange(0, 3, .01)
        # fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))

        # canvas = FigureCanvasTkAgg(fig, self)
        # canvas.draw()

        # canvas.get_tk_widget().grid(row = 0, column = 2, rowspan = 4)

    def _quit(self):
        self.quit() 
        self.destroy()

if __name__=="__main__":
    app = MainWindow(None)
    app.mainloop()