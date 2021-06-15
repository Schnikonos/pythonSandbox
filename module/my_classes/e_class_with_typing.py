
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


if __name__ == '__main__':
    john = Person('john', 24)
    print('john:', john.name, john.age)

    doe = Person(42, 'unknown')
    print('doe:', doe.name, doe.age)
