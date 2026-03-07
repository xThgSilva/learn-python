"""
Simple counting

Create a function that:
- Receives a number n
- Returns a list from 0 to n (inclusive)
"""
def count_numbers(num):
    count = []

    for n in range(0, num + 1):
        count.append(n)

    return count

counter = int(input("Enter a final number for counting: "))
print(f"Count:\n{count_numbers(counter)}")
