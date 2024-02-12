# This program promt the user and read in 2 money amounts
# Author: Francesca Ruberto


amount1 = int(input("Enter amount1 in cents: "))
amount2 = int(input("Enter amount2 in cents: "))

total = amount1 + amount2

euros = total // 100
cents = total % 100

print(f"The sum of this is: €{euros}.{cents}" .format(euros, cents))

