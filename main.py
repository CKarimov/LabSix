def encode(number_string: str) -> str:
	output = ""
	for number in number_string:
		add_to_output = int(number)
		add_to_output += 3
		add_to_output = add_to_output % 9
		output += str(add_to_output)
	return output
def main():
	user_input = input("Enter your number")
	encoded = encode(user_input)
	print(encoded)

if __name__ == "__main__":
	main()
