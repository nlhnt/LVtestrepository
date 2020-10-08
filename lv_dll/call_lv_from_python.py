import ctypes
from ctypes import *

# based on
# https://stackoverflow.com/questions/252417/how-can-i-use-a-dll-file-from-python

# Load DLL into memory
# for 64bit Python
lv_dll = cdll.LoadLibrary('builds/lv_maths_x64.dll')
# for 32bit Python
# lv_dll = cdl.LoadLibrary('builds/lv_maths.dll')

# Set up prototype and parameters for the desired function call
lv_power_of_2 = lv_dll.Power_of_2

# Inform python of the expected return type, by default it is c_int
lv_power_of_2.restype = c_double

# Show the dll working
print(lv_power_of_2(c_double(2.0)))

# You can also do more, by setting the types of expected arguments by the functions
# read:
# https://docs.python.org/3/library/ctypes.html#return-types