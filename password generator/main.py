import random
import sys
import time

#=====================================================================================
#                                 Welcome Page
#=====================================================================================

user_name = input("Enter Your Name: ")

WELCOME_ASCII = r"""
__        __   _                            _
\ \      / /__| | ___ ___  _ __ ___   ___  | |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
  \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""

for line in WELCOME_ASCII.splitlines():
	print(line)
	time.sleep(0.1)

msg = f"\nWelcome {user_name}! Get as many passwords as you want!"
for char in msg:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n")

#=======================================================================================
#                               Password Generator Code
#=======================================================================================

while True:
	try:
		number_passwords = int(input("Enter number of passwords: "))
		break
	except ValueError:
		print("Please Enter an Integer Value")

list_lengths_passwords = []

print("Please Enter passwords length between 8 and 20!\n")

for i in range(number_passwords):
	while True:
		try:
			length_passwords = int(input(f"Enter password length of password {i + 1}: "))
			if length_passwords >= 8 and length_passwords <= 20:
				list_lengths_passwords.append(length_passwords)
				break
			else:
				print("Please Enter between 8 and 20!")
		except ValueError:
			print("Please Enter an Integr value!")


list_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "&", "*", "=", "?"]

random.shuffle(list_chars)

print("\n========================================================")
print("                  Your Passwords                        ")
print("========================================================")

i = 1
for length in list_lengths_passwords:
	print(f"Password {i}: {''.join(random.sample(list_chars, length))}")
	i = i + 1
	time.sleep(0.1)
