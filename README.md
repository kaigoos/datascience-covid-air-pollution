# CS410/510 Final Project

This repository contains all documentation and Python scripts for Todd Graham and Kyle Gustke's final project. 

## Documents:

The Document folder contains our Project Plan, Midpoint Report, Research Paper (The impacts of COVID-19 on an Air Quality Metric (PM2.5)_Gustke_Graham) and Final Presentation (Graham_Gustke_Final_Presentation). The file 2019vs2020_graphs.pdf contains the graphs that are included in the Final Presentation appendix.

## Python Scripts:

### CSV Parser:

The CSV parser is a basic script to parse data by fields under specific columns.
The parser is strictly meant for personal use and is in no way robust or user friendly.
Make sure the input is precise when using.

Formatting option should only be used for files in the Original folder. To modify other files in the Formatted or Modified folder user the Parsing option instead.

To use the parser create a folder called CSV under the main project folder.
Then create 3 sub folders in the CSV folder names Formatted, Modfied, and Original. 

Usage: 

```python
python interface.py
```

### Visualization Tools:

heatmap.py, linePlot.py, ScatterPlot.py, and timeSeries.py are all the different types of graphs implemented. Each type of plot is run through the GUI in App.py. 

Usage: 

```python
python App.py
```