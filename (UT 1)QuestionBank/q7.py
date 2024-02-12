# Define a list of numbers
numbers = []

# Get 5 numbers from the user
for i in range(5):
  number = int(input("Enter a number: "))
  numbers.append(number)

# Initialize minimum and maximum values
minimum = numbers[0]
maximum = numbers[0]

# Iterate through the list to find minimum and maximum
for number in numbers:
  if number < minimum:
    minimum = number
  if number > maximum:
    maximum = number

# Print the minimum and maximum values
print("Minimum:", minimum)
print("Maximum:", maximum)
