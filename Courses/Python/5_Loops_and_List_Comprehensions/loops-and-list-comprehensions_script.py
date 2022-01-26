# %% [markdown]
# # Loops
# 
# Loops are a way to repeatedly execute some code. Here's an example:

# %% [code]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

# %% [markdown]
# The ``for`` loop specifies 
# - the variable name to use (in this case, `planet`)
# - the set of values to loop over (in this case, `planets`)
# 
# You use the word "``in``" to link them together.
# 
# The object to the right of the "``in``" can be any object that supports iteration. Basically, if it can be thought of as a group of things, you can probably loop over it. In addition to lists, we can iterate over the elements of a tuple:

# %% [code]
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product

# %% [markdown]
# You can even loop through each character in a string:

# %% [code]
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')        

# %% [markdown]
# ### range()
# 
# `range()` is a function that returns a sequence of numbers. It turns out to be very useful for writing loops.
# 
# For example, if we want to repeat some action 5 times:

# %% [code]
for i in range(5):
    print("Doing important work. i =", i)

# %% [markdown]
# ## ``while`` loops
# The other type of loop in Python is a ``while`` loop, which iterates until some condition is met:

# %% [code]
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 1

# %% [markdown]
# The argument of the ``while`` loop is evaluated as a boolean statement, and the loop is executed until the statement evaluates to False.

# %% [markdown]
# # List comprehensions
# 
# List comprehensions are one of Python's most beloved and unique features. The easiest way to understand them is probably to just look at a few examples:

# %% [code]
squares = [n**2 for n in range(10)]
squares

# %% [markdown]
# Here's how we would do the same thing without a list comprehension:

# %% [code]
squares = []
for n in range(10):
    squares.append(n**2)
squares

# %% [markdown]
# We can also add an `if` condition:

# %% [code]
short_planets = [planet for planet in planets if len(planet) < 6]
short_planets

# %% [markdown]
# (If you're familiar with SQL, you might think of this as being like a "WHERE" clause)
# 
# Here's an example of filtering with an `if` condition *and* applying some transformation to the loop variable:

# %% [code]
# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

# %% [markdown]
# People usually write these on a single line, but you might find the structure clearer when it's split up over 3 lines:

# %% [code]
[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

# %% [markdown]
# (Continuing the SQL analogy, you could think of these three lines as SELECT, FROM, and WHERE)
# 
# The expression on the left doesn't technically have to involve the loop variable (though it'd be pretty unusual for it not to). What do you think the expression below will evaluate to? Press the 'output' button to check. 

# %% [code] {"_kg_hide-output":true}
[32 for planet in planets]

# %% [markdown]
# List comprehensions combined with functions like `min`, `max`, and `sum` can lead to impressive one-line solutions for problems that would otherwise require several lines of code. 
# 
# For example, compare the following two cells of code that do the same thing.
# 

# %% [code] {"jupyter":{"outputs_hidden":true}}
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

# %% [markdown]
# Here's a solution using a list comprehension:

# %% [code] {"jupyter":{"outputs_hidden":true}}
def count_negatives(nums):
    return len([num for num in nums if num < 0])

# %% [markdown]
# Much better, right?
# 
# Well if all we care about is minimizing the length of our code, this third solution is better still!

# %% [code] {"jupyter":{"outputs_hidden":true}}
def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])

# %% [markdown]
# Which of these solutions is the "best" is entirely subjective. Solving a problem with less code is always nice, but it's worth keeping in mind the following lines from [The Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python):
# 
# > Readability counts.  
# > Explicit is better than implicit.
# 
# So, use these tools to make compact readable programs. But when you have to choose, favor code that is easy for others to understand.

# %% [markdown]
# # Your Turn
# 
# You know what's next -- we have some **[fun coding challenges](https://www.kaggle.com/kernels/fork/1275177)** for you! This next set of coding problems is shorter, so try it now.

# %% [markdown]
# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
