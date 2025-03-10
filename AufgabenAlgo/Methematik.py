"""
    C.Marriott
    03/03/2025
    Dateiname: Methematik.py
    Kommentar: Math Functions
"""

def calculate_GGT(A, B, T, ggT):
    if A % T != 0:
        pass
    elif B % T != 0:
        pass
    else:
        ggT = T
    T += 1
    return ggT, T


def ggt(A, B):
    T = 2
    ggT = 1

    ggT, T = calculate_GGT(A, B, T, ggT)

    while T <= A and T <= B:
        ggT, T = calculate_GGT(A, B, T, ggT)

    return ggT


def decimal_to_binary(decimal_number):
    split_number = str(decimal_number).split(".")
    first_number = int(split_number[0])
    bin_num = ""
    first_number, bin_num = __calc_decimal(first_number, bin_num)
    while first_number != 0:
        first_number, bin_num = __calc_decimal(first_number, bin_num)

    if len(split_number) == 2:
        second_number = float("0." + split_number[1])
        bin_num2 = ""
        while second_number != 0.0:
            second_number = second_number*2
            if second_number >= 1.0:
                second_number -= 1
                bin_num2 = bin_num2 + "1"
            else:
                bin_num2 = bin_num2 + "0"

        bin_num += "." + bin_num2

    return bin_num


def square_root(search_number):
    end_number = 0

    end_number, temp_number = __square_root_calc(end_number, search_number)

    while search_number > temp_number:
        end_number, temp_number = __square_root_calc(end_number, search_number)

    if temp_number == search_number:
        return end_number
    return None


def heron(rooter):
    end_number = rooter
    control_number = 1
    last_number = rooter

    while end_number > control_number:
        end_number = (end_number+control_number) / 2
        control_number = rooter / end_number

        if last_number == end_number:
            return end_number
        last_number = end_number

    return end_number


def prime_number(number):
    p = 2
    e = None

    while e is None:
        if p >= number:
            e = "Primzahl"
        else:
            tmp = number % p
            if tmp == 0:
                e = "Keine Primzahl"

        p += 1

    return e


def prime_number_faster(number:[float, int], return_divider_list:bool=False) -> dict:
    """
        Determines whether a number is prime.

        Parameters:
        ----------
        number : float | int
            The number to check for primality.
        return_divider_list : bool, optional
            If True, includes a list of tested divisors in the returned dictionary.

        Returns:
        -------
        dict
            A dictionary containing:
            - 'isPrimeNumber' (str): "Primzahl" if the number is prime, otherwise "Keine Primzahl".
            - 'dividerList' (list, optional): A list of tested divisors if `return_divider_list` is True.
    """
    p = 2
    e = None
    divider_list = []
    return_data = {}

    while e is None and p * p <= number:
        divider_list.append(p)
        if number % p == 0:
            e = "Keine Primzahl"
        else:
            p += number % p

    if return_divider_list:
        return_data["dividerList"] = divider_list

    return_data["isPrimeNumber"] = e if e else "Primzahl"
    return return_data


def prime_numbers_faster(number1:[float, int], number2:[float, int]) -> dict:
    """
        Determins all Prime Numbers that are from number1 to number2. Also works if number1 is higher than number2

        Parameters:
        ----------
        number1 : float | int
            The first number.
        number2 : float | int
            The second number.

        Returns:
        -------
        list
            A list containing:
            - all Prime Numbers from number1 to number2.
    """
    if number1 == number2:
        return prime_number_faster(number1)
    elif number1 > number2:
        return prime_numbers_faster(number2, number1)

    return_data = []
    for i in range(number1, number2+1):
        d = prime_number_faster(i)
        if d["isPrimeNumber"] == "Primzahl":
            return_data.append(i)

    return return_data


def next_prime_number(number:[float, int]) -> int:
    """
        Determines the next Prime Number after number

        Parameters:
        ----------
        number : float | int
            The first number.

        Returns:
        -------
        int
            The next Prime Number after number.
    """
    e = None
    number_counter = number + 1
    while e is None:
        test = prime_number_faster(number_counter)["isPrimeNumber"]
        if test == "Primzahl":
            e = number_counter
        else:
            number_counter += 1

    return number_counter


def __calc_decimal(number, bin_num):
    bin_num = str(number % 2) + bin_num
    number = int(number / 2)
    return number, bin_num


def __square_root_calc(end_number, search_number):
    temp_number = end_number * end_number
    if temp_number != search_number:
        end_number += 1

    return end_number, temp_number