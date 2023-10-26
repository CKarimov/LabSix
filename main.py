def encode(number_string: str) -> str:
	output = ""
	for number in number_string:
		add_to_output = int(number)
		add_to_ouput += 3
		add_to_ouput = add_to_output % 9
		output += str(add_to_output)
def main():
	user_input = input("Enter your number")
	encoded = encode(user_input)
	print(encoded)

if __name__ == "__main__"
	main()
