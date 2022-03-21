# Factorial of given number

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)


x = int(input("Enter a number:"))
result = fact(x)
print("The factorial of", x, "is", result)