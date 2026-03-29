class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        return self.name + " is eating"

    def sleep(self):
        return self.name + " is sleeping"

    def speak(self):
        return self.name + " makes a sound"

    def __str__(self):
        return "Name is: " + self.name + ", Age is: " + str(self.age) + ", Color is: " + self.color


class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        return self.name + " says woof"

    def run(self):
        return self.name + " is running"

    def __str__(self):
        return "Dog's name is: " + self.name + ", Age is: " + str(self.age) + ", Color is: " + self.color + ", Breed is: " + self.breed


class Cat(Animal):
    def __init__(self, name, age, color, indoor):
        super().__init__(name, age, color)
        self.indoor = indoor

    def speak(self):
        return self.name + " says meow"

    def climb(self):
        return self.name + " is climbing"

    def __str__(self):
        return "Cat's name is: " + self.name + ", Age is: " + str(self.age) + ", Color is: " + self.color + ", Indoor is: " + str(self.indoor)