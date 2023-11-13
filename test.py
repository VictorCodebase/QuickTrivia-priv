example_input = "1234ge23"

# Remove non-numeric characters from the input
example_input = ''.join(filter(str.isdigit, example_input))

# Convert the input to an integer
example_input = int(example_input)

print(example_input)
