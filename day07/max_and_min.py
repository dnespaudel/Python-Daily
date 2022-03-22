# Maximum and Minimum number in list

list = []
num = int(input("Enter the number of elements: "))
for i in range(0, num):
    element = int(input())
    list.append(element)

max = list[0]
min = list[0]

for i in range(1, num):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]

print("The maximum number in list is:", max)
print("The minimum number in list is:", min)