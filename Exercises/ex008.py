"""
Create a function that:
- Receives a list
- Returns the highest number in the list
- Without using max()
"""
numbers = [3,7,2,9,5]

def highest_number_list(array):
    highest = array[0]

    for num in array:
        if num > highest:
            highest = num

    return highest

print(f"Highest number in list: {highest_number_list(numbers)}")
