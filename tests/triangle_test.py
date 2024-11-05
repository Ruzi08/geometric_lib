import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    test_cases = [
        (1, 2, 2, 1, 5),
        (2, 5, 5, 5, 12),
        (3, 4, 6, 6, 13),
        (3, 5, 7.5, 7.5, 15.5),
        (1000000, 1000000, 1000000, 500000000000, 3000000)
    ]

    def test_area(self):
        for test_case in self.test_cases:
            res = area(test_case[0], test_case[1])
            expected = test_case[3]
            self.assertEqual(res, expected, f"\nTest: triangle.area({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_area(self):
        negative_radius = (-1, 0)
        try:
            area(negative_radius[0], negative_radius[1])
            self.fail(f"ValueError not raised for test: triangle.area{negative_radius}")
        except ValueError:
            pass

    def test_perimeter(self):
        for test_case in self.test_cases:
            res = perimeter(test_case[0], test_case[1], test_case[2])
            expected = test_case[4]
            self.assertEqual(res, expected, f"\nTest: triangle.perimeter({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_perimeter(self):
        negative_radius = (-1, 0, 0)
        try:
            perimeter(negative_radius[0], negative_radius[1], negative_radius)
            self.fail(f"ValueError not raised for test: triangle.perimeter{negative_radius}")
        except ValueError:
            pass
