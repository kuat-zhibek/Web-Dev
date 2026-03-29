from models import Animal, Dog, Cat

animal = Animal("Animal", 5, "gray")
dog = Dog("Rex", 3, "brown", "Labrador")
cat = Cat("Cat", 2, "white", True)

animals = [animal, dog, cat]

for a in animals:
    print(a)
    print(a.eat())
    print(a.sleep())
    print(a.speak())
    if isinstance(a, Dog):
        print(a.run())
    if isinstance(a, Cat):
        print(a.climb())
    print()