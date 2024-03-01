# Programming and Scripting Course Repository

## Introduction
Hello! I am Francesca Ruberto, a student currently enrolled in the "Programming and Scripting" course at ATU Mato-Galway. This repository contains my solutions to weekly assignments and the final project for the course.

## Weekly Assignments
### Week 1
Description: The first assignment required an introduction post on Teams, installation of required software, GitHub setup, and the creation of a simple Python program.
Task: 
- Pull the sample code from the repository.
- Create a GitHub account and a repository named "pands-mywork" and another for weekly tasks ("pands-weekly-tasks").
- Commit and push a file named helloworld.py that displays "Hello World!" when run.

### Week 2 - bank.py
Description: The second assignment requited exploring fundamental programming concepts and developing a Python program named bank.py with the following specifications:
- Prompt the user and read in two money amounts (in cents).
Add the two amounts.
Print out the answer in a human-readable format with a euro sign and a decimal point between the euro and cent of the amount.

For this task I did not use external sources for this solution, I solely relied on the material provided during the lecture. 

Note: The solution to this task can be found in the program uploaded to this Git repository.

### Week 3 - account.py
Description: 
For the third week's assignment, the focus was on understanding variables, covering various aspects (variable types, understanding the Math module, manipulating strings). The task for this week involved creating a Python program named accounts.py with the following requirements:
- Bank account numbers can be stored as 10-character strings, but for security reasons, some applications display only the last 4 characters (with the preceding characters replaced with Xs). The program should read in a 10-character account number and output the account number with only the last 4 digits showing, replacing the first 6 digits with Xs.

An extra requirement was given:
- Modify the program to deal with account numbers of any length. The requirement is somewhat vague, so assumptions should be commented in the code.

Note1: For the first part of the task, no external sources were used. However, for the extra requirement, external sources were consulted, particularly online references:
- W3 School: https://www.w3schools.com/python/python_strings.asp / https://www.w3schools.com/python/ref_string_format.asp
- Geeksforgeeks: https://www.geeksforgeeks.org/python-string/ / https://www.geeksforgeeks.org/python-string-format-method/
- Python official documentation

Note2: The solution to this task can be found in the program uploaded to this Git repository.

### Week 4 - collatz.py
Description: For the fourth week's assignment, the focus was on introducing if statements, while loops, and for loops. The main objective was to understand their syntax and basic functionality. The task for this week was to write a Python program named collatz.py that prompts the user to input any positive integer and outputs the successive values of a specific calculation. The calculation involves, at each step, taking the current value and dividing it by two if it is even, and multiplying it by three and adding one if it is odd. The program should end when the current value becomes one.

Note1: To understand the Collatz sequence, I watched materials provided by the professor, including an optional YouTube video. While the initial part of the code was understood through the provided material and lab, the appending of values to the list proved challenging. While working on the collatz.py program, I faced the challenge of maintaining a sequence of values generated during its execution. In order to achieve this, I recognized the need to use a data structure capable of storing an ordered sequence.During my search, I found valuable resources that explained the manipulation of lists in Python, and one common method that stood out was append(). This method seemed to be a standard and efficient way to add elements to a list. Some of the websites I consulted during this process include:
- Python official documentation: https://docs.python.org/3/tutorial/datastructures.html
W3 School: https://www.w3schools.com/python/python_lists.asp / https://www.w3schools.com/python/python_lists_methods.asp
- Geeksforgeeks: https://www.geeksforgeeks.org/python-list-append-method/

Note2: The solution to this task can be found in the program uploaded to this Git repository.


### Week 5 - weekday.py
Description: This week's module covered key data structures in Python, including lists, tuples, and dictionaries. Additionally, a brief overview of Jupyter notebooks was provided. The task of this week required to create a program that determines whether the current day is a weekday or the weekend. 

Note1: : At the beginning of this task, I encountered challenges as I didn't initially understand the need to import the datetime module. To resolve this, I referred to online sources, to comprehend how to utilize this import. Once I gained clarity on its usage, I was able to complete the program smoothly. The omline sources I used included:
- W3 School: https://www.w3schools.com/python/python_datetime.asp / https://www.w3schools.com/python/gloss_python_date.asp 

Note2: The solution to this task can be found in the program uploaded to this Git repository.