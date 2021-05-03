# Given a list of numbers, return True if first and last number of the list are the same

# my_list = [12, 54, 9, 4, 66, 10]
my_list = [12, 54, 9, 4, 66, 12]

# if my_list[0] == my_list[len(my_list) - 1]:
if my_list[0] == my_list[-1]:
    print('Are the same')
else:
    print('Not the same')