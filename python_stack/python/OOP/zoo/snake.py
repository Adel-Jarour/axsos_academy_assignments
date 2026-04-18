from animal import Animal

class Snake(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.poison = 90

    def feed(self):
        self.health += 10
        self.happiness += 5