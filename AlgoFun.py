"""
    C.Marriott
    24/02/2025
    Dateiname: AlgoFun.py
    Kommentar: Algorythmus zur konvertierung von Dezimalsystem in Binärsystem
"""


def decimal_to_binary(decimal_number):
    bin_num = ""
    while decimal_number != 0:
        bin_num += str(decimal_number % 2)
        decimal_number = int(decimal_number / 2)
    return bin_num


print(10>9)
print(decimal_to_binary(10))