import unittest
from scaling import ScalingApp

class TestScalingApp(unittest.TestCase):
    def test_scaling(self):
        self.assertEqual(ScalingApp._calculate_scaled_value(5, 0, 10, 0, 100), 50)
        self.assertEqual(ScalingApp._calculate_scaled_value(0, 0, 10, 0, 100), 0)
        self.assertEqual(ScalingApp._calculate_scaled_value(10, 0, 10, 0, 100), 100)
        self.assertEqual(ScalingApp._calculate_scaled_value(2.5, 0, 10, 0, 100), 25)

if __name__ == "__main__":
    unittest.main()
