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

class TestRectangle(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

    def test_area_with_different_values(self):
        rect = Rectangle(3, 9)
        self.assertEqual(rect.area(), 27)

if __name__ == "__main__":
    unittest.main()

#Miles
#Nana Kwame