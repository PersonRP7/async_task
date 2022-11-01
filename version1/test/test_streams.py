import sys

sys.path += ['./']
#Allows the tests to be run from the root directory, as python doesn't treat
#the current working directory as a package.

import unittest
import requests
from math import floor
from streams import Stream


#py -m unittest

class TestStreams(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # base_stream = Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler")
        base_stream = Stream("https://swapi.dev/api/people", 
        "https://baconipsum.com/api/?type=meat-and-filler",
        "https://pokeapi.co/api/v2/pokemon"
        )
        star_wars = base_stream.list_getter("star_wars_list")
        pork = base_stream.list_getter("pork_list")

        cls.base_stream = base_stream
        cls.star_wars = star_wars
        cls.pork = pork
    
    def test_star_wars_reachable(self):
        response = requests.get("https://swapi.dev/api/people")
        self.assertEqual(response.status_code, 200)

    def test_pork_reachable(self):
        response = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
        self.assertEqual(response.status_code, 200)


    def test_star_wars_list_populated(self):
        
        self.assertGreater(len(self.star_wars), 0)
    
    def test_pork_list_populated(self):

        self.assertGreater(len(self.pork), 0)

    def test_reduce_list_size(self):
        ls = [1, 2, 3, 4, 5]
        ls_reduced = self.base_stream.reduce_list_size(ls)
        self.assertEqual(len(ls_reduced), 2)

    
        
if __name__ == '__main__':
    unittest.main()