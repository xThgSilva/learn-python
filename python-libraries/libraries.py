# Library for mathematical calculations
import math

# Library to generate random numbers
import random

# Library to work with dates
from datetime import datetime  # It is necessary to use "from datetime" to import only the datetime class

# Common usages - Math
print("=" * 25)
print("Math")
number = 4
print(f"Square root = {math.sqrt(number)}")
print(f"Power of a number (2 for example) = {math.pow(number, 2)}")
print(f"Round a number up = {math.ceil(3.1)}")
print(f"Round a number down = {math.floor(3.9)}")
print(f"Pi = {math.pi}")
print("=" * 25)

# Common usages - Random
print("=" * 25)
print("Random")
print(f"Generate a random integer within a range = {random.randint(1, 10)}")  # In this case, from 1 to 10
print(f"Generate a number between 0 and 1 = {random.random()}")
print("=" * 25)

# Common usages - Datetime
print("=" * 25)
print("Datetime")
now = datetime.now()
print(f"Current moment = {now}")  # Format: year - month - day - time
print(f"Current year = {now.year}")
print(f"Current month = {now.month}")
print("=" * 25)

# To "create" a library, just import the file or specify the method directly
print("=" * 25)
print("Creating a custom library")
import utils
from utils import multiply
print(f"Sum from utils library: {utils.sum_numbers(1, 2)}")
print(f"Multiply function imported directly: {multiply(2, 3)}")
print("=" * 25)

print("=" * 25)
print("Files and system - os")
import os
print("Current directory")
print(os.getcwd())
print("=" * 25)

print("=" * 25)
print("System interaction - sys")
import sys
print("Current Python version")
print(sys.version)
print("=" * 25)

print("=" * 25)
print("Execution time - time")
import time
print("Waiting for 5 seconds")
time.sleep(5)
print("Done! 5 seconds have passed")
