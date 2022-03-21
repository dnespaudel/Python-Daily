# HCF of given two numbers

def compute_hcf(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = compute_hcf(x, y)

print("The HCF is:", result)
