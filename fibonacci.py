def get_positive_integer(prompt):
    while True:
        num = input(prompt)
        if num.isdigit() and int(num) > 0:
            return int(num)
        print("Please enter a positive integer.")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = get_positive_integer("How many terms of the Fibonacci sequence do you want? ")
fibonacci(n)
