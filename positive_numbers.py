# Program to print all positive numbers in a list

# First list
list1 = [12, -7, 5, 64, -14]
positive1 = [num for num in list1 if num > 0]
print("Input: list1 =", list1)
print("Output:", ", ".join(map(str, positive1)))

# Second list
list2 = [12, 14, -95, 3]
positive2 = [num for num in list2 if num > 0]
print("\nInput: list2 =", list2)
print("Output:", positive2)
