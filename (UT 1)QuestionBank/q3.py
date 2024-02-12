import math

def calculate_height(length, angle):
  """
  Calculates the height reached by a ladder on a wall given its length and angle.

  Args:
    length: The length of the ladder in feet.
    angle: The angle between the ladder and the ground in degrees.

  Returns:
    The height reached by the ladder on the wall in feet.
  """
  # Convert angle to radians
  angle_radians = math.radians(angle)

  # Calculate height using sine function
  height = length * math.sin(angle_radians)

  # Round the height to two decimal places
  return round(height, 2)

# Calculate and print heights for different cases
print("a) 16ft & 75 degrees:")
height = calculate_height(16, 75)
print(f"  Height reached: {height} feet")

print("b) 20ft & 0 degrees:")
height = calculate_height(20, 0)
print(f"  Height reached: {height} feet")

print("c) 24ft & 45 degrees:")
height = calculate_height(24, 45)
print(f"  Height reached: {height} feet")

print("d) 24ft & 80 degrees:")
height = calculate_height(24, 80)
print(f"  Height reached: {height} feet")
