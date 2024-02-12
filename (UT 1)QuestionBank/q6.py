def check_eligibility(name, age):
  """
  Checks if a user is eligible to apply for a driving license based on age.

  Args:
    name: The name of the user.
    age: The age of the user.

  Returns:
    A message indicating whether the user is eligible or not.
  """
  if age >= 18 and age < 80:
    return f"{name}, you are eligible to apply for a driving license."
  elif age < 18:
    years_remaining = 18 - age
    return f"{name}, you are not eligible yet. You need to wait {years_remaining} years to be eligible."
  else:
    return f"{name}, you are not eligible due to age restrictions."

name = input("Enter your name: ")
age = int(input("Enter your age: "))

message = check_eligibility(name, age)
print(message)
