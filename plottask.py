#This program is designed to plot an a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
#And a plot of the function  h(x)=x3 in the range 0 to 10

#Author: Francesca Ruberto

import numpy as np
import matplotlib.pyplot as plt

#We need to generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
values = np.random.normal(5, 2, 1000)

#Now I create an histogram of the value
plt.hist(values, bins=5, color='blue', edgecolor='black', label='Normal distribution')

#Now let's define the function h(x) = x^3 in the range 0 to 10
#This passage has been quite tricky for me. 
#According to my researches on numpy documentation I have a couple of options available
#The easier way should be using linspace, that allows us to generate evenly spaces numbers on a specified interval
x = np.linspace(0, 10, 100)

#Now that we have the x I need to generate the corresponding y value for this funciton
y = x ** 3

#Let's plot the function h(x) = x^3
plt.plot(x, y, label='$h(x) = x^3$')

#I need to add a title to this plot
plt.title("Histogram of normal distribution and plot of h(x) = x^3 function")
#Let's also add x and y axes labels
plt.xlabel('Range')
plt.ylabel('$h(x)$')

#Let's add a legend
plt.legend()

#Let's display our plot
plt.show()




