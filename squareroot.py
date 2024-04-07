#This program tasked a positive floating-point number and outputs an approximation of its square roots.
#Author: Francesca Ruberto

# To begin, I believe I should import the math module
# As I have to use sqrt function

import math

# Now I need to proceed with the creation of my sqrt function
def sqrt():
    # I make sure the number is positive
    while True:
        number = float(input("Please enter a positive number: "))
        return number

# Now that I have my function I need to write the main program
# I can't use build-in functions of math.sqrt
# Suggested to use the Newton methon
# Newton's Method = 0.5*(approx+n/approx)

# Apply newton method 
# I need to enter a piece of code from which I can estimate the squareroot
number = sqrt()
estimate_num = number / 2

# According to my research the Newton method include the "espsilon"
# The epsilon should represent a tolerance value
epsilon = 0.0001

# I need to calculate the absolute value
while abs(estimate_num * estimate_num - number) > epsilon:
    # Now I apply the method
    estimate_num = 0.5 * (estimate_num + number / estimate_num)

print(f"The square root of {number} is approx {estimate_num}")

           

