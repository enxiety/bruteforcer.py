import random
import string

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=+_/';.,[]`"
chars_list = list(chars)
password = input("Enter a password: ")
tries = 0
guess_password = ""

while guess_password != password:
    guess_password = random.choices(chars_list, k=len(password))
    tries += float(1)

    print(guess_password, tries, "<- number of tries")

    if guess_password == list(password):
        print("Your password is: " + "".join(guess_password))
        input("Press enter to exit ")
        break
