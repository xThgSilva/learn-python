"""
Create a function that:
- Receives a list
- Receives an optional parameter even=True
- If even=True, return only even numbers
- If even=False, return only odd numbers
"""
numbers = [1,2,3,4,5,6,7,8,9,10]

def filter_numbers(lst, even=True):
    new_list = []

    for num in lst:
        if even and num % 2 == 0:
            new_list.append(num)
        elif not even and num % 2 == 1:
            new_list.append(num)

    return new_list

print(filter_numbers(numbers))
print(filter_numbers(numbers, even=False))
