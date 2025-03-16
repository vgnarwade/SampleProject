""" This is sample views file"""


# updated file

def add_numbers(a,b):
    res = int(a)+int(b)
    return res


def subtract_numbers(a,b):
    res = a-b
    return res


def multiply_numbers(a,b):
    res = a*b
    return res


if __name__ == "__main__":
    add_numbers(2,3)
    subtract_numbers(40, 20)
    multiply_numbers(12, 10)