# LCM of given two numbers

def compute_lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        else:
            greater += 1

    return lcm


x = int(input('Enter first number:'))
y = int(input('Enter second number:'))

result = compute_lcm(x, y)
print("The LCM is:", result)
