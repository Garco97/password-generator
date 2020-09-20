import random
import string
a = open("passwords.txt", "a+")
upper, digits, punctuation = 0,0,0
account = input("Account: ")
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
exec (cmd)
a.write(account + ":" + password + "\n")
a.close()
