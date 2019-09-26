# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../Week4'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Week 3: Tutorial + Exercises
# 
# Contents:
# 
# 1. [Conditionals](#2.-Conditionals)
# 2. [Lists](#3.-Lists)
# 3. [Loops](#4.-Loops)
# 4. [Tuples](#5.-Tuples)
# 5. [Dictionaries](#6.-Dictionaries)
# 6. [Combining Data Types](#7.-Combining-Data-Types)
# 
#%% [markdown]
# ## Printing and inspecting variables
# 
# In Jupyter notebooks, we have two different ways of inspecting variables. Python's `print()` function is useful as always:

#%%
my_str = 'Hello'
my_int = 16

print(my_str)
print(my_int)

#%% [markdown]
# We can also just execute a cell with the name of a variable:

#%%
my_str

#%% [markdown]
# The big difference here between the two approaches is that `print()` statements can output multiple items per cell, while the latter approach will only display the last variable named. Observe:

#%%
my_str
my_int

#%% [markdown]
# As opposed to the first example using `print()`, this only outputs the last value.
#%% [markdown]
# # 2. Conditionals
# 
# "Conditionals" is a fancy word for if-statements. If you've ever done any programming, you are surely aware of the if-then-else construction. In Python it's done as follows:

#%%
number_of_apples = 5

if number_of_apples < 1:
    print('You have no apples')
elif number_of_apples == 1:
    print('You have one apple')
elif number_of_apples < 4:
    print('You have a few apples')
else:
    print('You have many apples!')

#%% [markdown]
# You can change `number_of_apples` and re-run the previous cell in order to get the different possible outputs.
# 
#%% [markdown]
# # 3. Lists
# 
# One of Python's most versatile and ubiquitous data types is the List ([Python documentation](https://docs.python.org/3/library/stdtypes.html#list)). This is an **ordered**, **mutable**, **collection** of **non-unique** items.
# 
# ## 3.1 Ordered
# 
# By *ordered*, we mean that the items are addressed by their *index* in the collection:

#%%
student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[1]

#%% [markdown]
# Indices in Python start at zero, so the head of the list has index 0:

#%%
student_names[0]

#%% [markdown]
# We can get the last item in a list by using negative indexing:

#%%
student_names[-1]

#%% [markdown]
# Lists can also be *sliced* to get a subset of the list items:

#%%
student_names[0:2]


#%%
student_names[1:3]

#%% [markdown]
# When slicing from the beginning of the list, or to the end of the list, we can leave out the index:

#%%
student_names[:2]


#%%
student_names[2:]

#%% [markdown]
# ## 3.2 Mutable
# 
# By *mutable*, we mean that the list can be changed by adding or removing items. We most often add items to the end of the list with `.append()`:

#%%
student_names.append('Esther')
student_names

#%% [markdown]
# But we can also add items at any arbitrary index with `.insert()`:

#%%
student_names.insert(2, 'Xavier')
student_names

#%% [markdown]
# We can delete items with the `del` keyword:

#%%
del student_names[2]
student_names

#%% [markdown]
# ## 3.3 Non-unique
# 
# Note that nothing stops us from repeatedly adding the same name to this list:

#%%
student_names.append('Esther')
student_names.append('Esther')
student_names

#%% [markdown]
# If you want a collection where uniqueness is enforced, you should look towards
# [sets](https://docs.python.org/3/library/stdtypes.html#set)
# or
# [dictionaries](https://docs.python.org/3/library/stdtypes.html#dict).
# 
# ## 3.4 Collection
# 
# A collection refers to a data type consisting of more than one values. Lists are one type of collection, but there are others such as tuples, sets, and dictionaries.
# 
# When naming your variables that contain lists, you should use plural nouns, *e.g.* `student_names` in the previous example. In contrast, single values should be named with singular nouns, *e.g.* `my_str` in the first section. This helps you and others reading your code keep straight which variables are collections and which are single items, and also helps when writing loops as shown in the next section.
#%% [markdown]
# # 4. Loops
# 
# If you're coming from another programming language, you're probably aware of more than one type of loop. In Python, we focus on one type of loop in particular: the for-loop. The for-loop iterates through a collection of items, executing its code for each item:

#%%
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

for student_name in student_names:
    print('Hello ' + student_name + '!')

#%% [markdown]
# ## 4.1 Naming conventions
# 
# Note the naming convention being used in the for-in construction:
# 
#     for student_name in student_names:
#     
# By using a plural noun for the collection `student_names`, we automatically have good name for the individual items in the collection: `student_name`. The tutorials in this book use this naming convention when possible as it makes clear to the reader which variable is the "loop variable" that changes value between iterations of the loop body.
#%% [markdown]
# ## 4.2 Loops, lists, and conditionals
# 
# One extremely common type of task when working with data is the *filtering task*. In abstract, this task involves looping over one collection, checking each item for some criterion, then adding items that meet the criterion to another collection.
# 
# In the following example, we'll create a list of just the "long" names from the `student_names` list. Long names are those that contain more than four characters. You will often see and write code that looks like the following in this book's tutorials:

#%%
# Initialize an empty list and add to it the
# student names containing more than four characters
long_names = []
for student_name in student_names:
    # This is our criterion
    if len(student_name) > 4:
        long_names.append(student_name)

long_names

#%% [markdown]
# ## <font color='red'>EXERCISE 1</font>
# 
# Make a list of 10 numbers within the range (1 - 100)
# 
# Write code which first finds the average of the values within your list, and prints out any values above the average. 
# 
# Check your work to ensure your function is producing the right result. 

#%%
import random

arr = []
rand = 0
total = 0
i = 0
while i < 10:
    rand = random.randint(1, 100)
    arr.append(rand)
    total += rand
    i += 1
avg = total / 10

for i in arr:
    if (i > avg):
        print(str(i) + " is greater than the avg " +  str(avg))

print(arr)

#%% [markdown]
# ## 4.3 Nested loops
# 
# Loops can be "nested" inside one another. This often occurs when we want to match up items from one collection to items from the same or another collection. Here let's create a list of all possible pairs of students:

#%%
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs

#%% [markdown]
# Note here that instead of just adding names to the `student_pairs` list, we are adding *tuples* `(student_name, language)`. This means each item in the list is a 2-tuple:

#%%
student_pairs[0]

#%% [markdown]
# We'll talk more about tuples in the next section. The second thing to notice is that we're including pairs with two of the same student. Suppose we wish to exclude those. We can accomplish this by adding an if-statement in the second for-loop to *filter* out those repeats:

#%%
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        # This is the criterion we added
        if student_name_0 != student_name_1:
            student_pairs.append(
                (student_name_0, student_name_1)
            )

student_pairs

#%% [markdown]
# And now the list has no repeats.
#%% [markdown]
# # 5. Tuples
# 
# Even experienced Python users often are confused about the difference between tuples and lists, so definitely read this short section even if you have some experience.
# 
# Tuples ([documentation](https://docs.python.org/3/library/stdtypes.html#tuple)) are superficially similar to lists as they are an ordered collection of non-unique items:

#%%



#%%
student_grade = ('Alice', 'Spanish', 'A-')
student_grade


#%%
student_grade[0]

#%% [markdown]
# ## 5.1 Immutable
# 
# The big difference from lists is that tuples are **immutable**. Each of the following cells should raise an exception.

#%%
student_grade.append('IU Bloomington')


#%%
del student_grade[2]


#%%
student_grade[2] = 'C'

#%% [markdown]
# This immutability makes tuples useful when **index matters**. In this example, the index matters semantically: index 0 is the student's name, index 1 is the course name, and index 2 is their grade in the course. The inability to insert or append items to the tuple means that we are certain that, say, the course name won't move around to a different index.
# 
# ## 5.2 Unpacking
# 
# Tuples' immutability makes them useful for *unpacking*. At its simplest, tuple unpacking allows the following:

#%%
student_grade = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)

#%% [markdown]
# While occasionally useful on its own, tuple unpacking is most useful when used with loops. Consider the following piece of code, which congratulates students on getting good grades:

#%%
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)

#%% [markdown]
# Compare this to the same code using indices:

#%%
for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations', student_grade[0],
              'on getting an', student_grade[2],
              'in', student_grade[1])

#%% [markdown]
# Tuple unpacking allows us to easily refer to this structured data by semantic names instead of having to keep the indices straight. The second example, while functionally identical, is more difficult to write and harder still to read.
#%% [markdown]
# # 6. Dictionaries
# 
# The next type of collection is much different than the previous two, but is among the most powerful tools in Python: the dictionary ([documentation](https://docs.python.org/3/library/stdtypes.html#dict)). The dictionary is an **unordered**, **mutable**, collection of **unique** items. In other languages these are called maps, mappings, hashmaps, hashes, or associative arrays.
# 
# ## 6.1 Unordered
# 
# By unordered, we mean that dictionary items aren't referred to by their position, or index, in the collection. Instead, dictionary items have *keys*, each of which is associated with a value. Here's a very basic example:

#%%
foreign_languages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}

#%% [markdown]
# Here the student names are the keys and the students' foreign language courses are the values. So to see Carol's foreign language, we use the key -- her name -- instead of an index:

#%%
foreign_languages['Carol']

#%% [markdown]
# Trying to get the value for a key that does not exist in the dictionary results in a `KeyError`:

#%%
foreign_languages['Zeke']

#%% [markdown]
# We can check if a particular key is in a dictionary with the `in` keyword:

#%%
'Zeke' in foreign_languages


#%%
'Alice' in foreign_languages

#%% [markdown]
# Note that keys are case-sensitive:

#%%
'alice' in foreign_languages

#%% [markdown]
# ## 6.2 Mutable
# 
# We can add, delete, and change entries in a dictionary:

#%%
# Add an entry that doesn't exist
foreign_languages['Esther'] = 'French'
foreign_languages


#%%
# Delete an entry that exists
del foreign_languages['Bob']
foreign_languages


#%%
# Change an entry that does exist
foreign_languages['Esther'] = 'Italian'
foreign_languages

#%% [markdown]
# ## 6.3 Unique
# Note that the syntax for adding an entry that does not exist and changing an existing entry are the same. When assigning a value to a key in a dictionary, it adds the key if it doesn't exist, or else updates the value for the key if it does exist. As a consequence, keys are necessarily *unique* -- there can't be more than one element with the same key in a dictionary.
#%% [markdown]
# ## 6.4 Looping over dictionaries
# 
# While not performed as often as with lists, it is possible to loop over entries in a dictionary. There are two ways to accomplish this task:

#%%
for key in foreign_languages:
    value = foreign_languages[key]
    print(key, 'is taking', value)


#%%
# print(foreign_languages.items())
for student, subject in foreign_languages.items():
    print(student, 'is taking', subject)

#%% [markdown]
# Here I'm using variables named `key` and `value` to show the general principle. When you write loops over dictionaries in your own code, you should use descriptive names as opposed to `key` and `value`.
#%% [markdown]
# ## <font color='red'>EXERCISE 2</font>
# 
# Write code to loop through the 'foreign_languages' dictionary and print out the names of the students who **do not** take Spanish. 

#%%
for s in foreign_languages.keys():
    if (foreign_languages[s] != "Spanish"):
        print(s)

#%% [markdown]
# ## 6.5 Dictionaries as records
# 
# In `foreign_languages` we have paired data -- every name is associated with a subject. Dictionaries are also often used to contain several different data about a single entity. To illustrate this subtle difference, let's take a look at one item from `student_grades`:

#%%
student_grade = ('Alice', 'Spanish', 'A')

#%% [markdown]
# Here we know that the items in each of these tuples is a name, subject, and grade:

#%%
student_name, subject, grade = student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)

#%% [markdown]
# We could instead represent this data as a dictionary and use it as such. A dictionary of information describing a single item is often referred to as a *record*:

#%%
record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])

#%% [markdown]
# While the code is slightly longer, there is absolutely no ambiguity here about matching up indices and what each value represents. This is also useful in contexts where some of the fields might be optional.
#%% [markdown]
# # 7. Combining Data Types
# 
# In most of these simple examples we've worked with collections of simple values like strings and numbers, however data analysis often involves working with complex data, where each item of interest has several data associated with it. These complex data are often represented as collections of collections, *e.g.,* lists of dictionaries.
# 
# Choosing the appropriate data types for a given problem will make it easier for you to write bug-free code and will make your code easier for others to read, but identifying the best data types is a skill gained through experience. Some of the commonly-used combination data types are illustrated below, but this is hardly exhaustive.
# 
# ## 7.1 List of tuples
# 
# We've actually seen this one before. Consider the `student_grades` data from the earlier example on tuple unpacking:

#%%
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

#%% [markdown]
# This is a list of tuples:

#%%
student_grades[1]

#%% [markdown]
# and we can work with the individual tuples as such:

#%%
student_grades[1][2]

#%% [markdown]
# ## 7.2 List of dictionaries
# 
# In the section on dictionaries, we explored how dictionaries are often used to contain several data about a single entity, and each such dictionary is sometimes called a *record*. Let's convert the list of tuples `student_grades` into a list of records `student_grade_records`:

#%%
student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records

#%% [markdown]
# Now each item in the list is a dictionary:

#%%
student_grade_records[1]

#%% [markdown]
# and we can work with the individual records as such:

#%%
student_grade_records[1]['grade']

#%% [markdown]
# This list-of-dicts is often used to represent data from a database or an API. Let's use this data to write our code congratulating students for good grades, as we did in the section on tuple unpacking:

#%%
for record in student_grade_records:
    if record['grade'].startswith('A'):
        print('Congratulations', record['name'], 
              'on getting an', record['grade'], 
              'in', record['subject'])

#%% [markdown]
# ## 7.3 Dictionary of dictionaries
# 
# The list of dictionaries is very useful when dealing with non-unique data; in the previous example each student might have several grades from different classes. But sometimes we want to refer to the data by a particular name or key. In this case, we can use a dictionary whose values are records, *i.e.*, other dictionaries.
# 
# Let's use data from `student_grades` again, but assume we just want the foreign language grade so we can use the students name as a key:

#%%
foreign_language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    foreign_language_grades[student_name] = record
    
foreign_language_grades

#%% [markdown]
# Now we can refer to these by student name:

#%%
foreign_language_grades['Alice']

#%% [markdown]
# And we can get the individual data that we care about:

#%%
foreign_language_grades['Alice']['grade']

#%% [markdown]
# ## 7.4 Dictionary with tuple keys
# 
# It is occasionally useful to key dictionaries on more than one data. Dictionaries can use any immutable object as a key, which includes tuples. Continuing with our student grades example, we may want the keys to be the student name and subject:

#%%
student_course_grades = {}
for student_name, subject, grade in student_grades:
    student_course_grades[student_name, subject] = grade
    
student_course_grades

#%% [markdown]
# Now we can represent all of a student's grades:

#%%
student_course_grades['Alice', 'Math'] = 'A'
student_course_grades['Alice', 'History'] = 'B'


#%%
student_course_grades

#%% [markdown]
# ## 7.5 Another dictionary of dictionaries
# 
# Let's take advantage of the fact that, for a particular student, we often want to get subject-grade pairs, *i.e.* a report card. We can create a dictionary with student names as keys and the values being dictionaries of subject-grade pairs. In this case we need to do a bit of checking; that step is commented below:

#%%
student_report_cards = {}
for student_name, subject, grade in student_grades:
    # If there is no report card for a student,
    # we need to create a blank one
    if student_name not in student_report_cards:
        student_report_cards[student_name] = {}
    student_report_cards[student_name][subject] = grade


#%%
student_report_cards

#%% [markdown]
# The advantage of this extra work is that we can now easily have multiple grades per student:

#%%
student_report_cards['Alice']['Math'] = 'A'
student_report_cards['Alice']['History'] = 'B'


#%%
student_report_cards

#%% [markdown]
# And we can easily fetch a student's "report card":

#%%
student_report_cards['Alice']

#%% [markdown]
# ## <font color='red'>EXERCISE 3</font>
# 
# Make a collection of records, one for each student. Then write code to loop through your records and print the information (name, subject, grade) for each student.
# 
# You may use whichever type (list, dictionary, tuple) of data structure you wish to contain the records, but justify your decision in the comments.
# 
# Print the students in alphabetical order first according to class subject, then according to class time. 
# 
# Consider that what you are doing is building networks - we will learn much more effective ways to do this later, but everything builds on these concepts.
# 
# -
# 
# Kelly P, Spanish, 9:30
# 
# Jacob Y, Portuguese, 2:15
# 
# Kata T, German, 10:00
# 
# Breesha H, Italian, 2:15
# 
# Antawn O, Russian, 9:30
# 
# Petra N, Portuguese, 2:15
# 
# Rodger I, Italian, 2:15
# 
# Fillip S, Spanish, 9:30
# 
# Tate S, Spanish, 9:30
# 
# Devi O, Italian, 2:15
# 
# Irene C, German, 10:00
# 
# Lars O, Russian, 9:30
# 
# Ye O, German, 10:00 
# 
# Thomas L, Portuguese, 2:15
# 
# 

#%%

# I chose a dictionary of lists because in this case, it is a
# pretty simple structure for storing one class name & its time
# I could also have done A list of dicts with structure:
# name : {course : coursename, time: classtime} but 
# that would have been a lot more typing :)

student_course = {
    "Kelly P" : ["Spanish", "9:30"],
    "Jacob Y" : ["Portuguese", "2:15"],
    "Kata T" : ["German", "10:00"],
    "Breesha H" : ["Italian", "2:15"],
    "Antawn O" : ["Russian", "9:30"],
    "Petra N" : ["Portuguese", "2:15"],
    "Rodger I" : ["Italian", "2:15"],
    "Filip S" : ["Spanish", "9:30"],
    "Tate S" : ["Spanish", "9:30"],
    "Devi O" : ["Italian", "2:15"],
    "Irene C" : ["German", "10:00"],
    "Lars O" : ["Russian", "9:30"],
    "Ye O" : ["German", "10:00"],
    "Thomas L" : ["Portuguese", "2:15"]

}

students = []
for i in student_course.keys():
    students.append(i)

# Sort array alphabetically
students.sort()
# students

for i in students:
    course = student_course[i][0]
    time = student_course[i][1]
    print("Student: " + i + " - Course: "  + course + " - Time:  " + time + "\n")

#%% [markdown]
# ## <font color='red'>EXERCISE 4</font>
# 
# An anonymous wealthy individual has offered the students 100k each if they sign up for another language! It is most likely some sort of trap (because who does that?) But of course, they all accept (because who wouldn't?) Their schedules now look like this: 
# 
# 
# Kelly P: 
# * Spanish, 9:30
# * Italian, 2:15
# 
# Jacob Y:
# * Portuguese, 2:15
# * Russian, 9:30
# 
# Kata T:
# * German, 10:00
# * Italian, 2:15
# 
# Breesha H:
# * Italian, 2:15
# * Spanish, 9:30
# 
# Antawn O:
# * Russian, 9:30
# * Portuguese, 2:15
# 
# Petra N:
# * Portuguese, 2:15
# * Italian, 2:15
# 
# Rodger I:
# * Italian, 2:15
# * German, 10:00
# 
# Fillip S:
# * Spanish, 9:30
# * Russian, 9:30
# 
# Tate S: 
# * Spanish, 9:30
# * Portuguese, 2:15
# 
# Devi O:
# * Italian, 2:15
# * German, 10:00
# 
# Irene C:
# * German, 10:00
# * Italian, 2:15
# 
# Lars O:
# * Russian, 9:30
# * Portuguese, 2:15
# 
# Ye O:
# * German, 10:00 
# * Italian, 2:15
# 
# Thomas L:
# * Portuguese, 2:15
# * German, 10:00 
# 
# 
# 
# Store this updated information in the data structure of your choosing - again, justifying your decision in the comments. 
# You may have noticed that there are some schedule conflicts! Write code which checks each student's schedule for conflicts - if there is a conflict, change the second class in the list to another class whose time is at least 2 hours before or after the first class. 
# 

#%%

# Here i'm going with a dictionary with arrays of arrays.
# This way, courses and times are mutable & easily searchable with indexing

studentCourses = {
    "Kelly P" : [
        ["Spanish" , "9:30"],
        ["Italian" , "2:15"]
    ],
    "Jacob Y" : [
        ["Portuguese" , "2:15"],
        ["Russian" , "9:30"]
    ],
    "Kata T" : [
        ["German" , "10:00"],
        ["Italian" , "2:15"]
    ],
    "Breesha H" : [
        ["Italian" , "2:15"],
        ["Spanish" , "9:30"]
    ], 
    "Antawn O" : [
        ["Russian" , "9:30"],
        ["Portuguese" , "2:15"]
    ],
    "Petra N" : [
        ["Portuguese" , "2:15"],
        ["Italian" , "2:15"]
    ],
    "Rodger I" : [
        ["Italian" , "2:15"],
        ["German" , "10:00"]
    ],
    "Filip S" : [
        ["Spanish" , "9:30"],
        ["Russian" , "9:30"]
    ],
    "Tate S" : [
        ["Spanish" , "9:30"],
        ["Portuguese" , "2:15"]
    ],
    "Devi O" : [
        ["Italian" , "2:15"],
        ["German" , "10:00"]
    ], 
    "Irene C" : [
        ["German" , "10:00"],
        ["Italian" , "2:15"]
    ],
    "Lars O" : [
        ["Russian" , "9:30"],
        ["Portuguese" , "2:15"]
    ],
    "Ye O" : [
        ["German" , "10:00"],
        ["Italian" , "2:15"]
    ],
    "Thomas L" : [
        ["Portuguese", "2:15"],
        ["German", "10:00"]
    ]
}

# You may have noticed that there are some schedule conflicts! Write code which checks each student's schedule for conflicts - if there is a conflict, change the second class in the list to another class whose time is at least 2 hours before or after the first class. 

for s in studentCourses:
    # print(studentCourses[s][0][1])
    studentFirstCourse = studentCourses[s][0]
    studentSecCourse = studentCourses[s][1]
    if (studentFirstCourse[1] == studentSecCourse[1]):
        print("Course times overlap for: " + s)
        print(studentFirstCourse)
        print(studentSecCourse)
        # Extract hour from string
        time2 = studentSecCourse[1].split(":")[0]
        print(time2)
        # Add/Subtract 2 from that course time ^^^ 
        # No classes before 8am - Add 2hrs if 9am or earlier
        if (int(time2) in range(8, 10)):
            studentSecCourse[1] = int(time2)+2
        else: 
            studentSecCourse[1] = int(time2)-2

        print(studentSecCourse)
        # Works but need to reformat!


#%% [markdown]
# ## <font color='red'>EXERCISE 5</font>
# 
# It's the end of the term, and final grades are due.
# Write code which goes though the students, and assigns each student random grade in each of their classes. The grades should be in the range A through F (do not worry about +/-).
# 
# Then, print out the list of grades for each class in the format "Student Name: Student Grade"
# 
# *Pay careful attention to these instructions*: 
# * The classes should be listed in alphabetical order. 
# * Within the listing for each class, the grades should be printed in descending order.
# * The grades should be right-justified to all start at a consistant point, based on the length of the students' names. 
# 
# 
# 
# 

#%%
import random as random
studentCourses = {
    "Kelly P" : [
        ["Spanish" , "9:30"],
        ["Italian" , "2:15"]
    ],
    "Jacob Y" : [
        ["Portuguese" , "2:15"],
        ["Russian" , "9:30"]
    ],
    "Kata T" : [
        ["German" , "10:00"],
        ["Italian" , "2:15"]
    ],
    "Breesha H" : [
        ["Italian" , "2:15"],
        ["Spanish" , "9:30"]
    ], 
    "Antawn O" : [
        ["Russian" , "9:30"],
        ["Portuguese" , "2:15"]
    ],
    "Petra N" : [
        ["Portuguese" , "2:15"],
        ["Italian" , "2:15"]
    ],
    "Rodger I" : [
        ["Italian" , "2:15"],
        ["German" , "10:00"]
    ],
    "Filip S" : [
        ["Spanish" , "9:30"],
        ["Russian" , "9:30"]
    ],
    "Tate S" : [
        ["Spanish" , "9:30"],
        ["Portuguese" , "2:15"]
    ],
    "Devi O" : [
        ["Italian" , "2:15"],
        ["German" , "10:00"]
    ], 
    "Irene C" : [
        ["German" , "10:00"],
        ["Italian" , "2:15"]
    ],
    "Lars O" : [
        ["Russian" , "9:30"],
        ["Portuguese" , "2:15"]
    ],
    "Ye O" : [
        ["German" , "10:00"],
        ["Italian" , "2:15"]
    ],
    "Thomas L" : [
        ["Portuguese", "2:15"],
        ["German", "10:00"]
    ]
}


grades = ["A", "B", "C", "D", "F"]
courses = {}

for s in studentCourses:
    studentFirstCourse = studentCourses[s][0]
    studentSecCourse = studentCourses[s][1]
    # Name print(s)
    # print(studentSecCourse)

    # Generate random grade
    thisGrade = grades[random.randint(0, len(grades)-1)]
    # print(thisGrade)

    # Add to course dictionary: "className" : [[student, grade]]
    for c in studentCourses[s]:
        # print(s, c)
        if (c[0] not in courses.keys()):
            courses[c[0]] = [[s, thisGrade]]
        else:
            courses[c[0]].append([s, thisGrade])

# Sort Classes in Alphabetical Order
# Print Later
sortedCourse = []
for cs in courses:
    sortedCourse.append(cs)
sortedCourse.sort()
# print(sortedCourse)

# Array of grades??

for cs in sortedCourse:
    for s in courses[cs]:
        print("Course:", cs, " Student Name:", s[0], " Grade:", s[1])

    

# Formatting!!