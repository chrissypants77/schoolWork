"""
    C.Marriott
    03/03/2025
    Dateiname: Task2.py
    Kommentar: Aufgabe 2 Dreieck sachen
"""
from Task2Functions import *
a = float(input("a >"))
b = float(input("b >"))
c = float(input("c >"))

if not check_is_triangle(a, b, c):
    print("Dreieck kann nicht erstellt werden!")
    exit()

scope = scope_of_triangle(a, b, c)
area = area_of_triangle(a, b, c, scope)

print("Scope of triangle:", scope)
print("Area of triangle:", area)
