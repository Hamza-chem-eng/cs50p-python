import re
def is_valid_formula(formula):
    if re.search(r"^([A-Z]{1}[a-z]?[0-9]*)+$",formula) :

        return True
    else :
        return False
if __name__ == "__main__":
    print(is_valid_formula(input()))        