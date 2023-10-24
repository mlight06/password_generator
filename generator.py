import random
import re
import string

characters = list(string.ascii_letters)
numbers = list(range(0,9))
stringNums = [str(num) for num in numbers]
allchars = characters + stringNums

numPasswords = int(input('How many passwords would you like to generate?'))
passLength = int(input("How many characters do you need for your password?"))

print('\nHere are your passwords:')

for password in range(numPasswords):
    passwords = ''
    for character in range(passLength):
        passwords += random.choice(allchars)
    print(passwords)


# print('chars', chars)
