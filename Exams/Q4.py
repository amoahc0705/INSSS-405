name = input("Enter your name: ")  # Prompt the user to enter their name and store it in the 'name' variable
reverse_name = ""  # Initialize an empty string to store the reverse name
for char in name:  # Iterate through each character in the 'name' string
    reverse_name = char + reverse_name # Append the current character to the beginning of the 'reverse_name' string
print("Reverse of your name:", reverse_name) # Print the reverse name

