# Return the count of sub-string "John" appears in the given string "John is good developer. John is a writer"

text = "John is good developer. John is a writer"

# First Method

counter = text.count('John')
print(counter)

# Second Method

words = text.split(' ')
counter2 = 0

for word in words:
    if word == 'John':
        counter2 += 1

print(counter2)