import math


class Shape:
    def __init__(self, color="black"):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def __str__(self):
        return f"{self.__class__.__name__}(color={self.color}, area={self.area():.2f})"


class Circle(Shape):
    def __init__(self, radius, color="black"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, color="black"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    shapes = [
        Circle(5, color="red"),
        Rectangle(4, 6, color="blue"),
        Circle(3),
    ]

    for shape in shapes:
        print(shape)
