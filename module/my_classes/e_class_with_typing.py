from typing import List, Dict, Tuple


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


tuple_person: Tuple[int, str, bool, Person] = (1, 'deux', True, Person('John', 24))
list_person: List[Person] = [Person('John', 24), Person('Doe', 22)]
dict_person: Dict[str, Person] = {'pers1': Person('John', 24), 'pers2': Person('Doe', 22)}


def get_name(person: Person) -> str:
    return person.name


if __name__ == '__main__':
    john = Person('john', 24)
    print('john:', john.name, john.age)

    doe = Person(42, 'unknown')
    print('doe:', doe.name, doe.age)

    print(tuple_person[3].name, list_person[1].name, dict_person['pers2'].name, get_name(list_person[0]))
