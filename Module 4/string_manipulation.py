# Accept string input from the user
user_input = input("Enter a string: ")

# (i) Remove leading and trailing spaces
trimmed_string = user_input.strip()

# (ii) Replace all spaces with underscores
modified_string = trimmed_string.replace(' ', '_')

# Display the results
print("Original string:", repr(user_input))
print("After removing leading and trailing spaces:", repr(trimmed_string))
print("After replacing spaces with underscores:", repr(modified_string))

