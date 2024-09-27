


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"name: {self.name}, age {self.age}")


class Dog(Animal):

    def __init__(self, sname):
        self.sname = sname
        self.Animal.__init__(self.name, self.age)

print("yest")


x = Animal("cat", 2.5)
x.print_details()