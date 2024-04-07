# This program prompts the user to input two amounts of money in cents.
# It then calculates the sum of the two amounts and converts it into euros and cents.
# Author: Francesca Ruberto

# Prompt the user to enter the first amount in cents
amount1 = int(input("Enter amount1 in cents: "))

# Prompt the user to enter the second amount in cents
amount2 = int(input("Enter amount2 in cents: "))

# Calculate the total sum of the two amounts
total = amount1 + amount2

# Convert the total sum into euros and cents
euros = total // 100
cents = total % 100

# Print the sum in euros and cents
print(f"The sum of the amounts is: €{euros}.{cents}")

