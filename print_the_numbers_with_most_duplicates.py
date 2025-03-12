# Use a list and ask the user to input numbers while in a loop
numbers = []

while True:
    user_input = input("Enter a number (or any non-numeric value to stop): ")
    try:
        number = int(user_input)  
        numbers.append(number)
# Break the loop if the input is invalid
# Count each number in the list
# Store the most frequent number in the list and print