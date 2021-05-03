# Reverse the following list using for loop: list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50]
list2 = []

for i in range(-1, -len(list1) - 1, -1):
    list2.append(list1[i])

print(list2)