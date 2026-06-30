import random


def get_min_max():
    while True:
        try:
            min_temp = int(input("Enter minimum temp: "))
            break
        except ValueError:
            continue
    while True:
        try:
            max_temp = int(input("Enter max temp: "))
            if min_temp > max_temp:
                raise ValueError
            break
        except ValueError:
            continue
    return min_temp, max_temp


def main():
    mi, ma = get_min_max()
    c_temp = random.randint(mi, ma)
    if c_temp < mi + 30:
        return f"Temp is too low:{c_temp}"
    elif c_temp > ma + 20:
        return f"Temp is too high:{c_temp}"
    else:
        return f"normal temp :{c_temp}"


print(main())
