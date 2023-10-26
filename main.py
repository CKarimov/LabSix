# Menu that is printed in main loop to show options
menu = ("Menu\n"
		"-------------\n"
		"1. Encode\n"
		"2. Decode\n"
		"3. Quit")

password = ""


# Encoder function (Shifts each number by 3)
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

# Matthew Khan
def decode(encoded_sequence):
    decoded_sequence = ""
    for digit in str(encoded_sequence):
        decoded_digit = str((int(digit) - 3) % 10)  # Ensure the result stays a single digit (0-9)
        decoded_sequence += decoded_digit
    return int(decoded_sequence)


# Main function
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
