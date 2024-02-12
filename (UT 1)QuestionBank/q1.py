import math

def is_in_dartboard(x, y):
  """
  Checks if a dart hits the dartboard based on its coordinates.

  Args:
    x: The x-coordinate of the dart.
    y: The y-coordinate of the dart.

  Returns:
    True if the dart hits the dartboard, False otherwise.
  """
  distance_from_center = math.sqrt(x**2 + y**2)
  return distance_from_center <= 10

# Evaluate for the given coordinates
coordinates = [
  (0, 0),
  (10, 10),
  (6, 6),
  (7, 8),
]

for coord in coordinates:
  x, y = coord
  result = is_in_dartboard(x, y)
  print(f"Dart at ({x}, {y}) hits the dartboard: {result}")
