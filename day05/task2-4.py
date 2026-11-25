class Bird:
    def fly(self):
        return "Bird is flying with wings"

class Airplane:
    def fly(self):
        return "Airplane is flying with engine"

class Drone:
    def fly(self):
        return "Drone is flying with propellers"

def make_it_fly(obj):
    print(obj.fly())

make_it_fly(Bird())
make_it_fly(Airplane())
make_it_fly(Drone())