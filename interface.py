import os
from csv_parser import csvParser


def list_menu():
    """
    List main menu to user
    """
    print("1. Parse CSV")
    print("2. Format CSV")
    print("3. Calculate Data")


def list_file_menu():
    """
    List main menu to user
    """
    print("1. Formatted")
    print("2. Modified")

    num = int(input("Enter option #: "))
    return num


def list_files(file_list):
    """
    List each file in the file_list with numerical ordering
    """
    num = 1
    for file in file_list:
        print(str(num) + ": " + file)
        num += 1


def format_data():
    """
    Ask User for a file from the Original folder and format csv
    to separate Date field into Year, Month, Data and remove
    comments in the header.
    Save the modified file to Formatted folder
    """
    file_list = os.listdir("./CSV/Original")
    list_files(file_list)
    num = int(input("Enter file #: "))
    file_name = file_list[num - 1]
    print("This might take a while....")
    data = parser.format_data("./CSV/Original/" + file_name)
    #add option to name file later
    parser.write_data(data, "./CSV/Formatted", file_name)


def parse_data():
    """
    Parse data from a specific CSV files by the given parameter.
    User has option of using CSV from Formatted or Modfied folder.
    Column names and filed names must be precice.
    Write to Modified when finished.
    """
    flag = False

    num = list_file_menu()
    if num is 1:
        path = "./CSV/Formatted"
    else:
        path = "./CSV/Modified"
    file_list = os.listdir(path)
    list_files(file_list)
    num = int(input("Enter file #: "))
    file_name = file_list[num - 1]
    data = parser.read_data(path + '/' + file_name)

    while flag is False:
        column = input('Enter column name: ')
        param = input('Enter parameter name: ')
        data = parser.parse_by_column(data, column, param)
        cont = int(input('Continue 1, Stop 0: '))
        if cont == 0:
            flag = True

    if data.empty is True:
        print("Empty data cannot be saved")
        return

    file_name = input("Enter file name: ")
    # Make sure the file ends with the .csv extension
    if file_name[-4:] != ".csv":
        file_name += ".csv"
    parser.write_data(data, "./CSV/Modified", file_name)

def calc_data():
    file_list = os.listdir("./CSV/Modified")
    list_files(file_list)
    num = int(input("Enter file #: "))
    file_name = file_list[num - 1]
    data = parser.read_data("./CSV/Modified/" + file_name)
    parser.calc_data(data)

def main_menu():
    list_menu()
    num = int(input("Enter Option #: "))
    if num is 1:
        parse_data()
    if num is 2:
        format_data()
    if num is 3:
        calc_data()


if __name__ == '__main__':
    parser = csvParser()
    main_menu()
