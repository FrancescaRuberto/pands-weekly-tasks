# This program ask the user to input a positive integer
# Then, it outputs the successive values of the following calculaions
# Author: Francesca Ruberto

# I need to calculate the next value by taking the current value
# and if this is even, divide by two
# and if it is off, multiply by three and add one


# First thing I need to establish the question for the user
first_input = int(input("Please enter a positive int: "))

# I need an if function to make sure the input is a positive int
if first_input <= 0:
    print("Please enter a positive int: ")
# Now I need to keep track of the steps when the user enter a correct number
else:
    collatz_order = [first_input]
# According to collatz rule I need to keep updating the number until it becomes 1
    while first_input != 1:
        if first_input % 2 == 0:
            first_input = first_input // 2
        else:
            first_input = 3 * first_input + 1 
# Apparently, I need to append "first_outupt" to "collatz_order"
# in this way each step will be recorded
        collatz_order.append(first_input)

    print(*collatz_order)