"""
    C.Marriott
    21/02/2025
    Dateiname: fun.py
    Kommentar: Aufgaben zu Datentypen
"""

aufgaben = {
    "Aufgabe 1 a)": lambda : float(13.4),
    "Aufgabe 1 b)": lambda : float(" 13 "),
    "Aufgabe 1 c)": lambda : "You cant do >\tfloat(13..4)",
    "Aufgabe 1 d)": lambda : int("W"),
    "Aufgabe 1 e)": lambda x=0x12: float(x),
    "Aufgabe 1 f)": lambda x=12.34: int(x),
    "Aufgabe 1 g)": lambda x=" 12,2333 ": float(x),
    "Aufgabe 2 a)": lambda : bool("Müller"),
    "Aufgabe 2 b)": lambda : "You cant do >\tbool(false)",
    "Aufgabe 2 c)": lambda : ord("c"),
    "Aufgabe 2 d)": lambda : ord("ABC"),
    "Aufgabe 2 e)": lambda : hex(int(float(7))),
    "Aufgabe 2 f)": lambda : str(int("AB", 16)),
    "Aufgabe 3 a)": lambda : str(34.5),
    "Aufgabe 3 b)": lambda x = 3: float(x),
    "Aufgabe 3 c)": lambda x = "388": float(x),
    "Aufgabe 3 d)": lambda : float("55.55"),
    "Aufgabe 3 e)": lambda x = " 12" : int(x),
    "Aufgabe 3 f)": lambda x = 12 : str(x)
}

def test_aufgaben(aufgaben_nummer):
    for auf in aufgaben:
        if aufgaben_nummer not in auf:
            continue
        try:
            result = aufgaben[auf]()
            print(auf, ">", result)
        except:
            print(auf, "> Doesnt work")

while True:
    aufgabe = input("Geben sie die Aufgaben nummer ein dammit sie diese testen können (1/2/3/exit)\n>")
    if aufgabe == "exit":
        break
    test_aufgaben(aufgabe)
