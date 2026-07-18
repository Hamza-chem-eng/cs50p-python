def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass


def temp_sensor(temperature):
    if temperature > 500:
        raise Exception("Temperature is too high")
    else:
        return temperature


def pressure_sensor(pressure):
    if pressure > 100:
        raise Exception("Pressure is too high")
    else:
        return pressure


def flow_sensor(flow):
    if flow < 0:
        raise Exception("Flow is too low")
    else:
        return flow


def sensor(temp, pressure, flow):
    while True:
        try:
            temp_sensor(temp)
            break
        except Exception as e:
            print(e)
    while True:
        try:
            pressure_sensor(pressure)
            break
        except Exception as e:
            print(e)

    while True:
        try:
            flow_sensor(flow)
            break
        except Exception as e:
            print(e)
    return "all is normal"


temp = get_number("Enter a temperature in degrees Celsius: ")
pressure = get_number("Enter a pressure : ")
flow = get_number("Enter a flow : ")
print(sensor(temp, pressure, flow))
