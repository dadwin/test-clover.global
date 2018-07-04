import unittest
import coins


class Test1(unittest.TestCase):
    def test_no_coins(self):
        r = coins.exchange([], 1)
        self.assertTrue(r is None)

        r = coins.exchange([], 43)
        self.assertTrue(r is None)

    def test_zero_sum(self):
        r = coins.exchange([1], 0)
        self.assertTrue(r is None)

        r = coins.exchange([5], 0)
        self.assertTrue(r is None)

    def test_one_coin1(self):
        r = coins.exchange([1], 1)
        self.assertTrue(r is not None)
        self.assertEqual(r[0], 1)
        combinations = r[1]
        self.assertEqual(len(combinations), 1)

        actual_combinations = {tuple(m) for m in combinations}
        expected_combinations = {(1,)}
        self.assertEqual(actual_combinations, expected_combinations)

    def test_one_coin2(self):
        r = coins.exchange([1], 6)
        self.assertTrue(r is not None)
        self.assertEqual(r[0], 6)
        combinations = r[1]
        self.assertEqual(len(combinations), 1)

        actual_combinations = {tuple(m) for m in combinations}
        expected_combinations = {(6,)}
        self.assertEqual(actual_combinations, expected_combinations)

    def test_one_coin3(self):
        r = coins.exchange([9], 27)
        self.assertTrue(r is not None)
        self.assertEqual(r[0], 3)
        combinations = r[1]
        self.assertEqual(len(combinations), 1)

        actual_combinations = {tuple(m) for m in combinations}
        expected_combinations = {(3,)}
        self.assertEqual(actual_combinations, expected_combinations)

    def test_one_coin_none1(self):
        r = coins.exchange([3], 0)
        self.assertTrue(r is None)

    def test_one_coin_none2(self):
        r = coins.exchange([3], 2)
        self.assertTrue(r is None)

    def test_one_coin_none3(self):
        r = coins.exchange([56], 200)
        self.assertTrue(r is None)

    def test1(self):
        r = coins.exchange([1, 3, 5], 11)
        self.assertTrue(r is not None)
        self.assertEqual(r[0], 3)
        combinations = r[1]
        self.assertEqual(len(combinations), 2)

        actual_mix = {tuple(m) for m in combinations}
        expected_mix = {(0, 2, 1), (1, 0, 2)}
        self.assertEqual(actual_mix, expected_mix)

    def test2(self):
        r = coins.exchange([2, 3, 5], 11)
        self.assertTrue(r is not None)
        self.assertEqual(r[0], 3)
        combinations = r[1]
        self.assertEqual(len(combinations), 1)

        actual_mix = {tuple(m) for m in combinations}
        expected_mix = {(0, 2, 1)}
        self.assertEqual(actual_mix, expected_mix)

    def test3(self):
        r = coins.exchange([4, 5], 8)
        self.assertTrue(r is not None)
        self.assertEqual(r[0], 2)
        combinations = r[1]
        self.assertEqual(len(combinations), 1)

        actual_mix = {tuple(m) for m in combinations}
        expected_mix = {(2, 0)}
        self.assertEqual(actual_mix, expected_mix)

    def test4(self):
        r = coins.exchange([4, 5], 10)
        self.assertTrue(r is not None)
        self.assertEqual(r[0], 2)
        combinations = r[1]
        self.assertEqual(len(combinations), 1)

        actual_mix = {tuple(m) for m in combinations}
        expected_mix = {(0, 2)}
        self.assertEqual(actual_mix, expected_mix)