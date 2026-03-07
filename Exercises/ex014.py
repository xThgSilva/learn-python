"""
Countdown

Create a function that:
- Receives a number n
- Returns a list from n down to 0
"""
def countdown(num):
    count = []

    for n in range(num, -1, -1): # It will start at number, going down to 0, decreasing by 1 each time.
        count.append(n)

    return count


counter = int(input("Enter a number for countdown: "))
print(f"Count:\n{countdown(counter)}")
