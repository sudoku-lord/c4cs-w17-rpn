import unittest
import rpn
import sys
from termcolor import colored, cprint
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
		
text_one = colored("Testing Addition:\n", 'red', attrs=['reverse', 'blink'])
print(text_one)
result_one = rpn.calculate('1 1 +')
if result_one == 2:
	print("Addition passed YO\n")

cprint("Testing Subtraction:\n", 'blue')
result_two = rpn.calculate('5 3 -')
if result_two == 2:
	print("Subtraction passed YO YO\n")

print("Testing Exponentiation:\n")
result_three = rpn.calculate('5 2 ^')
if result_three == 25:
	print("Exponentiation passed YO YO YO\n")
