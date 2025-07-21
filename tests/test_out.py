import unittest
import subprocess
import sys
from io import StringIO
from unittest.mock import patch

# Assuming your script is named hello_script.py
SCRIPT_PATH = 'dreamknot.py'

class TestFileSelection(unittest.TestCase):

    def test_out(self):
        """Test the out function."""
        result = subprocess.run([sys.executable, SCRIPT_PATH, "tests\\files\\out.dk"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0) # Assuming it exits cleanly even with an argument   
        self.assertEqual(result.stdout, "Hello World!\nHello World!\n123\nabc\n()())\n()()\n\n\n\"\n\'\n")
        self.assertEqual(result.stderr, "")     

if __name__ == '__main__':
    unittest.main()