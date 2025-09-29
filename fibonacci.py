#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
# fibonacci.py

while True:
    num = input("How many terms of the Fibonacci sequence do you want? ")
    if num.isdigit() and int(num) > 0:   # check if it's a positive integer
        n = int(num)
        break
    else:
        print("Please enter a positive integer.")

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
