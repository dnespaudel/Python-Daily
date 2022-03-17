# If the total bill was $100, had to split between 5 people, with 15% tip you choose to make.
# Each staff would get (100 / 5) * 1.15 = $23
# Format the result to 2 decimal place = $23.00


initial_bill = ''
tip_percent = ''
staff = ''


# get the initial bill without tip
while True:
    print('What was the initial bill?')
    initial_bill = input()

    try:
        float(initial_bill)
        if float(initial_bill) < 0:
            print('The bill should be positive number. Please, Enter a valid number.')
        else:
            break
    except ValueError:
        print('Please, Enter a valid amount.')


# Get the tip_percent from customer
while True:
    print('What percentage tip do you want give? Please, Choose between 10, 12, or 15.')
    tip_percent = input()
    choices = ['10', '12', '15']
    if tip_percent not in choices:
        print('Please choose between 10, 12, or 15. Thank you!')
    else:
        break


# get the number of staffs
while True:
    print('Between how many staffs, the tip should be splitted to?')
    staff = input()

    if not staff.isdigit() or staff == 0:
        print('Please enter a valid number of staffs.')

    else:
        break

total_bill = float(initial_bill) * ((100 + int(tip_percent))/100)
amount = round(total_bill/int(staff), 2)

print('Each staff would get', amount)