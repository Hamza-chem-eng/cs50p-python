class Element:
    def __init__(self,symbol, atomic_number):
        self.symbol = symbol 
        self.atomic_number = atomic_number
    def __str__(self):
        return f"{self.symbol} (atomic {self.atomic_number})"

element = Element("H",1)
print(element)