"""
    C.Marriott
    FEB 2025
    calcThing.py
    Antwort für die Aufgabe f)
"""

celc = input("Please enter the temperature in Celsius: ")
if not celc.isdigit():
    exit()
celc = float(celc)
print(celc*9/5 + 32, "°F")
