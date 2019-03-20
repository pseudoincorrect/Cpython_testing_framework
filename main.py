""" Test heart_rate.c with ctypes """

from ctypes import c_int32, CDLL
from xlrd import open_workbook
import matplotlib.pyplot as plt
import subprocess

MAKEFILE_DIR_PATH = "./heart_rate"
LIB_PATH          = "./heart_rate/lib/heart_rate.so"
EXCEL_FILE_PATH   = "./data/raw_heart_IR_1.xlsx"
LAST_ROW          = 5000
EXCEL_COLUMN      = 5
def test_filtering():
    """ Test the custom heart rate filtering """
    
    # init few variable/data structures
    raw_sensor_data = []
    filtered        = []
    row_index       = 0
    # compile the c shared library
    command = ' '.join(['cd', MAKEFILE_DIR_PATH, '&&', 'make'])
    subprocess.check_call(command, shell=True)

    # import the library in python
    lib                 = CDLL(LIB_PATH)
    hr_init             = lib.heart_rate_init
    hr_process          = lib.heart_rate_process
    hr_process.argtypes = [c_int32]
    hr_process.restype  =  c_int32

    # import data from excel file
    book  = open_workbook(EXCEL_FILE_PATH)
    sheet = book.sheet_by_index(0)

    # fill array with data from excel
    for row in range(1, LAST_ROW):
        try:
            raw_sensor_data.append(int(sheet.cell(row, EXCEL_COLUMN).value))
            row_index += 1
        except:
            pass  

    x_axis = range(0, row_index )

    # run the init function from lib
    hr_init()

    # run the main lib process against raw data
    for sensor_data in raw_sensor_data:
        filt_val = hr_process(c_int32(sensor_data))
        filtered.append(filt_val)

    # plot it
    plt.title("raw_sensor_data")
    # plt.subplot(211)
    # plt.plot(x_axis[100:], raw_sensor_data[100:])
    # plt.subplot(212)
    plt.plot(x_axis[100:], filtered[100:])
    plt.show()



if __name__ == "__main__":
    test_filtering()
