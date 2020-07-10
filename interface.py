import pandas as pd
from csv_parser import csvParser

def list_menu():
    """
    List main menu to user
    """
    print("1. Format csv")
    print("2. Something else")

def main_menu():
    list_menu()

def format_data():
    """
    Ask User for a file from the Original folder and format csv
    to separate Date field into Year, Month, Data and remove
    comments in the header.
    Save the modified file to Formatted folder
    """
    file_list = parser.create_file_list("./CSV/Original")
    parser.list_files(file_list)
    num = int(input("Enter file #: "))
    file_name = file_list[num - 1]
    print("This might take a while....")
    data = parser.format_data(file_name)
    parser.write_data(data, "../Formatted", file_name)

if __name__ == '__main__':
    parser = csvParser()
    format_data()
