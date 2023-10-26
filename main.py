menu = ("Menu\n"
		"-------------\n"
		"1. Encode\n"
		"2. Decode\n"
		"3. Quit")

password = ""


def encode(number_string: str) -> str:
	output = ""
	for number in number_string:
		add_to_output = int(number)
		add_to_output += 3
		if add_to_output > 9:
			add_to_output = add_to_output % 9
			add_to_output -= 1
		output += str(add_to_output)
	return output


def decode(encoded_string: str) -> str:
	pass


def main():

	while True:
		print(menu)
		selection = input("Please enter an option: ")
		if selection == "1":
			original_pass = input("Please enter your password to encode:")
			global password
			password = encode(original_pass)
			print("Your password has been encoded and stored!")
		if selection == "2":
			print(f"The encoded password is {password}, and the original password is {decode(password)}.")
		if selection == "3":
			exit()


if __name__ == "__main__":
	main()
