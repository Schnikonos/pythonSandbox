
class Person:
    """Describes a person"""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_older(self):
        """Adds 1 year"""
        self._add_age(1)

    def _add_age(self, age: int):
        self.age += age

    def __str__(self):
        return 'Person: {name} {age}'.format(name=self.name, age=self.age)


if __name__ == '__main__':
    guy = Person('Guy', 20)
    print(guy)

    guy.make_older()
    print(guy)
