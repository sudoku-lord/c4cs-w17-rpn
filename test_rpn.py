import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		print("Testing Addition:\n")
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
		print("Addition passed YO\n")
	def test_subtract(self):
		print("Testing Subtraction:\n")
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
		print("Subtraction passed YO YO\n")
	def test_carat(self):
		print("Testing Exponentiation:\n")
		result = rpn.calculate('5 2 ^')
		self.assertEqual(25, result)
		print("Exponentiation passed YO YO YO\n")
