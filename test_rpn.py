import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
                print("Addition passed\n")
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
                print("Subtraction passed\n")
        def test_carat(self):
                result = rpn.calculate('5 2 ^')
                self.assertEqual(25, result)
		print("Exponentiation passed\n")
