origPrice = float(input("Enter the original price"))
discount = float(input("Enter discount percentage: "))
newPrice = (1 - discount/100) * origPrice

print("${:.2f} discounted by {:.0f}% is ${:.2f}  ".format(origPrice, discount, newPrice ))