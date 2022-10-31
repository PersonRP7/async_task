import sys

sys.path += ['./']
#Allows the tests to be run from the root directory, as python doesn't treat
#the current working directory as a package.

import unittest
import requests
from streams import Stream
from stream_operators import StreamOperators
from collections import defaultdict

class TestStreamOperators(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_stream = Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler")
        star_wars = base_stream.list_getter("star_wars_list")
        pork = base_stream.list_getter("pork_list")
        cls.star_wars = star_wars
        cls.pork = pork

    def test_vowel_comparison_returns_none(self):
        response = StreamOperators.vowel_comparison(sw = self.star_wars, p = self.pork)
        self.assertEqual(response, None)

    def test_length_comparison_returns_none(self):
        response = StreamOperators.length_comparison(sw = self.star_wars, p = self.pork)
        self.assertEqual(response, None)

    def test_counter_general_returns_integer_one(self):
        ls = ["a"]
        response = StreamOperators.counter_general(ls)
        self.assertEqual(response, 1)

    def test_count_repeat_returns_true(self):
        word = "wword"
        response = StreamOperators.count_repeat(word, "w", 2)
        self.assertEqual(response, True)

    def test_count_repeat_returns_false(self):
        word = "word"
        response = StreamOperators.count_repeat(word, "w", 2)
        self.assertEqual(response, False)


if __name__ == '__main__':
    unittest.main()

