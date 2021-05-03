#Write a program to check if a word is a Palindrome

word = input('Enter the word to check: ')

if word == word[::-1]:
    print('The word is a Palindrome')
else:
    print('Is not a Palindrome')