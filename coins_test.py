import unittest
import coins2 as coins


class TestExchange(unittest.TestCase):
    def test_no_coins(self):
        combinations = coins.exchange([], 1)
        self.assertTrue(combinations is None)

        combinations = coins.exchange([], 43)
        self.assertTrue(combinations is None)

    def test_zero_sum(self):
        combinations = coins.exchange([1], 0)
        self.assertTrue(combinations is None)

        combinations = coins.exchange([5], 0)
        self.assertTrue(combinations is None)

    def test_one_coin1(self):
        combinations = coins.exchange([1], 1)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(1,)})

    def test_one_coin2(self):
        combinations = coins.exchange([1], 6)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(6,)})

    def test_one_coin3(self):
        combinations = coins.exchange([9], 27)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(3,)})

    def test_one_coin_none1(self):
        combinations = coins.exchange([3], 0)
        self.assertTrue(combinations is None)

    def test_one_coin_none2(self):
        combinations = coins.exchange([3], 2)
        self.assertTrue(combinations is None)

    def test_one_coin_none3(self):
        combinations = coins.exchange([56], 200)
        self.assertTrue(combinations is None)

    def test1(self):
        combinations = coins.exchange([5, 3, 1], 11)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 2)
        self.assertEqual(combinations, {(1, 2, 0), (2, 0, 1)})

    def test2(self):
        combinations = coins.exchange([5, 3, 2], 11)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(1, 2, 0)})

    def test3(self):
        combinations = coins.exchange([5, 4], 8)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(0, 2)})

    def test4(self):
        combinations = coins.exchange([5, 4], 10)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(2, 0)})

    def test5(self):
        combinations = coins.exchange([9, 5, 4], 11)
        self.assertTrue(combinations is None)

    def test6(self):
        combinations = coins.exchange([25, 17, 4, 3], 111)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(4, 0, 2, 1)})

    def test7(self):
        combinations = coins.exchange([5, 3, 2], 10002)
        self.assertTrue(combinations is not None)
        self.assertEqual(len(combinations), 1)
        self.assertEqual(combinations, {(2000, 0, 1)})
