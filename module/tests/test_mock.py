from unittest import TestCase
from unittest.mock import Mock


class ComplexClass:
    def do_stuff(self, name: str, age: int) -> str:
        return '{} {}'.format(name, age)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def my_function(self) -> str:
        return ComplexClass().do_stuff(self.name, self.age)


class TestWithMock(TestCase):
    def test_mock_do_stuff(self):
        ComplexClass.do_stuff = Mock(return_value='this is mocked !')

        person = Person('john', 24)
        res = person.my_function()

        self.assertEqual('this is mocked !', res)
        ComplexClass.do_stuff.assert_called_once_with('john', 24)
