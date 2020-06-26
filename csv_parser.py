import pandas as pd
import os

class csvParser(object):
    def __init__(self):
        # Change into CSV/Orignal directory and read csv
        try:
            os.chdir("./CSV/Original")
            data = pd.read_csv("waqi-covid19-airqualitydata-2020.csv", skiprows=4)
        except OSError:
            print("Can't change the Current Working Directory")

        # Change into CSV/Modified to write dataframe as csv
        try:
            os.chdir("../Modified")
            print("Enter a name for the new file: ")
            file_name = str(input())
            # Make sure the file ends with the .csv extension
            if file_name[-4:] != ".csv":
                file_name += ".csv"

            data.to_csv(file_name, index=False)
        except OSError:
            print("Can't change the Current Working Directory")

if __name__=='__main__':
    parser = csvParser()
