"""
    C.Marriott
    FEB 2025
    calcThing.py
    Antwort für die Aufgabe e)
"""
import math

print("Welcome to the circle calculator")
mm = input("Enter it in mm >")
if not (mm.isdigit()):
    print("Invalid Input. Please enter a number")
    exit()

mm = float(mm)
radius_cm = mm / 10
area_cm2 = math.pi * (radius_cm ** 2)

print("The area of the circle in cm² is: ", round(area_cm2, 2))
