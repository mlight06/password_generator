import random
import re


# want to comeback and refactor with regex
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
# chars = re.compile('')

numPasswords = int(input('How many passwords would you like to generate?'))
passLength = int(input("How many characters do you need for your password?"))

print('\nHere are your passwords:')

for password in range(numPasswords):
    passwords = ''
    for character in range(passLength):
        passwords += random.choice(chars)
    print(passwords)

# print('chars', chars)
