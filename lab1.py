import math
import unittest

class Shape:
    def __init__(self, color="red"):
        self.color = color

    def get_color(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, width, height, color="red"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # Adding a New method: Perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius, color="red"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    # Adding a New method: Circumference of the circle
    def circumference(self):
        return 2 * math.pi * self.radius

# Unit tests for Rectangle
class TestRectangle(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

    def test_area_with_different_values(self):
        rect = Rectangle(3, 9)
        self.assertEqual(rect.area(), 27)

    # Unit test for the new perimeter method
    def test_perimeter(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.perimeter(), 14)

    def test_perimeter_with_different_values(self):
        rect = Rectangle(5, 7)
        self.assertEqual(rect.perimeter(), 24)

# Unit tests for Circle
class TestCircle(unittest.TestCase):

    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25, places=5)

    # Unit test for the new circumference method
    def test_circumference(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.circumference(), 2 * math.pi * 5, places=5)

    def test_circumference_with_different_values(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.circumference(), 2 * math.pi * 3, places=5)

if __name__ == "__main__":
    unittest.main()


#Miles
#Nana Kwame