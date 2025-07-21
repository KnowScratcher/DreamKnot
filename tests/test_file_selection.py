import unittest
import subprocess
import sys
from io import StringIO
from unittest.mock import patch

# Assuming your script is named hello_script.py
SCRIPT_PATH = 'dreamknot.py'

class TestFileSelection(unittest.TestCase):

    def test_no_file_argument(self):
        """Test the behavior when no file argument is provided."""
        result = subprocess.run([sys.executable, SCRIPT_PATH], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)  # Expecting a clean exit in this case based on your script
        self.assertIn("No file selected, exiting", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_file_argument_provided(self):
        """Test the behavior when a file argument is provided."""
        # For this test, we'll just provide a dummy filename.
        # Your script currently doesn't *do* anything with the file,
        # so we'll just check that it doesn't exit immediately without a message.
        result = subprocess.run([sys.executable, SCRIPT_PATH, "tests\\files\\file_test.dk"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0) # Assuming it exits cleanly even with an argument
        self.assertNotIn("No file selected, exiting", result.stdout)
        self.assertEqual(result.stderr, "")

if __name__ == '__main__':
    unittest.main()