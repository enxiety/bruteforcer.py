import random
import pyautogui
import string

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars_list = list(chars)
password = pyautogui.password("Enter a password : ")
guesses_used = 0
guess_password = ""

while guess_password != password:
    guess_password = random.choices(chars_list, k=len(password))
    guesses_used += float(1)

    print(guess_password)
    print(guesses_used)

    if guess_password == list(password):
        print("Your password is : " + "".join(guess_password))
        input("Press enter to exit")
        break
