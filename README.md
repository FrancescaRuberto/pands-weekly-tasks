# Programming and Scripting Course Repository

## Introduction
Hello! I am Francesca Ruberto, a student currently enrolled in the "Programming and Scripting" course at ATU Mato-Galway. This repository contains my solutions to weekly assignments and the final project for the course.

## Weekly Assignments
### Week 1
Description: Week 1 served as an introduction to the course, primarily focusing on familiarizing ourselves with the essential tools and setting up our development environment. We delved into introductory tasks, including creating a GitHub account, downloading necessary software, and establishing the foundational elements required for the subsequent weeks of the course.

Weekly task: The first assignment required an introduction post on Teams, installation of required software, GitHub setup, and the creation of a simple Python program.
Task: 
- Pull the sample code from the repository.
- Create a GitHub account and a repository named "pands-mywork" and another for weekly tasks ("pands-weekly-tasks").
- Commit and push a file named helloworld.py that displays "Hello World!" when run.

### Week 2 - bank.py
Description: Week 2 focused on the basics of programming, featuring engaging content such as lectures on programming's nature (optional), hands-on Python experiences in iPython, tutorials on command line and VSCode, and the installation of Git for VSCode's terminal. The week culminated in crafting our first programs, providing practical application of the learned concepts.

Weekly task: The second assignment requited exploring fundamental programming concepts and developing a Python program named bank.py with the following specifications:
- Prompt the user and read in two money amounts (in cents).
Add the two amounts.
Print out the answer in a human-readable format with a euro sign and a decimal point between the euro and cent of the amount.

For this task I did not use external sources for this solution, I solely relied on the material provided during the lecture. 

Note: The solution to this task can be found in the program uploaded to this Git repository.

### Week 3 - account.py
Description: 
For the third week's assignment, the focus was on understanding variables, covering various aspects (variable types, understanding the Math module, manipulating strings). 

Weekly tasks: The task for this week involved creating a Python program named accounts.py with the following requirements:
- Bank account numbers can be stored as 10-character strings, but for security reasons, some applications display only the last 4 characters (with the preceding characters replaced with Xs). The program should read in a 10-character account number and output the account number with only the last 4 digits showing, replacing the first 6 digits with Xs.

An extra requirement was given:
- Modify the program to deal with account numbers of any length. The requirement is somewhat vague, so assumptions should be commented in the code.

Note1: For the first part of the task, no external sources were used. However, for the extra requirement, external sources were consulted, particularly online references:
- W3 School: https://www.w3schools.com/python/python_strings.asp / https://www.w3schools.com/python/ref_string_format.asp
- Geeksforgeeks: https://www.geeksforgeeks.org/python-string/ / https://www.geeksforgeeks.org/python-string-format-method/
- Python official documentation

Note2: The solution to this task can be found in the program uploaded to this Git repository.

### Week 4 - collatz.py
Description: For the fourth week's assignment, the focus was on introducing if statements, while loops, and for loops. The main objective was to understand their syntax and basic functionality. 

Weekly task: The task for this week was to write a Python program named collatz.py that prompts the user to input any positive integer and outputs the successive values of a specific calculation. The calculation involves, at each step, taking the current value and dividing it by two if it is even, and multiplying it by three and adding one if it is odd. The program should end when the current value becomes one.

Note1: To understand the Collatz sequence, I watched materials provided by the professor, including an optional YouTube video. While the initial part of the code was understood through the provided material and lab, the appending of values to the list proved challenging. While working on the collatz.py program, I faced the challenge of maintaining a sequence of values generated during its execution. In order to achieve this, I recognized the need to use a data structure capable of storing an ordered sequence.During my search, I found valuable resources that explained the manipulation of lists in Python, and one common method that stood out was append(). This method seemed to be a standard and efficient way to add elements to a list. Some of the websites I consulted during this process include:
- Python official documentation: https://docs.python.org/3/tutorial/datastructures.html
W3 School: https://www.w3schools.com/python/python_lists.asp / https://www.w3schools.com/python/python_lists_methods.asp
- Geeksforgeeks: https://www.geeksforgeeks.org/python-list-append-method/

Note2: The solution to this task can be found in the program uploaded to this Git repository.


### Week 5 - weekday.py
Description: This week's module covered key data structures in Python, including lists, tuples, and dictionaries. Additionally, a brief overview of Jupyter notebooks was provided. 

Weekly task: The task of this week required to create a program that determines whether the current day is a weekday or the weekend. 

Note1: At the beginning of this task, I encountered challenges as I didn't initially understand the need to import the datetime module. To resolve this, I referred to online sources, to comprehend how to utilize this import. Once I gained clarity on its usage, I was able to complete the program smoothly. The online sources I used included:
- W3 School: https://www.w3schools.com/python/python_datetime.asp / https://www.w3schools.com/python/gloss_python_date.asp 

Note2: The solution to this task can be found in the program uploaded to this Git repository.

### Week 6 - squareroot.py
Description: This week our attention turns towards the crucial concepts of functions and modules. The lab assignment challenges us to create a more extensive program, emphasizing the importance of breaking down code into modular functions for enhanced readability and maintainability. 

Weekly task: The weekly task involved crafting a program capable of taking a positive floating-point number as input and delivering an approximation of its square root. The key requirement is to construct a function, named sqrt, to execute this operation. Importantly, we are urged to refrain from using convenient built-in methods such as x ** 0.5 or math.sqrt(x).

Note 1: This week's assignment presented a notable challenge, taking me more time for completion compared to previous ones. While I cannot assert absolute correctness, the code seems running fine, albeit with potential room for improvement. The first part, dealing with function creation using def, was relatively smooth, thanks to my earlier experience obtained while exercising on the weekly lab. Realizing the need to import the math module for its sqrt function was pretty straightforward. However, the subsequent part, entailing the utilization of the Newton method, introduced a layer of complexity. Despite relying on the professor's materials, I had to dive deeper into understanding the intricacies of the Newton method. Each step in the computation posed its own challenge, leading me to explore various online sources to grasp the process better. The online sources I used included:
- W3 School https://www.w3schools.com/python/python_functions.asp
- Real Python https://realpython.com/defining-your-own-python-function/
- Geeksforgeeks https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
- Patrick Walls https://patrickwalls.github.io/mathematicalpython/root-finding/newton/
- StackOverflow https://stackoverflow.com/questions/61310003/newton-raphson-root-finding-algorithm
- StackExchange https://codereview.stackexchange.com/questions/75279/newtons-square-root
- Wikipedia https://en.wikipedia.org/wiki/Newton%27s_method

Note2: The solution to this task can be found in the program uploaded to this Git repository.

### Week 7 - es.py
Description: This week's focus includes mastering the fundamentals of reading and writing files, along with an introduction to JSON and CSV file formats. Additionally, we delve deeper into Python functions and modules, emphasizing the importance of modular code for readability and maintainability. Error handling techniques are explored to ensure program robustness.

Weekly task: this week's task is designed to count the occurrences of the letter 'e' in a text file provided as an argument via the command line. The script incorporates error handling to address scenarios such as missing arguments, non-existent files, or files that are not in a text format.

Note1: This code snippet is designed to count the occurrences of the letter "e" in a text file named "moby-dick.txt." The program incorporates error handling to address scenarios such as missing files or files that are not in a text format. Assumptions made during the development process include the file's existence in the same directory as the script and the filename being provided as just the name of the file without a full path. To handle errors effectively, I relied on online material to ensure proper error messages and handling techniques, as precise completion instructions were not provided. The online sources I used included:
- GeeksForGeeks https://www.geeksforgeeks.org/os-module-python-examples/
- Java2B1og https://java2blog.com/check-if-variable-is-none-python/
- Python Documentation https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- Python Documentation https://docs.python.org/3/tutorial/errors.html
- Real Python https://realpython.com/python-exceptions/
- Real Python https://www.google.com/search?q=Python+Exception+Handling+Techniques&rlz=1C1CHBF_itIE1032IE1032&oq=Python+Exception+Handling+Techniques&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB7SAQczNjFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
- W3 School https://www.w3schools.com/python/module_os.asp
- W3 School https://www.w3schools.com/python/ref_string_count.asp

Note2: The solution to this task can be found in the program uploaded to this Git repository.
