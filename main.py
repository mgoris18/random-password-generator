from lib2to3.pygram import Symbols
import string
from random import choice, shuffle

def randomPass():
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    all = lower + upper + digits + symbols
    shuffle(all)

    length = int(input("How long is the password?: "))
    password= ''

    for i in range(length):
        password += choice (all)
    print(password)

randomPass()