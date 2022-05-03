class MyCar:
    def __init__(self, manufacturer, model, make, transmission, color):
         self.manufacturer = manufacturer
         self.model = model 
         self.make = make 
         self.transmission = transmission 
         self.color = color 

def accelerate(self):
    print(self.manufacturer + " " + self.model + " is moving ")

def stop(self):
    print(self.manufacturer + " " + self.model + " has stopped ")

p1 = MyCar("Ford", "165", "2018", "Manual", "Blue")
print(p1.manufacturer)
print(p1.model)
print(p1.make)
print(p1.transmission)
print(p1.color)

accelerate(p1)
stop(p1)

p2 = MyCar("Aadi", "162", "2015", "Auto", "Red")
print(p2.manufacturer)
print(p2.model)
print(p2.make)
print(p2.transmission)
print(p2.color)

accelerate(p2)
stop(p2)

p3 = MyCar("Ambassador", "160", "2019", "Manual", "Black")
print(p3.manufacturer)
print(p3.model)
print(p3.make)
print(p3.transmission)
print(p3.color)

accelerate(p3)
stop(p3)

