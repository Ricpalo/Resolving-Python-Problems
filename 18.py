# Write a program to find out the average of a set of integers

def get_average(numbers):
    summation = 0

    for i in numbers:
        summation += i
    
    summation /= len(numbers)
    return summation

def get_average2(numbers):
    summation = sum(numbers)
    summation /= len(numbers)
    return summation

numbers = [1, 2, 3, 4]
print(get_average(numbers))

print(get_average2(numbers))