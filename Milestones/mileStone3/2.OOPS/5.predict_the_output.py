
class Vehicle:
    def __init__(self, color):
        self.color = color


class Car(Vehicle):
    def __init__(self, color, numGears):
        self.numGears = numGears
        self.color=color


c = Car("black", 5)

print(c.color)