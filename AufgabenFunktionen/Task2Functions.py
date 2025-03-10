"""
    C.Marriott
    03/03/2025
    Dateiname: Task2Functions.py
    Kommentar: Functions to calculate Triangle stuff
"""

import math

def area_of_triangle(a: float, b: float, c: float, scope: float) -> float:
    s = scope/2
    tmp = s*(s-a)*(s-b)*(s-c)
    return math.sqrt(tmp)


def scope_of_triangle(a: float, b: float, c: float) -> float:
    return a + b + c

def check_is_triangle(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True