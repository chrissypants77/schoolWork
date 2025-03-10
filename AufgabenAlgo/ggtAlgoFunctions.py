"""
    C.Marriott
    03/03/2025
    Dateiname: ggtAlgoFunctions.py
    Kommentar: ggt sub file for functions
"""

def user_input(text):
    while True:
        user = input(text)
        try:
            user = int(user)
            if user > 0:
                return user
            print("Number cant be negative")
        except ValueError:
            try:
                user = float(user.replace(",", "."))
                if user > 0:
                    return user
                print("Number cant be negative")
            except ValueError:
                print("Invalid Number")
                #

def print_dict(printable:dict):
    for key, value in printable.items():
        print(f"{key}: {value}")