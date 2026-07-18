def get_int():
    while True:
        try:
            return int(input("input an integer: "))
        except ValueError:
            pass


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"


def get_op(op):
    if op not in ["+", "-", "*", "/"]:
        raise Exception("Invalid operation")
    return op


def calculate(a, b, op):
    if op == "/":
        return divide(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "+":
        return add(a, b)


a = get_int()
while True:
    try:
        op = get_op(input("input an operation: "))
        break
    except Exception as e:
        print(e)
b = get_int()
print(calculate(a, b, op))
