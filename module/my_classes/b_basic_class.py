

class Person:
    name = 'unknown'
    age = 42


if __name__ == '__main__':
    first_person = Person()
    print(first_person.name, first_person.age)

    first_person.age = 24
    first_person.name = 'John'
    print(first_person.name, first_person.age)
