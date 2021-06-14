
class Rectangle:
    def __init__(self, length: int, width: int):
        self.width = width
        self.length = length

    def area(self) -> int:
        return self.length * self.width

    @staticmethod
    def name() -> str:
        return 'rectangle'


class Square(Rectangle):
    def __init__(self, length: int):
        super().__init__(length, length)

    @staticmethod
    def name() -> str:
        return 'square'


if __name__ == '__main__':
    rectangle = Rectangle(2, 3)
    print(rectangle.name(), rectangle.area())

    square = Square(5)
    print(square.name(), square.area())