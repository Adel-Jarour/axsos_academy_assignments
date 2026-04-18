from animal import Animal

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.roar_power = 80

    def feed(self):
        self.health += 15
        self.happiness += 5