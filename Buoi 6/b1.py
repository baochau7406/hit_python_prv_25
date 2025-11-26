class Manufacturer:
    def __init__(self, identity, location):
        self.identity= identity
        self.location= location
    def describe(self):
        return f"Identity:{self.identity}- Loaction:{self.location}"

class Device(Manufacturer):
    def __init__(self, name, price, identity, location):
        self.name= name
        self.price= price
        super().__init__(identity,location)
    def describe(self):
        return (f"Name:{self.name}- Price:{self.price} "+ super().describe())
dv1= Device("mouse", 2500, 9725, "Vienam")
print(dv1.describe())
dv2= Device("monitor", 12.5, 11, "Germany")
print(dv2.describe())