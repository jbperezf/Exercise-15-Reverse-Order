# Exercise 15. Reverse Order
#
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
#
#   My name is Michele
#
# Then I would see the string:
#
#   Michele is name My
#
# shown back to me.


def reverse_string_1(user_string):
    user_string = user_string.split()
    return " ".join(reversed(user_string))

def reverse_string_2(user_string):
    user_string = user_string.split()
    return " ".join(user_string[::-1])

def reverse_string_3(user_string):
    user_string = user_string.split()
    reversed_string = []
    for word in user_string:
        reversed_string.insert(0, word)
    return " ".join(reversed_string)


def reverse_string_4(user_string):
    user_string = user_string.split()
    user_string.reverse()
    return " ".join(user_string)


a = input("Enter a phrase: ")

print(reverse_string_1(a))
print(reverse_string_2(a))
print(reverse_string_3(a))
print(reverse_string_4(a))
