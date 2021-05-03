# Display the multiplication table from 1 to 12

for i in range(1, 13):
    for j in range(1, 11):
        print(i, '*', j, '=', i * j)
    print()

i = 1

while i <= 12:
    j = 1

    while j <= 10:
        print(i, '*', j, '=', i * j)
        j += 1

    print()
    i += 1