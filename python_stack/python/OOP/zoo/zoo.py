from lion import Lion
from bear import Bear
from snake import Snake

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self):
        for animal in self.animals:
            animal.feed()

    def display_all(self):
        print(self.name)
        for animal in self.animals:
            animal.display_info()
            print('-------------------------')


zoo = Zoo("Adel's Zoo")

zoo.add_animal(Lion("Simba", 5))
zoo.add_animal(Snake("Trump", 3))
zoo.add_animal(Bear("Putin", 7))

print("Before Feeding:")
zoo.display_all()

zoo.feed_all()

print("-------------------------------------")
print("After Feeding:")
zoo.display_all()