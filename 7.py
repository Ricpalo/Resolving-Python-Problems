# Find the factorial of any number

num = int(input('Enter a number: '))

# First Method

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(factorial)

# Second Method

def fact(value):
    if value == 1:
        return 1
    else:
        return value * fact(value - 1)

print(fact(num))