"""
    C.Marriott
    03/03/2025
    Dateiname: Task3Functions.py
    Kommentar: Conversion from data sizes like KB to KiB
"""
def MB_to_MiB(data_size, unit):
    converter = {
        "KB" : 1,
        "MB" : 2,
        "GB" : 3,
        "TB" : 4,
    }
    if unit not in converter:
        print("Invalid Unit")
        return None

    converted_unit = converter[unit]
    return round((data_size * 1000 ** converted_unit) / 1024 ** converted_unit, 3)
