# Return the largest item from a list

numbers = [12, 55, 30, 23, 10, 67, 0, -5]
max_num = numbers[0]

for i in numbers[1:]:
    if i > max_num:
        max_num = i

print(max_num)
print(max(numbers))
print(min(numbers))