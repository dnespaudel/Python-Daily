# Fibonacci Sequence

def fibo(n_terms):
    n1 = 0
    n2 = 1
    count = 0

    if n_terms <= 0:
        print("Please! Enter a positive integer.")

    elif n_terms == 1:
        print("Fibonacci Sequence:", n1)

    else:
        while count < n_terms:
            print(n1, end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


n_terms = int(input("How many terms do you want to display?"))
fibo(n_terms)