import pandas as pd
import glob


class csvParser(object):
    # def __init__(self):
    def format_data(self, file):
        """
        Separate Date field into Year, Month, Data and remove
        comments in the header.
        """
        data = pd.read_csv(file, skiprows=4)
        data.insert(0, 'Year', "")
        data.insert(1, 'Month', "")
        data[['Year', 'Month', 'Date']] = data.Date.apply(lambda x: pd.Series(str(x).split('-')))
        return data

    def read_data(self, file):
        """
        Returns csv as dataframe, use only for Formatted or Modified data
        """
        data = pd.read_csv(file)
        data["Year"] = data["Year"].astype(int)
        return data


    def write_data(self, data, path, name):
        """
        Convert dataframe to csv and write to specified path.
        """
        data.to_csv(path + '/' + name, index=False)

    def parse_by_column(self, data, column, param):
        """
        Parse data based on column, INCOMPLETE
        """
        matches = ["Country", "City", "Specie"]
        if any(x in column for x in matches):
            data = data.loc[data[column] == param]
        else:
            data = data.loc[data[column] == float(param)]
        return data
