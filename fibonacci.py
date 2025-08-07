# Python Program to display Fibonacci sequence up to n terms

n_terms = 5  # Set the number of terms manually
a, b = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
