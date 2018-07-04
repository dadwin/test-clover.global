import unittest

from palindrome import get_longest_palindrome


class TestPalindrome(unittest.TestCase):
    def test_empty(self):
        r = get_longest_palindrome("")
        self.assertEqual(r, {""})

    def test_one_char(self):
        r = get_longest_palindrome("a")
        self.assertEqual(r, {"a"})

    def test_two_char(self):
        r = get_longest_palindrome("aa")
        self.assertEqual(r, {"aa"})

    def test_three_char1(self):
        r = get_longest_palindrome("aaa")
        self.assertEqual(r, {"aaa"})

    def test_three_char2(self):
        r = get_longest_palindrome("aba")
        self.assertEqual(r, {"aba"})

    def test_four_char1(self):
        r = get_longest_palindrome("daad")
        self.assertEqual(r, {"daad"})

    def test_four_char2(self):
        r = get_longest_palindrome("adad")
        self.assertEqual(r, {"ada", "dad"})

    def test_four_char3(self):
        r = get_longest_palindrome("abdd")
        self.assertEqual(r, {"dd"})

    def test_one_palindrome(self):
        inputs = ["radar", "aradar", "radara", "cdavfaradar"]
        for i in inputs:
            r = get_longest_palindrome(i)
            self.assertEqual(r, {"radar"})

    def test_two_palindromes(self):
        inputs = ["radarsoon", "aradarsooncf", "radarasoon", "cdavfasoonradar"]
        for i in inputs:
            r = get_longest_palindrome(i)
            self.assertEqual(r, {"radar"})

    def test_two_equal_palindromes(self):
        inputs = ["radarlevel", "aradarlevelcf", "radaraslevel", "cdavfalevelradar"]
        for i in inputs:
            r = get_longest_palindrome(i)
            self.assertEqual(r, {"radar", "level"})

    def test_big_string1(self):
        r = get_longest_palindrome("amanaplanacanalpanama")
        self.assertEqual(r, {"amanaplanacanalpanama"})

    def test_big_string2(self):
        r = get_longest_palindrome("1223411000amanaplanacanalpanama34513058413758762098347658294396857389423058742385467489")
        self.assertEqual(r, {"amanaplanacanalpanama"})

    def test_no_palindrome(self):
        r = get_longest_palindrome("abcdefgjhiklmnoprsqtxyz")
        self.assertEqual(r, {})
