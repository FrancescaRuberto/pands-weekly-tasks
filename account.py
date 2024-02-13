# This program should read a 10 character account number and give as output only the last 4 digits. 
# Author: Francesca Ruberto 

# I should start by writing my string input
# account_number = str(input("Please enter a 10-digits code: "))

#I believe I should determine the lenght of the string
# account_lenght = len(account_number)

# Now I need to hide the first 6 characters of the account number
# to do that apparently I should use "mask function" when printing
# print("Masked account number:" "XXXXXX" + account_number[-4:])

# Now I should modify the program to deal with number of any lenght
# this requirement is quite ambiguous
# I believe I need to adapt the code so that for any lenght I will have always the last 4 number showing (?)
# to do so I should be adapt the code so it calculates how many characters there are in the string and mask all except last 4
account_number = (input("Please enter a code: "))
masked_length = 'X' * (len(account_number)-4) + account_number [-4:]
# In this way the program should be able to create a string of X
# calculate the number of characters and subtract last 4 so understand that has to mask the rest
# while last part should extraxt the last 4 digits from the account string
print("Masked account number: {}" .format(masked_length))

