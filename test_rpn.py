import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
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
		
print("Testing Addition:\n")
result_one = rpn.calculate('1 1 +')
if result_one == 2:
	print(Fore.RED + "Addition passed YO\n")

print("Testing Subtraction:\n")
result_two = rpn.calculate('5 3 -')
if result_two == 2:
	print(Fore.RED + "Subtraction passed YO YO\n")

print("Testing Exponentiation:\n")
result_three = rpn.calculate('5 2 ^')
if result_three == 25:
	print(Fore.RED + "Exponentiation passed YO YO YO\n")
