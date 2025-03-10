"""
    C.Marriott
    28/02/2025
    Dateiname: uebung_funktionen.py
    Kommentar:
"""

def spannung_calc(ampere, widerstand):
    return ampere * widerstand


def leistung_calc(volt, ampere):
    return volt * ampere


def kapazitaet_calc(ladung, spannung):
    return ladung / spannung

ampere = float(input("Stromstärke (A): "))
widerstand = float(input("Wiederstand (\u2126): "))
spannung = spannung_calc(ampere, widerstand)
# stromstaerke  = float(input("Stromstärke(A): "))
ladung  = float(input("Ladung (Coulomb): "))
# spannung  = float(input("Spannung(V): "))

print("Spannung: ", spannung_calc(ampere, widerstand))
print("Leistung: ", leistung_calc(spannung, ampere))
print("Kapazität:",kapazitaet_calc(ladung, spannung),"Farad")
