def calculate_discount(amount, is_member):
  
  if amount >= 2000:
    discount_percentage = 10
  elif amount >= 1000:
    discount_percentage = 8
  elif amount >= 500:
    discount_percentage = 5
  else:
    discount_percentage = 0

  # Apply additional discount for members
  if is_member:
    discount_percentage += 5

  # Calculate net payable amount
  discount_amount = amount * discount_percentage / 100
  net_payable_amount = amount - discount_amount

  return discount_percentage, net_payable_amount

shopping_amount = float(input("Enter shopping amount: "))
is_member = input("Are you a member (y/n): ").lower() == "y"

discount_percentage, net_payable_amount = calculate_discount(shopping_amount, is_member)

print("Discount percentage:", discount_percentage, "%")
print("Net payable amount:", net_payable_amount)

