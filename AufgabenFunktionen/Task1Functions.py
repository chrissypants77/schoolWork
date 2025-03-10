"""
    C.Marriott
    03/03/2025
    Dateiname: Task1Functions.py
    Kommentar: Functions for Task1 which calculates area and scope of rectangle and circles
"""
import math
def area_of_rectangle(length: float, width: float) -> float:
    return length * width

def scope_of_rectangle(length: float, width: float):
    return length*2 + width*2

def area_of_circle(radius: float) -> float:
    return math.pi * radius**2

def scope_of_circle(radius: float) -> float:
    return 2 * math.pi * radius
