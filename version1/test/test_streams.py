import sys
sys.path += ['./']
#Allows the tests to be run from the root directory, as python doesn't treat
#the current working directory as a package.

import unittest
import requests
from streams import Stream


#py -m unittest

class TestStreams(unittest.TestCase):
    
    def test_star_wars_reachable(self):
        response = requests.get("https://swapi.dev/api/people")
        self.assertEqual(response.status_code, 200)

    def test_pork_reachable(self):
        response = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
        self.assertEqual(response.status_code, 200)

    def test_star_wars_list_populated(self):
        stream = Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler")
        self.assertGreater(len(stream.star_wars_list), 0)
    
    def test_pork_list_populated(self):
        stream = Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler")
        self.assertGreater(len(stream.pork_list), 0)

if __name__ == '__main__':
    unittest.main()