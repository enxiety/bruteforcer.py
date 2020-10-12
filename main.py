import random
import string

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=+_/';.,[]`"
chars_list = list(chars)
password = input("Enter a password: ")
guesses_used = 0
guess_password = ""

while guess_password != password:
    guess_password = random.choices(chars_list, k=len(password))
    guesses_used += float(1)

    print(guess_password, guesses_used, chars.isupper(), )

    if chars.isupper():
        guesses_used = + str(2)

    if guess_password == list(password):
        print("Your password is: " + "".join(guess_password))
        input("Press enter to exit")
        break

    if guesses_used == 10000000:
        print("Too many tries, quitting program")
        exit(0)
