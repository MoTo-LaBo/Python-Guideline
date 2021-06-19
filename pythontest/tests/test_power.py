# 実際の開発現場でも file 作成時の title の付け方は、test_〇〇とつける
import unittest

from power import power, times


class TestMyMethod(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3
        # assert power(base, exp) == 8, "This should be 8"
        self.assertEqual(power(base, exp), 8)

    def test_times(self):
        num1 = 2
        num2 = 3
        # assert times(num1, num2) == 6, "This should be 6"
        self.assertEqual(times(num1, num2), 6)
        # context manager
        with self.assertRaises(TypeError):
            power("3", "2")

    if __name__ == "__main__":
        # test_power()
        # test_times()
        unittest.main()
