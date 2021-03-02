class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def __init__(self, name, color, kind, worth):
        self.name = name
        self.color = color
        self.kind = kind
        self.value = worth
    def description(self): 
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle("Car1", "Red", "Convertible", 6000)
print(car1.description())