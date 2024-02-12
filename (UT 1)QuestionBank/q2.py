# Speed of light in meters per second
speed_of_light = 3 * 10**8

def calculate_energy(mass):
  """
  Calculates the energy equivalent of a mass using the formula e = mc^2.

  Args:
    mass: The mass of the object in kilograms.

  Returns:
    The energy equivalent of the mass in joules.
  """
  energy = mass * speed_of_light**2
  return energy

# Get mass from the user
mass = float(input("Enter the mass of the object in kilograms: "))

# Calculate and print the energy
energy = calculate_energy(mass)
print(f"The energy equivalent of {mass} kg is {energy:.2e} joules.")
