from functools import total_ordering
from typing import List, Set


@total_ordering   # allows, when defining lt and eq, to have a definition for neq, gt, gte and lte
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{} ({})'.format(self.name, self.age)

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()


class Club:
    def __init__(self, type_group: str, persons: List[Person]):
        self.persons = persons
        self.type_group = type_group

    def __str__(self):
        self.persons.sort()  # uses __lt__ by default
        return 'orderedByName: {} {}'.format(self.type_group, self.persons)

    def custom_print(self):
        self.persons.sort(key=lambda x: x.age)
        print('orderedByAge:', self.type_group, self.persons)


if __name__ == '__main__':
    club = Club('foot', [Person('john', 20), Person('doe', 24), Person('foo', 19)])
    print(club)

    club.custom_print()

    # Set uses __eq__ and __hash__
    person_set: Set[Person] = {Person('john', 20), Person('john', 24), Person('doe', 20)}
    print(person_set)