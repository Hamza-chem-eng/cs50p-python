import re
def find_cas_numbers(text):
    cas_numbers = re.findall(r"\b[0-9]{2,7}-[0-9]{2}-[0-9]\b",text)
    return cas_numbers

if __name__ == "__main__":
    print(find_cas_numbers(input()))