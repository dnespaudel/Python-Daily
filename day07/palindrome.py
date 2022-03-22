# Palindrome Number

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")