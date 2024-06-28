# pattern_drawing.py

# Ask the user to enter a positive integer
size = int(input("Enter a positive integer: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side without advancing to a new line
    for _ in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Increment the row counter
    row += 1