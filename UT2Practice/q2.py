import math

c = 3 * 10 ** 8

def findEnergy(mass):
    energy = mass * c ** 2
    return energy

mass = float(input("Enter mass in kgs: "))
energy = findEnergy(mass)
print(f"The energy equivalent of {mass} kg is {energy:.2e} joules") 