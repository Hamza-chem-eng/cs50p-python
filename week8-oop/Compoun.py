class Compound:
    def __init__(self,name ,mass):
        self.name = name 
        self.mass= mass 
    def __repr__(self):
        return f"{self.name} ({self.mass}g)"
    @property 
    def mass (self):
        return self._mass
    @mass.setter
    def mass (self,mass):
        if mass < 0:
            raise ValueError("the mass should be in positive")
        self._mass = mass
    def __add__(self,other):
        mix = Mixture("Mixture")
        mix.add_compoents(self)
        mix.add_compoents(other)
        return mix

class Mixture(Compound):
    def __init__(self,name,mass = 0 ):
        super().__init__(name,mass)
        self.components = []
    def add_compoents(self,compound):
        self.components.append(compound)
        self.mass += compound.mass
c1 = Compound("NaCl", 10.0)
c2 = Compound("H2O", 5.0)

mix = c1 + c2
print(mix)             
print(mix.components)   
print(mix.components[0])   