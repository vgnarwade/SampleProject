""" This is sample views file"""


# updated file

def add_numbers(a,b):
    res = int(a)+int(b)
    print(f"{a}+{b}= ", res)
    return res


def subtract_numbers(a,b):
    res = a-b
    print(f"{a}-{b}= ", res)
    return res


def multiply_numbers(a,b):
    res = a*b
    print(f"{a}*{b}= ", res)
    return res


def division_numbers(a,b):
    if b==0:
        print("Can't divide by Zero, provide valid number")
    else:
        res = a/b
        print(f"{a}/{b}= ", res)
        return res


if __name__ == "__main__":
    add_numbers(2,3)
    subtract_numbers(40, 20)
    multiply_numbers(12, 10)
    division_numbers(10,5)