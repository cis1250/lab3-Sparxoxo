while True:
    num = input("How many terms of the Fibonacci sequence do you want? ")
    if num.isdigit() and int(num) > 0:  
        n = int(num)
        break
    else:
        print("Please enter a positive integer.")

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
