import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_assertions(self):
        self.assertTrue(1 < 2)
        self.assertFalse(1 > 2)
        self.assertIsNone(None)
        self.assertIsNotNone(1)
        self.assertIn(1, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
        self.assertIsInstance(1, int)

    def test_list_equality(self):
        self.assertListEqual([1, 2], [1, 2])

    def test_dict_equality(self):
        self.assertDictEqual({"a": 1}, {"a": 1})

class TestString(unittest.TestCase):
    def setUp(self):
        self.text = "hello world"

    def test_upper(self):
        self.assertEqual(self.text.upper(), "HELLO WORLD")

    def test_split(self):
        self.assertEqual(self.text.split(), ["hello", "world"])

if __name__ == "__main__":
    unittest.main(verbosity=2)