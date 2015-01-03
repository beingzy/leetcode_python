import unittest
from reverse_integer import Solution

s = Solution()

class TestUM(unittest.TestCase):

	def setUp(self):
		pass

	def test_123(self):
		self.assertEqual(s.reverse(123), 321)

	def test_m123(self):
		self.assertEqual(s.reverse(-321), -123)

	def test_100(self):
		self.assertEqual(s.reverse(100), 1)

if __name__ == '__main__':
	unittest.main()

