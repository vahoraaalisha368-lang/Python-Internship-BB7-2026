class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Top Speed: {self.top_speed} km/h")

s = SportsCar("Lamborghini", "Huracan", 325)
s.show_info()