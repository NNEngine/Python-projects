import math
import time
import sys

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
	time.sleep(0.07)

msg = f"\nWelcome {user_name}! Enjoy The Calculations!"
for char in msg:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.05)
print()

print("\n")

print("#==========================================================#")
print("#                Scientific Calculator                     #")
print("#----------------------------------------------------------#")
print("# Features                                                 #")
print("# - 1. Powers                                              #")
print("# - 2. Roots                                               #")
print("# - 3. Logarithm                                           #")
print("# - 4. Modulus                                             #")
print("# - 5. Factorial                                           #")
print("# - 6. Trigonometry                                        #")
print("# - 7. Exit                                                #")
print("#==========================================================#")


def input_number(msg):
	while True:
		try:
			return float(input(f"Enter {msg}: "))
		except ValueError:
			print("Enter Valid Input")


while True:
	while True:
		try:
			choice = int(input("Enter choice: "))
			break
		except ValueError:
			print("Please enter a Integer value")

	if choice == 1:
		number = input_number("number")
		power = input_number("power")
		result = number ** power
		print(result)

	elif choice == 2:
		number = input_number("number")
		root = input_number("root (2, 3, 4, 5)")
		result = number ** (1 / root)
		print(result)

	elif choice == 3:
		while True:
			number = input_number("number")
			if number > 0:
				while True:
					base = input_number("base")
					if base > 0 and base!=1:
						result = math.log(number, base)
						print(result)
						break
					else:
						print("Enter a Positive base but not 1")
				break
			else:
				print("Enter a Positive Number")

	elif choice == 4:
		number = input_number("Number")
		if number < 0:
			number = -number
		print(number)

	elif choice == 5:
		while True:
			number = input_number("number")
			number = int(number)
			if number >= 0:
				result = math.factorial(number)
				print(result)
				break
			else:
				print("Please enter positive number")

	elif choice == 6:
		print("#--------------------------------#")
		print("# 1. sin    5. cosec             #")
		print("# 2. cos    6. sec               #")
		print("# 3. tan    7. cot               #")
		print("# 4. Exit                        #")
		print("#--------------------------------#")

		while True:
			while True:
				try:
					trig_choice = int(input("Enter choice: "))
					break
				except ValueError:
					print("Enter a Valid Choice")

			match trig_choice:
				case 1:
					number = input_number("number")
					print(math.sin(math.radians(number)))
				case 2:
					number = input_number("number")
					print(math.cos(math.radians(number)))
				case 3:
					number = input_number("number")
					print(math.tan(math.radians(number)))
				case 5:
					number = input_number("number")
					print(1 / math.sin(math.radians(number)))
				case 6:
					number = input_number("number")
					print(1 / math.cos(math.radians(number)))
				case 7:
					number = input_number("number")
					print(1 / math.tan(math.radians(number)))
				case 4:
					print("Exit from trigonometry section")
					print("------------------------------")
					break
				case _:
					print("Choose from the existing choices")

	elif choice == 7:
		print("Exit!")
		break
	else:
		print("Please choose from (1, 2, 3, 4, 5)")
