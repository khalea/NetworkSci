# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# This is a quick review of some basic Python 3 features that you might use in your assignments. 
# Of course, this is far from being exhaustive. 
# 
# This tutorial follows a example-exercise format. Grey boxes are cells containing code - just place the cursor in 
# any code cell you want to execute, then press Shift + Enter on your keyboard or click on 'Cell -> Run'.
# 
# Some exercises have a block of `assert` statements after them. These are used for you to make sure you're on the right track and help me when grading. **Do not alter `assert` statements without instruction to do so.**
# 
# Official Python documentation - https://docs.python.org/3/
# 
# A popular book “A byte of python" - http://www.swaroopch.com/notes/Python
#%% [markdown]
# # Basics
#%% [markdown]
# ## Variables & printing
# Assigning values to variables, and printing them.

#%%
x = 0
print(x)

y = 'code'
print(y)

print(x, y)

#%% [markdown]
# In Jupyter notebook, executing a block with just a variable name or a function output will automatically print the value.

#%%
x + 4

#%% [markdown]
# ## <font color='red'>EXERCISE 1.1</font>
# Assign numerical values to two different variables, multiply them, store the result in a different variable and print it.

#%%
el = 4
em = 10
elem = el * em
print(elem)



#%% [markdown]
# ## "Concatenation"
# This will be a running theme for the data types we look at: how to combine two elements of the type. Numberic types (`int` and `float`) are immutable in Python.

#%%
x, y = 2, 3
z = x + y
print(z)


#%%
x = 2
x = x + 3
print(x)


#%%
x = 2
x += 3
print(x)

#%% [markdown]
# By analogy, you can probably figure out what the `-=` and `*=` operators do.
#%% [markdown]
# ## Comparison

#%%
4 < 5


#%%
4 > 5


#%%
# Need to use the double-equals for comparison
4 == 4


#%%
4 >= 4

#%% [markdown]
# ## <font color='red'>EXERCISE 1.2</font>
# It is true that for a given integer N, N times N (N squared) is greater than or equal to N. Assign an integer to a variable and show this condition evaluates to `True`.

#%%
n = 6
print(n*n >= n) # true
# print(n*n <= n) false

#%% [markdown]
# ## Numerical operations
# Division, modulo, exponent

#%%
5 / 2 # "Regular" division


#%%
5 // 2 # Integer division


#%%
5 % 2  # Modulo, returns the remainder


#%%
5 ** 2 # Exponentiation. This is 5 to the 2nd power.

#%% [markdown]
# Yes, the all of the shorthand assignment operators work like you would expect

#%%
x = 5
x **= 2
print(x)

#%% [markdown]
# ## <font color='red'>EXERCISE 1.3</font>
# Calculate the product of x and its reciprocal (1/x). Verify that the result is equal to 1.0

#%%
x = x * (1/x)
print(x)

#%% [markdown]
# ## Functions
# 
# Defining functions with `def`. Note the colon at the end of the arguments list.

#%%
def square(x):
    return x * x

square(4)

#%% [markdown]
# Functions can have optional arguments as well

#%%
def pow(x, exponent=2):
    result = x ** exponent
    return result

print( pow(4) )
print( pow(4,3) )

#%% [markdown]
# ## <font color='red'>EXERCISE 1.4</font>
# 
# Define a function called `is_even` that uses the modulo operator to return whether or not a given integer is even. You'll know your function works if the assertions in the block after run without error.

#%%
def is_even(x):
    if (x % 2 == 0):
        return True
    else:
        return False

#%%
assert is_even(6)
assert not is_even(5)

#%% [markdown]
# ## Conditional logic
# Note how the else-if is implemented in python – it is ‘elif’. 
# Also, notice the colon at the end of the conditions which is part of the syntax.

#%%
x = 0

if x == 1:
    print('x is 1')
elif x > 1:
    print('x is > 1')
else:
    print('x is < 1')


#%%
# Employing logical AND, OR within conditions

x = 1
y = 5
z = 5

if z >= x and z <= y:
    print("z lies within the interval [x,y]")

if z == x or z == y:
    print("z lies on the boundary of the interval [x,y]")

#%% [markdown]
# ## <font color='red'>EXERCISE 2.1</font>
# Write a function `compare()` that accepts two values, and prints if the first value is greater, less than, or equal to the second value.
# 
# **Example:**
# ```
# >>>  compare(4, 5)
# <<<  4 is less than 5
# ```

#%%
def compare(m, n):
    if (m > n):
        print(str(m) + " is greater than " + str(n))
    elif (m < n):
                print(str(m) + " is less than " + str(n))
    elif (m == n):
                print(str(m) + " is equal to " + str(n))


#%%
compare(4,5)
compare(5,4)
compare(7,7)

#%% [markdown]
# ## Ranges and `for`-loops
# 
# The `for` loop is by far the most useful and Pythonic loop. Again note the colon at the end of the loop statements.

#%%
for i in range(0,10):  
    print(i)

print("Final value:", i)

#%% [markdown]
# Often used in loops, the `range()` function allows iterating over a sequence of integers.
# 
# With one argument, `range(x)` gives integers in the half-open interval [0, x), that is, including zero and not including x.
# 
# By itself, `range()` gives an iterator:

#%%
# Not so descriptive
range(10)

#%% [markdown]
# We can use the `list()` constructor to return all of the values in a list:

#%%
list(range(10))

#%% [markdown]
# With two arguments, range(x, y) gives integers in the range [x, y):

#%%
list(range(0, 10))

#%% [markdown]
# With three arguments, range(x, y, z) gives integers in the range [x, y), counting by z:

#%%
list(range(1, 10, 2))

#%% [markdown]
# Counting backwards works too

#%%
list(range(10, 5, -1))

#%% [markdown]
# ## <font color='red'>EXERCISE 3.1</font>
# 
# Using a loop, calculate the sum of first 10 positive integers (zero is not positive, pay attention to the endpoints).

#%%
t = 0
for i in range(2, 20, 2):
    t += i
    print(t)

#%% [markdown]
# ## <font color='red'>EXERCISE 3.2</font>
# 
# Write a loop that goes through numbers 1 through 20, printing only the even numbers

#%%
for i in range(1, 20):
    if (i%2 == 0):
        print(i)

#%% [markdown]
# ## <font color='red'>EXERCISE 3.3</font>
# A natural number is prime if it has no positive divisors other than 1 and itself. Write a function `is_prime()` that checks if a number is prime. The assertions afterwards should pass.

#%%
def is_prime(d):

    prime = True

    if (d > 1):
        
        for i in range (2, d):
            if (d % i == 0):
                prime = False

    return prime

# print(is_prime(2))
# print(is_prime(4))
# print(is_prime(11))
# print(is_prime(12))


#%%
assert is_prime(11)
assert not is_prime(12)

#%% [markdown]
# ## <font color='red'>EXERCISE 3.4</font>
# The following function should return the minimal item from a sequence, but one or more of the assertions fail. Correct the bug in the function so that the assertions pass.
# 
# *Note:* this is a bug that I guarantee every single one of you will write at least once in this course.

#%%
def minimum(seq):
    my_min = 0
    for item in seq:
        if item < my_min:
            my_min = item
        return my_min


#%%
assert minimum(range(0,10)) == 0
assert minimum(range(9, 0, -1)) == 1


#%%



