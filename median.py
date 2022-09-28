"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

if(len(numbers) % 2 == 0):
	index1 = len(numbers)/2
	index2 = index1 - 1
	E_median = (numbers[int(index1)] + numbers[int(index2)])/2
	print(E_median)
else:
	index1 = len(numbers)/2
	O_median = numbers[int(index1)]
	print(O_median)
print(numbers)
