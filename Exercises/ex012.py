"""
Accumulator function

Create a function that:
- Receives two numbers: start and end
- Returns the sum of all numbers between them (inclusive)
"""
def sum_interval(start, end):

    total = 0

    for num in range(start, end + 1):
        total += num

    return total

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"The sum from {start} to {end} is {sum_interval(start, end)}")
