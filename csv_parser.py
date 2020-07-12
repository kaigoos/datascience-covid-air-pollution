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

    def parse_by_column(self, data, column, *args):
        """
        Parse data based on column, INCOMPLETE
        """
        matches = ["Country", "City", "Specie"]
        temp = pd.DataFrame()
        for param in args:
            if any(x in column for x in matches):
                if temp.empty is True:
                    temp = data.loc[data[column] == param]
                else:
                    temp = temp.append(data.loc[data[column] == param])
            else:
                if temp.empty is True:
                    temp = data.loc[data[column] == float(param)]
                else:
                    temp = temp.append(data.loc[data[column] == float(param)])
        return temp

    def calc_data(self, data):
        row_count = data.index
        city_count = data.City.unique()
        min_mean = data["min"].mean()
        max_mean = data["max"].mean()
        median_mean = data["median"].mean()
        variance_mean = data["variance"].mean()
        print(f"Rows: {row_count}")
        print(f"Cities: {city_count.size}")
        print(f"Average minimum: {min_mean}")
        print(f"Average maximum: {max_mean}")
        print(f"Average median: {median_mean}")
        print(f"Average variance: {variance_mean}")

