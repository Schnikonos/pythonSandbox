
class Person:
    def __init__(self, name='unknown', age=42):
        self.name = name
        self.age = age


if __name__ == '__main__':
    unknown = Person()
    print('unknown:', unknown.name, unknown.age)

    john = Person('John')
    print('john:', john.name, john.age)

    doe = Person(age=24)
    print('doe:', doe.name, doe.age)
