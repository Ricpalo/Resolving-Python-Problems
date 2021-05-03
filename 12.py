# Given a range of the first 10 numbers, iterate from the start number to the end number
# In each iteration print the sum of the current number and previous numbers

for i in range(1, 11):
    summation = 0

    for j in range(1, i + 1):
        summation += j

    print(f'Iteration: {i} ===> summation: {summation}')

i = 1

print()
print()
print()

while i <= 10:
    summation = 0
    j = 1

    while j <= i:
        summation += j
        j += 1
    
    print(f'Iteration: {i} ===> summation: {summation}')
    i += 1