import random
import string
import os.path
from console import fg, bg, fx
from encryption import generate_key, decrypt_message, encrypt_message, load_key
    
if __name__ == "__main__":
    if not os.path.isfile(".secret.key"):
        generate_key()
    upper, digits, punctuation = 0,0,0
    account = input("Account: ")
    a = open("." + account + ".key", "wb")
    N = int(input("Choose length of the password: "))
    upper= True if input("Upper case too? (y/n) ") == "y" else False
    digits = True if input("Digits? (y/n) ") == "y" else False
    punctuation = True if input("Punctuation signs? (y/n) ") == "y" else False 
    print("\nLength:", str(N))
    print("Uppercase:", str(upper))
    print("Digits:", str(digits))
    print("Punctuation:", str(punctuation))
    options = 'string.ascii_lowercase'
    options += '+ string.digits' if digits else ''
    options += '+ string.ascii_uppercase' if upper else '' 
    options += '+ string.punctuation' if punctuation else ''
    cmd = "password = ''.join(random.choice(" + options + ") for _ in range(N))"
    exec(cmd)
    a.write(encrypt_message(password))
    a.close()
