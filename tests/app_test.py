import unittest
import subprocess

class TestApp(unittest.TestCase):
	def test_output(self):
		result = subprocess.run(['python', 'app/app.py'], capture_output=True, text=True)
		self.assertEqual(result.stdout.strip(), 'Hello, World!')

if __name__ == '__main__':
	unittest.main()
