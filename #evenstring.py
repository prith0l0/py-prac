"""Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’."""
# Accept input string from user
input_str = input("Enter a string: ")

# Display characters at even index numbers
print("".join(input_str[i] for i in range(len(input_str)) if i % 2 == 0)) #The characters that are present at even index numbers are concatenated together using the "".join() function and printed to the console.
