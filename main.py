# This is a sample Python script.
# https://pypi.org/project/openpyxl/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openpyxl
import os

def readExcelWorkbook():
    print("inside readWorkbook")
    print(f"OpenPyXL version: {openpyxl.__version__}")
    print(f"current working directory is: {os.getcwd()}")
    # C:\Users\frede\Dropbox\Family Room\S-Drive\Holiday Cards\2022 Card list.xlsx
    # C:\Users\frede\Dropbox\download\python\Automate_the_Boring_Stuff\example.xlsx
    #fn : str = r"C:\Users\frede\Dropbox\Family Room\S-Drive\Holiday Cards\2022 Card list.xlsx"
    #fn: str = r"C:\Users\frede\Dropbox\download\python\Automate_the_Boring_Stuff\example.xlsx"
    fn: str = "example.xlsx"
    wb = openpyxl.load_workbook(filename=fn, read_only=True)
    print(f"wb typs: {type(wb)}")
    print("after load_workbook")
    print(f"sheetnames: {wb.sheetnames}")
    ws = wb.active
    print(f"The active worksheet title={ws.title}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readExcelWorkbook()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
