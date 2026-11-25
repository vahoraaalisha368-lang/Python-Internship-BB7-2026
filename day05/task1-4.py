class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Salary increased to {self.__salary}")
        else:
            print(f"Error: Salary can only increase! Current: {self.__salary}, Tried: {new_salary}")

e = Employee("Alisha", 50000)
print(e.get_salary())

e.set_salary(60000)
print(e.get_salary())

e.set_salary(40000)
print(e.get_salary())