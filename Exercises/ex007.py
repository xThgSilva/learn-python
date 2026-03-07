"""
Create a function that:
- Receives a list
- Returns the sum of its elements
- Without using sum()
"""
numbers = [1,2,3,4,5,6,7,8,9,10]

def sum_list(array):
    total = 0

    for num in array:
        total += num

    return total

print(f"List: {numbers}")
print(f"Sum of elements: {sum_list(numbers)}")
