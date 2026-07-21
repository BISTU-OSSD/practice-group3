import unittest
from calculator import calculate_weighted_score


class TestScoreCalculate(unittest.TestCase):

    def test_normal_weight(self):
        result = calculate_weighted_score([80, 90], [0.4, 0.6])
        self.assertEqual(result, 86.0)

    def test_err_length(self):
        with self.assertRaises(ValueError):
            calculate_weighted_score([70], [0.5, 0.5])


if __name__ == "__main__":
    unittest.main()
