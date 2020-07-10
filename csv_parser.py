import pandas as pd
import os
import glob


class csvParser(object):
    # def __init__(self):

    def create_file_list(self, path):
        """
        Create a list of files in the specified path
        and return as a list.
        """
        try:
            os.chdir(path)
        except OSError:
            print("Can't change the Current Working Directory")

        file_list = []
        for file in glob.glob("*.csv"):
            file_list.append(file)

        return file_list

    def list_files(self, file_list):
        """
        List each file in the file_list with numerical ordering
        """
        num = 1
        for file in file_list:
            print(str(num) + ": " + file)
            num += 1;

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

    def write_data(self, data, path, name):
        """
        Convert dataframe to csv and write to specified path.
        """
        try:
            #Move this to interface later
            #print("Enter a name for the new file: ")
            #file_name = str(input())
            # Make sure the file ends with the .csv extension
            #if file_name[-4:] != ".csv":
            #    file_name += ".csv"
            os.chdir(path)
            data.to_csv(name, index=False)
        except OSError:
            print("Can't change the Current Working Directory")

    def parse_by_column(self, data):
        """
        Parse data based on column, INCOMPLETE
        """
        data = data.loc[data['Specie'] == 'pm25']
        data = data.loc[data['Country'] == 'CN']
        return data
