"""
    C.Marriott
    03/03/2025
    Dateiname: Task1.py
    Kommentar: Erste Aufgabe
"""
from Task1Functions import *
length = float(input("Length: "))
width = float(input("Width: "))
radius = float(input("Radius: "))

print("area of rectangle", area_of_rectangle(length, width))
print("scope of rectangle", scope_of_rectangle(length, width))
print("area of circle", area_of_circle(radius))
print("scope of circle", scope_of_circle(radius))
