from unittest import TestCase, main
from module.my_classes.b_basic_class import Person


class TestBasicClass(TestCase):
    def test_default_init(self):
        person = Person()
        self.assertEqual(person.name, 'unknown')
        self.assertEqual(person.age, 42)

    def test_set_value(self):
        person = Person()
        person.name = 'John'
        person.age = 24

        self.assertEqual(person.name, 'John')
        self.assertEqual(person.age, 24)


if __name__ == '__main__':
    main()
