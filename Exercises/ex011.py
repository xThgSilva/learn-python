"""
Create a function that:
Receives a number and returns:
- "positive" if it is greater than 0
- "negative" if it is less than 0
- "zero" if it is 0
"""
def classify_number(num):

    if num > 0:
        return f"{num} is positive"
    elif num < 0:
        return f"{num} is negative"
    else:
        return f"{num} is zero"

print(classify_number(10))
print(classify_number(-10))
print(classify_number(0))
