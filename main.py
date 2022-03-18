# Problem 25:
#     1000-digit Fibonacci Number
#
# Description:
#     The Fibonacci sequence is defined by the recurrence relation:
#         F_n = F_{n−1} + F_{n−2}, where F_1 = 1 and F_2 = 1.
#
#     Hence the first 12 terms will be:
#
#         F_1  =   1
#         F_2  =   1
#         F_3  =   2
#         F_4  =   3
#         F_5  =   5
#         F_6  =   8
#         F_7  =  13
#         F_8  =  21
#         F_9  =  34
#         F_10 =  55
#         F_11 =  89
#         F_12 = 144
#
#     The 12th term, F_12, is the first term to contain three digits.
#
#     What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from math import ceil, log10, sqrt

# Golden mean, used to calculate exact Fibonacci values
PHI = (1 + sqrt(5)) / 2


def main(d):
    """
    Returns the index of the first term in the Fibonacci sequence to contain `d` digits,
        where F_1 = F_2 = 1,
        and F_n = F_{n−1} + F_{n−2} for n > 2.

    Args:
        d (int): Natural number

    Returns:
        Index of first Fibonacci number having `d` digits.
    """
    assert type(d) == int and d > 0
    global PHI

    # Reasoning:
    #     F_n >= 10 ** (d - 1)
    #     round(PHI ** n / sqrt(5)) >= 10 ** (d - 1)
    #     PHI ** n / sqrt(5) >= 10 ** (d - 1) - 0.5
    #     PHI ** n >= sqrt(5) * 10 ** (d - 1) - 0.5
    #     log(PHI ** n) >= log(sqrt(5) * 10 ** (d - 1) - 0.5)
    #     n * log(PHI) >= log(sqrt(5) * 10 ** (d - 1) - 0.5)
    #     n >= log(sqrt(5) * 10 ** (d - 1) - 0.5) / log(PHI)
    #     n >= log(sqrt(5) * 10 ** (d - 1)) / log(PHI)
    #     n >= [log(sqrt(5)) + log(10 ** (d - 1))] / log(PHI)
    #     n >= [0.5 * log(5) + log(10 ** (d - 1))] / log(PHI)
    #     n >= [0.5 * log10(5) + log10(10 ** (d - 1))] / log10(PHI)
    #     n >= [0.5 * log10(5) + (d-1)] / log10(PHI)

    return ceil((0.5 * log10(5) + (d - 1)) / log10(PHI))


if __name__ == '__main__':
    digits = int(input('Enter a natural number: '))
    index = main(digits)
    print('Index of first Fibonacci number to have {} digits:'.format(digits))
    print('  {}'.format(index))
