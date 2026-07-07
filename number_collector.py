# number_collector.py
# A program that collects 3 numbers from the user outputs the sum and average of those numbers.

# Number 1
try:
    num1 = int(input("Enter number 1:")) #indentation block is important here because we want to catch the ValueError exception that may occur when converting the input to an integer.
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num1 = 0 # in this case no need for closing program because we can use 0 as a default value and continue with the program.
# any value that is not a valid int will be replaced with 0 and the program will continue to run without crashing.
# Number 2
try:
    num2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num2 = 0

# Number 3
try:
    num3 = int(input("Enter number 3: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num3 = 0

# Calculate sum and average
total = num1 + num2 + num3
average = total / 3  # Calculate average by dividing the total by 3

# Display the results
print()
print(f"Your numbers: {num1}, {num2}, {num3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")