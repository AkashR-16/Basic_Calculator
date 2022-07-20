from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide
import unittest


class Testcalculator(unittest.TestCase):

    def test_add_case(self):
        self.assertEqual(add(1, 1), 2.0)
        self.assertEqual(add(-3, 1), -2.0)
        self.assertEqual(add(-1, -1), -2.0)

    def test_sub_case(self):
        self.assertEqual(subtract(1, 1), 0.0)
        self.assertEqual(subtract(-1, 1), -2.0)
        self.assertEqual(subtract(-3, -1), -2.0)

    def test_mul_case(self):
        self.assertEqual(multiply(3, 2), 6.0)
        self.assertEqual(multiply(-3, 2), -6.0)
        self.assertEqual(multiply(-3, -2), 6.0)
        self.assertEqual(multiply(3, 0), 0.0)

    def test_div_case(self):
        self.assertEqual(divide(4, 2), 2.0)
        self.assertEqual(divide(-4, 2), -2.0)
        self.assertEqual(divide(0, 2), 0.0)



if __name__ == '__main__':
    unittest.main()
