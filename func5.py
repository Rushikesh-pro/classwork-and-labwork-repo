def count_characters(input_string):
    letters = 0
    digits = 0
    special_symbols = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    return letters, digits, special_symbols


# Example usage
input_string = input("Enter a string: ")
letters, digits, special_symbols = count_characters(input_string)

print(f"Total letters: {letters}")
print(f"Total digits: {digits}")
print(f"Total special symbols: {special_symbols}")
