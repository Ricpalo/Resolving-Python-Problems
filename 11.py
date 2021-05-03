# Write a program that disply all prime numbers within a range

for number in range(2, 51):
    for i in range(2, number):
        if number % i == 0:
            print(f'The number {number} is not prime')
            break  
    else:
        print(f'The number {number} is prime')