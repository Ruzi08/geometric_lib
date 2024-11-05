import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    test_cases = [
        (0, 0, 0),
        (1, 1, 4),
        (2, 4, 8),
        (3, 9, 12),
        (1000000, 1000000000000, 4000000)
    ]

    def test_area(self):
        for test_case in self.test_cases:
            res = area(test_case[0])
            expected = test_case[1]
            self.assertEqual(res, expected, f"\nTest: square.area({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_area(self):
        negative_radius = -1
        try:
            area(negative_radius)
            self.fail(f"ValueError not raised for test: square.area({negative_radius})")
        except ValueError:
            pass

    def test_perimeter(self):
        for test_case in self.test_cases:
            res = perimeter(test_case[0])
            expected = test_case[2]
            self.assertEqual(res, expected, f"\nTest: square.perimeter({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_perimeter(self):
        negative_radius = -1
        try:
            perimeter(negative_radius)
            self.fail(f"ValueError not raised for test: square.perimeter({negative_radius})")
        except ValueError:
            pass
