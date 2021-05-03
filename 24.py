# Write a program to find the factors of a number

number = int(input('Enter a number: '))

factors = []

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

print(f'The factors of the number {number} are: ')
print(factors)