# Function to perform string operations
def string_operations(s, char_to_count):
    # (i) Find length of the string
    length = len(s)

    # (ii) Convert to uppercase and lowercase
    upper = s.upper()
    lower = s.lower()

    # (iii) Count the number of occurrences of a given character
    count_char = s.count(char_to_count)

    # Display results
    print(f"Original string: {s}")
    print(f"Length of the string: {length}")
    print(f"Uppercase: {upper}")
    print(f"Lowercase: {lower}")
    print(f"Occurrences of '{char_to_count}': {count_char}")


# Example usage
input_string = "Hello World! Welcome to Python Programming."
character = 'o'

string_operations(input_string, character)

