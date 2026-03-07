"""
Create a function that:
- Receives a list
- Returns the highest and lowest numbers
- The sum
- The average
- Without using max(), min(), sum() or average()
"""
numbers = [3,7,2,9,5]

def analyze_list(array):
    if len(array) == 0:
        print("Invalid list")
        return None, None, None, None

    highest = array[0]
    lowest = array[0]
    total = 0

    for num in array:
        total += num

        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    average = total / len(array)

    return highest, lowest, total, average


highest, lowest, total, average = analyze_list(numbers)

print("Problem data:")
print(f"List: {numbers}")
print(f"Highest number: {highest}")
print(f"Lowest number: {lowest}")
print(f"Sum: {total}")
print(f"Average: {average}")
