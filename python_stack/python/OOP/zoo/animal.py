class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10