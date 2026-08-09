class Vehicle:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

class Car(Vehicle):

    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type= fuel_type

    def display(self):
        super().display()
        print("Fuel_type:", self.fuel_type)


class Bike(Vehicle):

    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display(self):
        super().display()
        print("Engine_cc:", self.engine_cc)
        


car= Car("Tyota", "Canry", "Petrol")
bike= Bike("Yamaha", "R15", 155)


car.display()
bike.display()

print(isinstance(car, Car))
print(isinstance(car, Vehicle))

print(issubclass(Car, Vehicle))
print(issubclass(Bike, Vehicle))