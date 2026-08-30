class Solution:
    def __init__(self,name , concentration):
        self.name = name 
        self.concentration = concentration
    def __str__(self):
        return f"{self.name} ({self.concentration} M)"
    @property
    def concentration(self):
        return self._concentration
    @concentration.setter
    def concentration(self,concentration):
        if concentration < 0 :
            raise ValueError("the concentration should be positive")
        self._concentration = concentration             

s = Solution("NaCl", 0.5)
print(s)
bad = Solution("Fake", -1)
print(bad)