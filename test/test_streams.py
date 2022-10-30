import unittest
import requests

#py -m unittest

class TestStreams(unittest.TestCase):
    
    def test_star_wars_reachable(self):
        response = requests.get("https://swapi.dev/api/people")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()