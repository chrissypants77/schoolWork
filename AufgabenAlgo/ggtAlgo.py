"""
    C.Marriott
    03/03/2025
    Dateiname: ggtAlgo.py
    Kommentar: ggt Algo haupt file
"""
from ggtAlgoFunctions import *
from Methematik import *
A = user_input("Input A: ")
B = user_input("Input B: ")

# A = int(input("Input A: "))
# B = int(input("Input B: "))

a_binary = decimal_to_binary(A)
b_binary = decimal_to_binary(B)
print("=== Binary ===")
print(a_binary)
print(b_binary)
print("\n")


"""a_square_root = square_root(A)
b_square_root = square_root(B)
print("=== Square Root ===")
print(a_square_root)
print(b_square_root)
print("\n")
"""

a_heron = heron(A)
b_heron = heron(B)
print("=== Heron ===")
print(a_heron)
print(b_heron)
print("\n")

a_and_b_ggt = ggt(A, B)
print("=== GGT ===")
print(f"GGT Von {A} und {B} ist {a_and_b_ggt}")
print("\n")

a_prime_number = prime_number_faster(A, True)
b_prime_number = prime_number_faster(B, True)
print("=== Prime Number ===")
print(A)
print_dict(a_prime_number)
print("\n" + str(B))
print_dict(b_prime_number)
print("\n")

a_and_b_prime_number_to = prime_numbers_faster(A, B)
print("=== Prime Number From To ===")
print(f"Von {A} zu {B}")
print(a_and_b_prime_number_to)
print("\n")

a_next_prime_number = next_prime_number(A)
b_next_prime_number = next_prime_number(B)
print("=== Next Prime Number ===")
print(f"{A} -> {a_next_prime_number}")
print(f"{B} -> {b_next_prime_number}")
print("\n")
