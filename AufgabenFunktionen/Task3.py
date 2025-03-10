"""
    C.Marriott
    03/03/2025
    Dateiname: Task3.py
    Kommentar: MB to MiB
"""
from Task3Functions import *
data_unit = input("Data Unit Size (KB/MB/GB/TB): ")
data_size = float(input(f"Data size in {data_unit}: "))

print(MB_to_MiB(data_size, data_unit), data_unit[0]+"iB")
