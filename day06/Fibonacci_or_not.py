# Checking weather the entered number is Fibonacci or not

import math


def isPerfectNumber(num1):
    num2 = int(math.sqrt(num1))
    if pow(num2, 2) == num1:
        return True
    return False


def isFibonacciNumber(n):
    t1 = 5*n*n - 4
    t2 = 5*n*n + 4

    if isPerfectNumber(t1) or isPerfectNumber(t2):
        return True
    else:
        return False


x = int(input("Enter a number:"))
result = isFibonacciNumber(x)

if result:
    print("Yup! It's a Fibonacci Number.")
else:
    print("It's not a Fibonacci Number.")

