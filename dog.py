class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking")


d1 = Dog("Tommy")
d1.bark()