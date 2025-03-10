"""
    C.Marriott
    14/02/2025
    Dateiname: calculator.py
    Kommentar: Implementiert eine einfache Zahlenrechner-Funktion mit den bekannten Operatoren
"""

operations = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "**": lambda x, y: x**y,
    "/": lambda x, y: x/y
}


def convert_to_int(num):
    try:
        return float(num)
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()


print("Easy Calculator")

number1 = convert_to_int(input("Enter the first number >"))
number2 = convert_to_int(input("Enter the second number >"))

operator = input(f"Enter the operator {str(tuple(operations.keys())).replace("'", '')} >")
if operator == "/" and number2 == 0:
    print("Cannot divide by zero")
elif operator in operations:
    result = operations[operator](number1, number2)
    print(f"{number1} {operator} {number2} = {result:.2f}")
else:
    print("Invalid operator")