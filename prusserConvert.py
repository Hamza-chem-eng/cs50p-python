atm_to = {"bar": 1.01325,
          "pa": 101325, "atm": 1}
to_atm = {"bar": 0.986923,
          "pa": 0.00000987, "atm": 1
          }


def get_unit(unit):
    if unit not in ["atm", "bar", "pa"]:
        raise Exception("Invalid unit")
    else:
        return unit


def get_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("invalid input")


def convert_unit(unit, number, user_want):
    unit_in_atm = to_atm[unit] * number
    unit_in_wanted = atm_to[user_want] * unit_in_atm
    return unit_in_wanted


while True:
    try:
        unit = get_unit(input("Enter unit:['atm','bar','pa']:  "))
        break
    except Exception as ex:
        print(ex)
number = get_number()
while True:
    try:
        user_want = get_unit(input("Enter unit:['atm','bar','pa']:  "))
        break
    except Exception as ex:
        print(ex)
print(convert_unit(unit, number, user_want))
