import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    test_cases = [
        (0, 0, 0),
        (1, 3.141592653589793, 6.283185307179586),
        (2, 12.566370614359172, 12.566370614359172),
        (3, 28.274333882308138, 18.84955592153876),
        (1000000, 3141592653589.793, 6283185.307179586)
    ]

    def test_area(self):
        for test_case in self.test_cases:
            res = area(test_case[0])
            expected = test_case[1]
            self.assertEqual(res, expected, f"\nTest: circle.area({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_area(self):
        negative_radius = -1
        try:
            area(negative_radius)
            self.fail(f"ValueError not raised for test: circle.area({negative_radius})")
        except ValueError:
            pass

    def test_perimeter(self):
        for test_case in self.test_cases:
            res = perimeter(test_case[0])
            expected = test_case[2]
            self.assertEqual(res, expected, f"\nTest: circle.perimeter({test_case[0]})\nexpected: {expected}, got: {res}")

    def test_negative_perimeter(self):
        negative_radius = -1
        try:
            perimeter(negative_radius)
            self.fail(f"ValueError not raised for test: circle.perimeter({negative_radius})")
        except ValueError:
            pass
