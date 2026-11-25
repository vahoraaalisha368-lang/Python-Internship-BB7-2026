class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C!")
        self._celsius = value

    @property
    def kelvin(self):
        return self._celsius + 273.15

t = Temperature(25)
print(f"Celsius: {t.celsius}")
print(f"Kelvin: {t.kelvin}")

try:
    t2 = Temperature(-300)
except ValueError as e:
    print(f"Error: {e}")