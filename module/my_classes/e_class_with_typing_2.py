from typing import Tuple, List, Dict, Callable, TypeVar, Generic

from module.my_classes.e_class_with_typing import Person


def get_name(person: Person) -> str:
    return person.name


# usual typings
tuple_person: Tuple[int, str, bool, Person] = (1, 'deux', True, Person('John', 24))
list_person: List[Person] = [Person('John', 24), Person('Doe', 22)]
dict_person: Dict[str, Person] = {'pers1': Person('John', 24), 'pers2': Person('Doe', 22)}
func_person: Callable[[Person], str] = get_name

# generic type
T = TypeVar('T')


class Vector(Generic[T]):
    def __init__(self, el: T):
        pass

    def add(self, el: T):
        pass

    def pop(self) -> T:
        pass


int_vector = Vector(123)
int_vector.add('str')


if __name__ == '__main__':
    john = Person('john', 24)
    print('john:', john.name, john.age)

    doe = Person(42, 'unknown')
    print('doe:', doe.name, doe.age)

    print(tuple_person[3].name, list_person[1].name, dict_person['pers2'].name, get_name(list_person[0]))