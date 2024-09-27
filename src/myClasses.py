
class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"name: {self.name}, age {self.age}")


class Dog(Animal):

    def __init__(self, name, age, numberOfLegs):
        super().__init__(self.name, self.age)
        self.numberOfLegs = numberOfLegs


class Cat(Animal):
    pass




my_container = []

dog = Dog("jh", 33, 4)
my_container.append(dog)

d2 = Dog("scheisser", 3, 4)
my_container.append(d2)






x = Animal("cat", 2.5)
my_container.append(x)

for itX in my_container:
    itX.print_details()

