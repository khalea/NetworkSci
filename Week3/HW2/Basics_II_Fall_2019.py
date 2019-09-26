'''

I had a busy week (extracurriculars/work & career prep, etc) and long story short, I didn't
have a ton of time to complete this assignment between the time it was released on Tuesday
and Friday night.

Anyways, to save you some time, I skipped these questions: 

1.4 (partially), 
2.1.2, 
2.2 (partially), 
2.3.1,
2.3.2

'''


# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
from IPython import get_ipython

#%% [markdown]
# Python Basics part 2
# ====
# 
# Intro to data munging
# ----
# 
# From [Wikipedia](https://en.wikipedia.org/wiki/Data_wrangling):
# > Data munging or data wrangling is loosely the process of manually converting or mapping data from one "raw" form into another format that allows for more convenient consumption of the data with the help of semi-automated tools.
# 
# 
# 
# A large part of working with data is reading and transforming that data prior to analysis. Getting comfortable with reading, writing, and working with data is crucial to doing any real work.
# 
# 
#%% [markdown]
# 1. Strings
# ----
# We're going to start where we left off in the Python Basics tutorial, on strings. Python features extremely powerful and sophisticated string handling, but it comes at a slight cost of complexity: of all the built-in datatypes, strings probably have the highest number of commonly-used methods.
# 
# ### String methods
# 
# The `replace()` method is used to replace all occurrences of one string with another:

#%%
header = 'mpg,cyl,displ,hp,weight,accel,yr,origin,name'
header.replace(',', ' ')

#%% [markdown]
# The `split()` method returns a list of substrings separated by the given character

#%%
header = 'mpg,cyl,displ,hp,weight,accel,yr,origin,name'
fields = header.split(',')
print(fields)

#%% [markdown]
# The `join()` method can be thought of as the inverse of the `split()` method; it takes a list of strings, and joins them into a single string separated by the given character. It has a somewhat unintuitive syntax though:

#%%
'|'.join(fields)

#%% [markdown]
# Often when dealing with reading from files, it's desirable to strip whitespace from the ends of a string. Whitespace includes spaces, tabs, and newline characters (`'\n'` in Python). The `strip()` convenience method makes this task easy:

#%%
read_string = '    this could come from a file\n'
print(read_string)


#%%
stripped_string = read_string.strip()
print(stripped_string)

#%% [markdown]
# ### Reading text files
# 
# A lot of the common tasks for reading and writing text files boil down to string operations. To open a file for reading, we can use the `open()` builtin function. The `open()` function returns a file handle, which can be `read()` to retrieve the contents as a string.
# 
# The `open()` function can be used as a "context manager" so that the file handle is automatically closed when we leave the indented block. Context managers are indicated by the `with` keyword.
# 
# In the Homeworks folder for this assignment on Canvas, you will find the 'employees.tsv' file you will need to download for the next portion of this assignment. 
# 
# **Note:** If you are using Google Colab, you can upload the file to this notebook by expanding the left-side menu, and then dragging a file into space marked "Files"
# If you are using Juypter Notebook, ensure the 'employees.tsv' file is in the same folder as the .ipynb file for this assignment
# 

#%%
with open('employees.tsv') as f_in:
    file_contents = f_in.read()

file_contents

#%% [markdown]
# Note that the more complex strings often encountered in files act differently in Jupyter Notebook whether they are `print()`ed or just executed by themselves:

#%%
print(file_contents)

#%% [markdown]
# As the `.tsv` file extension hints at, this file is a tab-separated values file. Think of it like an Excel spreadsheet; each line is a row, and the cells are delimited by tab characters. Like many spreadsheets, we can see that the first row has labels for the columns.
#%% [markdown]
# ## <font color='red'>EXERCISE 1.1</font>
# Read the `employees.tsv` file in this directory and get a list of the column names. Assign this list to a variable named `column_names`. Don't reuse the `file_contents` variable from above, do the file reading yourself.

#%%
# Open the file
with open('employees.tsv') as employees:
    # read the file
    file_contents = employees.read()
    # separate columns by \n (only split once to get 1st column)
    separated = file_contents.split('\n', 1)
    print(separated[0])
    # separate cells by \t (get column names)
    column_names = separated[0].split('\t')
    print(column_names)


#%%
assert tuple(column_names) == (
    'NAME',
    'JOB TITLE',
    'DEPARTMENT',
    'EMPLOYEE ANNUAL SALARY',
    'ESTIMATED ANNUAL SALARY MINUS FURLOUGHS',
)

#%% [markdown]
# The use-case of iterating through the lines of a file is so common that file handles can be used as iterators in order to process a file one line at a time:

#%%
for line in open('employees.tsv'):
    print('Here is the next line')
    print(line)

#%% [markdown]
# Notice the newline characters in the above block. Eliminating those is a primary use-case for the `strip()` method.
#%% [markdown]
# ## <font color='red'>EXERCISE 1.2</font>
# Recall that lists are used when you have a homogeneous collection of things, and tuples are used for heterogeneous collections. In the case of the Employees "spreadsheet" we're working with, the spreadsheet rows are all the same "type", a record, while each row is a heterogeneous collection of name, title, etc., and the column number is what defines the cell type, e.g. the first column contains names, the second contains job titles, etc.
# 
# With that in mind, open the `employees.tsv` file and parse it, returning a list of tuples, with each tuple containing one row's worth of data. Remember to take care of the trailing newlines. Assign this list to a variable named `employee_table`.

#%%
employee_table = []

for line in open('employees.tsv'):
    # Must use tuple constructor, else it will add line as a string
    employee_table.append(tuple([line.strip().split('\t')]))  

employee_table



#%%
# There should be five records, six if you keep the header row
assert 5 <= len(employee_table) <= 6
# The rows should be contained in a list
assert isinstance(employee_table, list)
# Each row should be a tuple
assert all(isinstance(r, tuple) for r in employee_table)
# The last character of the last field should not be a newline in any employee record
assert not any(r[-1][-1] == '\n' for r in employee_table)

#%% [markdown]
# #### A caveat
# 
# Be careful when manually splitting file contents by newlines. Often text files (especially on UNIX-based OSes) will end with a newline character. In this case, the last item of the split list will be a blank string.

#%%
open('employees.tsv').read().split('\n')[-1]

#%% [markdown]
# You can make sure a line is not blank with 
# ```
# if line:
# ```
# since a blank string is evaluated as False:

#%%
bool('') == False

#%% [markdown]
# ### String formatting
#%% [markdown]
# String formatting, or string interpolation, is used to to take a string "template" and insert the variables into the string. This very often comes up when displaying data read from a database. Python's `format()` method is very powerful, and this is the bare minimum, but here's the gist:

#%%
person = ('Rob', 21)

# Implicit positional arguments
print( '{} is {} years old'.format(person[0], person[1]) )

# Explicit positional arguments
template = '{1} years ago, {0} was born. Yes {1} years old!'
print( template.format(person[0], person[1]) )

# Named arguments
template = '{age} years ago, {name} was born. Yes {age} years old!'
print(template.format(name=person[0], age=person[1]) )

#%% [markdown]
# ## <font color='red'>EXERCISE 1.3.1</font>
# Get the data from the `employees.tsv` file. This time you may use the `employee_table` you defined in the previous exercise. Skipping over the header row, use string formatting with implicit or explicit positional arguments in order to print each row's data in English, e.g.
# ```
# LUKE SKYWALKER is a NERF HERDER in the MAINTENANCE department, making $14,021 per year
# ...
# ```

#%%
template = '{} is a {} in the {} department, making {} per year.'
length = len(employee_table)


for i in range(1, length-1):
    # Gather all data included for this person
    emData = employee_table[i][0]
    # Get name (unsplit, in reverse order)
    preName = emData[0].split(',')
    # Put name into standard order & remove spaces
    emName = str(preName[1].strip()) + " " + str(preName[0])
    # Get Occupation
    emOcc = emData[1]
    # Get department
    emDept = emData[2]
    # Get income
    emInc = emData[3]
    
    print(template.format(emName, emOcc, emDept, emInc)) 

#%% [markdown]
# ## <font color='red'>EXERCISE 1.3.2</font>
# Repeat the above exercise using the named argument form of string formatting.

#%%
template = '{name} is a {occupation} in the {dept} department, making {income} per year.'
length = len(employee_table)

for i in range(1, length-1):
    # Gather all data included for this person
    emData = employee_table[i][0]
    # Get name (unsplit, in reverse order)
    preName = emData[0].split(',')
    # Put name into standard order & remove spaces
    emName = str(preName[1].strip()) + " " + str(preName[0])
    # Get Occupation
    emOcc = emData[1]
    # Get department
    emDept = emData[2]
    # Get income
    emInc = emData[3]
    
    print(template.format(name=emName, occupation=emOcc, dept=emDept, income=emInc))

#%% [markdown]
# ### Writing text files
# 
# Writing text files is similar to reading but in reverse. Where we would use `read()`, we now use `write()`; `split()` is replaced with `join()`; and we use an `open()` function with an additional argument to specify that we want to open a file for writing.

#%%
lines = ['line 1', 'line 2', 'line 3']
file_contents = '\n'.join(lines)
with open('test.txt', 'w') as f_out:
    f_out.write(file_contents)


#%%
# Statements beginning with a % are called Jupyter "magic".
# They are not valid Python, but are instead commands for Jupyter
# to handle before passing them to the Python kernel
get_ipython().run_line_magic('cat', 'test.txt')

#%% [markdown]
# ## <font color='red'>EXERCISE 1.4</font>
# Your boss only wants a list of the employee names and estimated annual salary. First generate a list of tuples containing only these data, along with the header giving the column names. Then write this data out to a tab-separated file called `employee_salaries.tsv`

#%%

'''
# Do we generarte a separate tuple containing the headers?
length = len(employee_table)
# List of tuples (name, income)
names_salary = []

# Get header list
headers = employee_table[0]

# Get name (and rearrange) and income
for i in range(1, length-1):
    emData = employee_table[i][0]
     # Get name (unsplit, in reverse order)
    preName = emData[0].split(',')
    # Put name into standard order & remove spaces
    emName = str(preName[1].strip()) + " " + str(preName[0])
    # Get income
    emInc = emData[3]
    # Add tuple to list names_salary
    names_salary.append((emName, emInc))

print(names_salary)
#print(names_salary[0])



headerName = []
for i in headers[0]:
    # print(headers[i])
    if (i == 'NAME'):
        headerName.append(i)
    elif (i == 'EMPLOYEE ANNUAL SALARY'):
        headerName.append(i)    

print(headerName)

fileHeaders = '\t'.join(headerName)
# fileData = '\t'.join(names_salary)

with open("employee_salaries.tsv", "w") as f_out:
    f_out.write(fileHeaders)

'''





#%%
'''
assert open('employee_salaries.tsv').read() == 'NAME\tEMPLOYEE ANNUAL SALARY\nBATEMAN,  KELLY ANNE\t$118404.00\nCREMINS,  KEVIN M\t$77238.00\nDAVIS,  CRAIG W\t$77238.00\nMORENO,  JOSE\t$120228.00\nURSETTA,  ROSARIO\t$51216.00'
'''

#%% [markdown]
# ## 2. Dictionaries
#%% [markdown]
# A dictionary (`dict`) can be used to store associations or relations between different entities (person and age, name and alias, person and friends' names etc.). Dict items are specified as **key**:**value** pairs within **curly brackets**. Instead of accessing dictionary values by their index, we use the **key**. As always, values are accessed using **square brackets**.

#%%
age_data = {'Jerry' : 23, 'Martha' : 21}

age_data['Jerry']  # retrieve Jerry's age

#%% [markdown]
# ### Inclusion tests

#%%
'Jerry' in age_data


#%%
'Mickey' in age_data


#%%
age_data['Mickey']

#%% [markdown]
# ### Looping over dicts
#%% [markdown]
# Since we check for key membership with the `in` keyword, which is associated with sequences (lists, tuples, strings), it makes sense that `list(age_data)` gives us the keys in `age_data`:

#%%
list(age_data)

#%% [markdown]
# The above is "syntactic sugar" for the following:

#%%
list(age_data.keys())

#%% [markdown]
# With a sequence of keys in hand, we have one way to loop over a dict:

#%%
for name in age_data:
    years = age_data[name]
    msg = '{} is {} years old'.format(name, years)
    print(msg)

#%% [markdown]
# The `.items()` method gives us another way:

#%%
list(age_data.items())


#%%
for name, years in age_data.items():
    msg = '{} is {} years old'.format(name, years)
    print(msg)

#%% [markdown]
# ### Mutable values
#%% [markdown]
# The keys of a dict must be an immutable object e.g. string, number, or tuple.
# 
# The values of a dict can be anything, including lists:

#%%
friends = {
    'Jerry': [
        'Alice',
        'Bob',
    ],
    'Martha': [
        'Bob',
        'Carol',
    ],
}

print( friends['Martha'] )
print( friends['Martha'][1] )

#%% [markdown]
# and mutable values in dicts can be changed.

#%%
friends['Martha'].append('Daniel')
print( friends['Martha'] )

#%% [markdown]
# Note that the above can be used to define a network. The dict keys are the node names and the dict values contain the node neighbors. Of course additional work would need to be done in the case of undirected networks, but this is the foundation of the NetworkX package that we will use in this course.
#%% [markdown]
# ### "Concatenation"
#%% [markdown]
# To revisit a theme from Python Basics, can we combine two dicts somehow? Indeed we can, using the `.update()` method:

#%%
age_data = {'Jerry' : 23, 'Martha' : 21}
new_age_data = {'Alice': 21, 'Bob': 25, 'Martha': 29}

age_data.update(new_age_data)
age_data

#%% [markdown]
# Note that values are overwritten for items that exist in the dict being updated (Martha in this example).
# 
# Unfortunately, the `+` operator does not work for dicts ☹

#%%
# Raises an error
age_data + new_age_data

#%% [markdown]
# ## <font color='red'>EXERCISE 2.1.1 </font>
# A bored (and inaccurate) spy satellite makes a record of your vacation trail. Below are a few entries in its cloud storage: <br/>
# Day 1: Paris, Lat = 99, Long = 100 <br/>
# Day 4: Prague, Lat = 99, Long = 90 <br/>
# Day 6: Zurich, Lat = 90, Long = 90 <br/>
# Day 10: Moscow, Lat = 80, Long = 70 <br/>
# 
# Store the above information in a dictionary. Choose an appropriate key. Using a loop, produce a list of just the names of places visited after Day 2 and located above 85 latitude. Name this list `matching_place_names`.

#%%
vacation = {
    1 : [
        'Paris', 99, 100
    ],
    4 : [
        'Prague', 99, 90
    ],
    6 : [
        'Zurich', 90, 90
    ],
    10 : [
        'Moscow', 80, 70
    ]
}

matching_place_names = []

# Iterate through keys
for day in vacation.keys():
    # print(day)
    if ((day > 2) and (vacation[day][1] > 85)): 
        # print(vacation[day][0])
        matching_place_names.append(vacation[day][0])


#%%
assert set(matching_place_names) == {'Prague', 'Zurich'}

#%% [markdown]
# This task of taking a list of things, filtering it on some condition, then extracting a value from the filtered items, is an extremely common one in data computing.
# 
# In the employee data example/exercise from the previous section, we obtained our data as a list of tuples, with each tuple representing one person's data as a "row". While very space-efficient, this index-based data format gets tricky to work with once you have several columns. A different way to work with that type of tabular data is for each row to be represented as a dict with the column names as keys and the data as values:
# ```
# employee_records = [
#     {
#         'name': 'BATEMAN,  KELLY ANNE',
#         'job_title': 'DEPUTY CHIEF ADMINISTRATIVE OFFICER',
#         ...
#     },
#     ...
# ]
# ```
#%% [markdown]
# ## <font color='red'>EXERCISE 2.1.2 </font>
# Repeat the previous exercise 2.1.2, but instead store the initial data as a list of dicts.

#%%



#%%
assert set(matching_place_names) == {'Prague', 'Zurich'}

#%% [markdown]
# ### Wow, that sucked; `zip()` to the rescue
# 
# Comparing exercise 2.1.1 and 2.1.2, we see the pros and cons of storing rows as tuples versus dicts. The filtering code is much more expressive and less error-prone when using dicts, but entering the data can be cumbersome. Luckly Python gives us some help. Observe the `zip()` builtin method:

#%%
names = ['Alice', 'Bob', 'Martha']
ages = [21, 25, 29]

list(zip(names, ages))

#%% [markdown]
# Note that this looks like the output to dict's `.items()` method from above:

#%%
age_data = {'Jerry' : 23, 'Martha' : 21}
list(age_data.items())

#%% [markdown]
# The `.items()` method is executed on a dict and returns a list of tuples. One might ask, is there an "inverse" to the `.items()` method that takes a list of tuples and returns a dict? Indeed there is, the `dict()` constructor itself:

#%%
new_age_data = dict( zip(names, ages) )
new_age_data

#%% [markdown]
# ## <font color='red'>EXERCISE 2.2 </font>
# Parse the `employees.tsv` file again, but this time store the data as a list of dicts. For the key names, transform the column names into snake_case, i.e. all lowercase with underscores instead of spaces. Use the `zip()` method to construct the dicts. Store this data again as `employee_table`.
# 
# Feel free to copy-paste your previous parsing code to get you started here.

#%%

'''
length = len(employee_table)
# List of tuples (name, income)
names_salary = []

# Get header list
headers = employee_table[0]

# Get name (and rearrange) and income
for i in range(1, length-1):
    emData = employee_table[i][0]
     # Get name (unsplit, in reverse order)
    preName = emData[0].split(',')
    # Put name into standard order & remove spaces
    emName = str(preName[1].strip()) + " " + str(preName[0])
    # Get income
    emInc = emData[3]
    # Add tuple to list names_salary
    names_salary.append((emName, emInc))

print(names_salary)
#print(names_salary[0])



headerName = []
for i in headers[0]:
    # print(headers[i])
    if (i == 'NAME'):
        headerName.append(i)
    elif (i == 'EMPLOYEE ANNUAL SALARY'):
        headerName.append(i)    

print(headerName)

employee_records = dict(zip(headerName, names_salary))
employee_records

'''


#%%
'''

assert isinstance(employee_records, list)
assert all(isinstance(r, dict) for r in employee_records)
assert len(employee_records) == 5

'''


#%% [markdown]
# ### Dict I/O with JSON
#%% [markdown]
# We went over using delimited files to store tabular data, but there is also another, more flexible solution: JSON, which stands for JavaScript Object Notation. If your data consists of strings, numbers, dicts, and lists/tuples, then it can be stored as json.

#%%
# Import statements are normally done just once, at the top of the file
import json

#%% [markdown]
# `json.dump()` is used to write the data to a file:

#%%
json.dump(employee_records, open('employees.json', 'w'))


#%%
get_ipython().run_line_magic('cat', 'employees.json')

#%% [markdown]
# and `json.load()` is used to read a json file into a Python object:

#%%
json_data = json.load(open('employees.json'))
json_data

#%% [markdown]
# ## <font color='red'>EXERCISE 2.3.1</font>
# 
# The file `'nato.txt'` contains the
# [NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet),
# one item per line:
# ```
# Alpha
# Bravo
# Charlie
# Delta
# ...
# ```
# Create a lookup table for the NATO phonetic alphabet. Store it in a dict named `nato`. The key should be the first letter of each item in the list.

#%%



#%%
assert 'Zulu' == (nato.get('z') or nato.get('Z'))
assert len(nato) == 26

#%% [markdown]
# ## <font color='red'>EXERCISE 2.3.2</font>
# 
# Write a function `phonetic()` that translates a word or short sentence into the NATO phonetic alphabet. Your function should return a space-separated string. Ignore spaces and capitalization, but don't worry about punctuation. Use the table from the previous problem.

#%%



#%%
assert phonetic('Hello World') == 'Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta'

#%% [markdown]
# ## 3. List comprehensions and generator expressions
#%% [markdown]
# Often we have one sequence of values and we want to generate a new sequence by applying an operation to each item in the first. List comprehensions and generator expressions are compact ways to do this.
# 
# List comprehensions are specified inside square brackets, and immediately produce a list of the result.

#%%
items = ['spider', 'y', 'banana']
[item.upper() for item in items]


#%%
[len(item) for item in items]

#%% [markdown]
# Generator expressions are slightly different as they are evaluated 'lazily.' These are specified using round braces, and if they are beiing expressed as a function argument, they can be specified without any braces. These are most often used in the context of aggregations:

#%%
max(len(item) for item in items)


#%%
sorted(item.upper() for item in items)

#%% [markdown]
# ## <font color='red'>EXERCISE 3.1</font>
# 
# Assign the list `[3, 9, 12, 15]` to a variable. Use a list comprehension to store the square of each of these numbers in a variable named `squares`.

#%%
square = [3, 9, 12, 15]
squares = [num ** 2 for num in square]
print(squares)
#%%
assert squares == [9, 81, 144, 225]

#%% [markdown]
# ## 4. Application: Histograms
# 
# Often when we want to get a sense of some data we use summary statistics like mean, median, mode, max, min, and maybe standard deviation. A generalization of these quantities is to look at the entire distribution, and a graphical way to do that is with the Histogram.
# 
# ## Discrete vs continuous variables
# 
# Consider the process of rolling a six-sided die. Every "measurement" will result in one of exactly six different values. Now compare this to the process of measuring the height of everybody in this room. If we can be perfectly precise, each measurement will probably be different. The die roll is an example of a discrete variable, whereas height would be considered to be continuous.
# 
# ## Discrete variables: dice
# Let's work with the discrete case illustrated in the example: die rolling. Rolling a die of N sides can be thought of as randomly choosing a number between 1 and N. We can simulate a die roll using Python's `random` module:

#%%
import random

#%% [markdown]
# `random.randint()` returns a random ineger in range [a, b], including both endpoints (how unpythonic!). Execute the below block a few times and see what happens:
# 
# *Hint*: Use ctrl + Enter instead of shift + Enter to execute but not move to the next block.

#%%
random.randint(1,6)

#%% [markdown]
# ## <font color='red'>EXERCISE 4.1</font>
# Write a function `roll_dice()` that takes two arguments in this order: the number of rolls and the number of sides. This function should return a dict with the keys being the possible values for the die, and the values being the number of times that value came up, e.g. for 10 sides and 50 rolls, I might get
# ```
# {
#    1: 5,
#    2: 7,
#    ...
#    10: 4,
# }
# ```
# Ensure that all possible die rolls have a corresponding key even if there were zero rolls recorded.

#%%
import random



def roll_dice(rolls, sides):
    
    storage = dict()

    for i in range(1, sides + 1):
        storage[i] = 0
    # print(storage)
    
    rando = 0
    j = 0
    while (j < rolls):
        rando = random.randint(1, sides)
        # print(rando)
        storage[rando] += 1
        j+=1

    
    return storage    

roll_dice(5, 5)

#%%
die_rolls = roll_dice(5, 9)
assert isinstance(die_rolls, dict)
assert len(die_rolls) == 9

die_rolls = roll_dice(20, 9)
assert len(die_rolls) == 9
assert sum(die_rolls.values()) == 20

#%% [markdown]
# ### Aside: Strings are awesome
# 
# We know that we can use the `+` operator to concatenate strings, and multiplication is just repeated addition, so is it possible to multiply strings?

#%%
'#' * 8

#%% [markdown]
# Indeed it is!
# 
# Another common case is when you want a bunch of strings of various lengths to line up, e.g.
# ```
# Number of whirligigs produced
# 
# Boston:     42k
# New York:   124k
# Washington: 35k
# ```
# 
# Python provides the `ljust` and `rjust` string methods for this task. Just specify the length of the string you want:

#%%
padded = 'twelve'.rjust(12)
print(len(padded))
padded

#%% [markdown]
# ## <font color='red'>EXERCISE 4.2</font>
# Let's make a histogram. Write a function `text_histogram()` that accepts a one argument, a dict with integer values, and returns a string. For each key-value pair in the input dict, the output string should have a line containing the key, a colon character '`:`', and a number of hashmarks corresponding to the key's associated value. These lines must be in numeric/lexicographic order by their key. 
# 
# Once you have that working, make sure the start of the hashmarks is consistent for each line. Make sure this function works with the `roll_dice()` function from the previous exercise, and that the label justification works for dice with >10 sides.
# 
# Example:
# ```
# In [ ]:  histogram = text_histogram({'apple': 2, 'cat': 3, 'banana': 2})
#          print(histogram)
# Out[ ]:  apple : ##
#          banana: ##
#          cat   : ###
# ```
# 
# Hint: You can cast a variable to a string with `str()`, e.g.
# ```
# In [ ]:  num = 42
#          str(42)
# Out[ ]:  '42'
# ```

#%%

def text_histogram(ints):

    stg = []

    for k in ints.keys():
        # print(str(k) + ': ' + str(ints[k]))

        # if 

        strToAdd = str(k) + ': ' + str('#' * ints[k])

        # stg.append(str(k) + ': ' + str('#' * ints[k]))

    return stg

# text_histogram(dict([('one', 3), ('two', 4)]))    

#%%
die_rolls = roll_dice(30,12)
print(die_rolls)
print(text_histogram(die_rolls))


#%%



