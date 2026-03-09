"""
Create a function that shows the current year and asks
the user's birth year, then shows:
- Current age
- How many years until turning 100
"""
from datetime import date
birth_year = int(input("What year were you born? "))

print("=" * 20)
print("Calculating age...")
print("=" * 20)

current_year = date.today().year
age = current_year - birth_year

print(f"Current year: {current_year}.")
print(f"You are turning {age} this year.")
print(f"You have {100 - age} years left to turn 100.")
