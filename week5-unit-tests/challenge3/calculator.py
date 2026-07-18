def calculate_concentration(mass , volum):
    if volum == 0:
        raise ValueError("Volume cannot be zero")
    elif volum < 0 :
        raise ValueError("there is no negative volum")  
    elif mass < 0 :
        raise ValueError("there is no negative mass ")
    else:
        return mass / volum