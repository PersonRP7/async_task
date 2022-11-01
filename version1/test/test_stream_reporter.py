import sys

sys.path += ['./']
#Allows the tests to be run from the root directory, as python doesn't treat
#the current working directory as a package.

import unittest
from unittest.mock import patch
from stream_reporter import send_error_email


#py -m unittest

class TestStreams(unittest.TestCase):

    @patch('builtins.print')
    def test_send_error_email(self, mock_print):
        send_error_email("msg")
        mock_print.assert_called_with('Sending error email with msg')

    
        
if __name__ == '__main__':
    unittest.main()