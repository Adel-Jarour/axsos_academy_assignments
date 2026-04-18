from animal import Animal

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.fur_thickness = 70

    def feed(self):
        self.health += 12
        self.happiness += 12