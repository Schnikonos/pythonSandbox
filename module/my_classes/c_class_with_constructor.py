
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    john = Person('John', 24)
    print(john.name, john.age)