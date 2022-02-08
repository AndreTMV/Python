import random

print("Welcome To Your Password Generator")
chars = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÇabcdefghijklmnñopqrstuvwxyzç1234567890.,:-^´¨*+@/ªº%&()=¿?'
number = int(input('Amount of passwords to generate: '))
length = int(input('input your password length: '))

print('\nHere are your password:')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
