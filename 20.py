# Write a program to check if a number is odd or even

number = int(input('Enter a number: '))

if number % 2 == 0:
    print(f'The number {number} is even')
else:
    print(f'The number {number} is odd')

print (f'The number {number} is even' if number % 2 == 0 else 'The number {number} is odd')