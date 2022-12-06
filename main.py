import random
import string

print("Hello User !\nWelcome To Password Generator !!")

print("... GENERATE A SECURE PASSWORD ...")

max_length = 12             #Maximum Length of Password

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*.?"

string = lower + upper + digits + symbols

pass_len = int(input("Enter Your Password Length: "))       #Password Length

password = "".join(random.sample(string, pass_len))

if (len(password) <= max_length) and (len(password) >= 8):
    print("Your New Password: ",password,"\nStrength of Password: STRONG")
elif (len(password) <= max_length) and (len(password) <= 6):
    print("Your New Password: ",password,"\nStrength of Password: WEAK")
else:
    print("INVALID INPUT ; Length of the Password must be atleast 12 characters. ")