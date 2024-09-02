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

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


class TestRectangle(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

    def test_area_with_different_values(self):
        rect = Rectangle(3, 9)
        self.assertEqual(rect.area(), 27)

      def test_perimeter(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.perimeter(), 18)

    def test_perimeter_with_different_values(self):
        rect = Rectangle(3, 3)
        self.assertEqual(rect.perimeter(), 12)

    def test_is_square(self):
        rect = Rectangle(4, 4)
        self.assertTrue(rect.is_square())

    def test_is_not_square(self):
        rect = Rectangle(4, 5)
        self.assertFalse(rect.is_square())

if __name__ == "__main__":
    unittest.main()

#Miles
#Nana Kwame