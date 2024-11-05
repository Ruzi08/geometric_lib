import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    test_cases = [
        (0, 0, 0, 0),
        (1, 2, 2, 6),
        (2, 5, 10, 14),
        (3, 4, 12, 14),
        (1000000, 1000000, 1000000000000, 4000000)
    ]

    def test_area(self):
        for test_case in self.test_cases:
            res = area(test_case[0], test_case[1])
            expected = test_case[2]
            self.assertEqual(res, expected, f"\nTest: rectangle.area({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_area(self):
        negative_radius = (-1, 0)
        try:
            area(negative_radius[0], negative_radius[1])
            self.fail(f"ValueError not raised for test: rectangle.area{negative_radius}")
        except ValueError:
            pass

    def test_perimeter(self):
        for test_case in self.test_cases:
            res = perimeter(test_case[0], test_case[1])
            expected = test_case[3]
            self.assertEqual(res, expected, f"\nTest: rectangle.perimeter({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_perimeter(self):
        negative_radius = (-1, 0)
        try:
            perimeter(negative_radius[0], negative_radius[1])
            self.fail(f"ValueError not raised for test: rectangle.perimeter{negative_radius}")
        except ValueError:
            pass
