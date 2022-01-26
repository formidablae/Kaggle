# %% [markdown]
# # Lists
# 
# Lists in Python represent ordered sequences of values. Here is an example of how to create them:

# %% [code]
primes = [2, 3, 5, 7]

# %% [markdown]
# We can put other types of things in lists:

# %% [code]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# %% [markdown]
# We can even make a list of lists:

# %% [code]
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# %% [markdown]
# A list can contain a mix of different types of variables:

# %% [code]
my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

# %% [markdown]
# ## Indexing
# 
# You can access individual list elements with square brackets.
# 
# Which planet is closest to the sun? Python uses *zero-based* indexing, so the first element has index 0.

# %% [code]
planets[0]

# %% [markdown]
# What's the next closest planet?

# %% [code]
planets[1]

# %% [markdown]
# Which planet is *furthest* from the sun?
# 
# Elements at the end of the list can be accessed with negative numbers, starting from -1:

# %% [code]
planets[-1]

# %% [code]
planets[-2]

# %% [markdown]
# ## Slicing
# 
# What are the first three planets? We can answer this question using *slicing*:

# %% [code]
planets[0:3]

# %% [markdown]
# `planets[0:3]` is our way of asking for the elements of `planets` starting from index 0 and continuing up to *but not including* index 3.
# 
# The starting and ending indices are both optional. If I leave out the start index, it's assumed to be 0. So I could rewrite the expression above as:

# %% [code]
planets[:3]

# %% [markdown]
# If I leave out the end index, it's assumed to be the length of the list.

# %% [code]
planets[3:]

# %% [markdown]
# i.e. the expression above means "give me all the planets from index 3 onward".
# 
# We can also use negative indices when slicing:

# %% [code]
# All the planets except the first and last
planets[1:-1]

# %% [code]
# The last 3 planets
planets[-3:]

# %% [markdown]
# ## Changing lists
# 
# Lists are "mutable", meaning they can be modified "in place".
# 
# One way to modify a list is to assign to an index or slice expression.
# 
# For example, let's say we want to rename Mars:

# %% [code]
planets[3] = 'Malacandra'
planets

# %% [markdown]
# Hm, that's quite a mouthful. Let's compensate by shortening the names of the first 3 planets.

# %% [code]
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

# %% [markdown]
# ## List functions
# 
# Python has several useful functions for working with lists.
# 
# `len` gives the length of a list:

# %% [code]
# How many planets are there?
len(planets)

# %% [markdown]
# `sorted` returns a sorted version of a list:

# %% [code]
# The planets sorted in alphabetical order
sorted(planets)

# %% [markdown]
# `sum` does what you might expect:

# %% [code]
primes = [2, 3, 5, 7]
sum(primes)

# %% [markdown]
# We've previously used the `min` and `max` to get the minimum or maximum of several arguments. But we can also pass in a single list argument.

# %% [code]
max(primes)

# %% [markdown]
# ## Interlude: objects
# 
# I've used the term 'object' a lot so far - you may have even read that *everything* in Python is an object. What does that mean?
# 
# In short, objects carry some things around with them. You access that stuff using Python's dot syntax.
# 
# For example, numbers in Python carry around an associated variable called `imag` representing their imaginary part. (You'll probably never need to use this unless you're doing some very weird math.)

# %% [code]
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

# %% [markdown]
# The things an object carries around can also include functions. A function attached to an object is called a **method**. (Non-function things attached to an object, such as `imag`, are called *attributes*).
# 
# For example, numbers have a method called `bit_length`. Again, we access it using dot syntax:

# %% [code]
x.bit_length

# %% [markdown]
# To actually call it, we add parentheses:

# %% [code]
x.bit_length()

# %% [markdown]
# > **Aside:** You've actually been calling methods already if you've been doing the exercises. In the exercise notebooks `q1`, `q2`, `q3`, etc. are all objects which have methods called `check`, `hint`, and `solution`.
# 
# In the same way that we can pass functions to the `help` function (e.g. `help(max)`), we can also pass in methods:

# %% [code]
help(x.bit_length)

# %% [markdown]
# <!-- TODO:
# dir?
# A useful builtin method for interacting with objects is `dir`. `dir` asks: what are the names of all the things (methods, and attributes) that this object is carrying around?
# help(x)?
# -->
# 
# The examples above were utterly obscure. None of the types of objects we've looked at so far (numbers, functions, booleans) have attributes or methods you're likely ever to use.
# 
# But it turns out that lists have several methods which you'll use all the time.

# %% [markdown]
# ## List methods

# %% [markdown]
# `list.append` modifies a list by adding an item to the end:

# %% [code]
# Pluto is a planet darn it!
planets.append('Pluto')

# %% [markdown]
# Why does the cell above have no output? Let's check the documentation by calling `help(planets.append)`.
# 
# > **Aside:** `append` is a method carried around by *all* objects of type list, not just `planets`, so we also could have called `help(list.append)`. However, if we try to call `help(append)`, Python will complain that no variable exists called "append". The "append" name only exists within lists - it doesn't exist as a standalone name like builtin functions such as `max` or `len`.

# %% [code]
help(planets.append)

# %% [markdown]
# The `-> None` part is telling us that `list.append` doesn't return anything. But if we check the value of `planets`, we can see that the method call modified the value of `planets`:

# %% [code]
planets

# %% [markdown]
# `list.pop` removes and returns the last element of a list:

# %% [code]
planets.pop()

# %% [code]
planets

# %% [markdown]
# ### Searching lists
# 
# Where does Earth fall in the order of planets? We can get its index using the `list.index` method.

# %% [code]
planets.index('Earth')

# %% [markdown]
# It comes third (i.e. at index 2 - 0 indexing!).
# 
# At what index does Pluto occur?

# %% [code] {"tags":["raises-exception"]}
planets.index('Pluto')

# %% [markdown]
# Oh, that's right...
# 
# To avoid unpleasant surprises like this, we can use the `in` operator to determine whether a list contains a particular value:

# %% [code]
# Is Earth a planet?
"Earth" in planets

# %% [code]
# Is Calbefraques a planet?
"Calbefraques" in planets

# %% [markdown]
# There are a few more interesting list methods we haven't covered. If you want to learn about all the methods and attributes attached to a particular object, we can call `help()` on the object itself. For example, `help(planets)` will tell us about *all* the list methods: 

# %% [code] {"_kg_hide-output":true}
help(planets)

# %% [markdown]
# Click the "output" button to see the full help page. Lists have lots of methods with weird-looking names like `__eq__` and `__iadd__`. Don't worry too much about these for now. (You'll probably never call such methods directly. But they get called behind the scenes when we use syntax like indexing or comparison operators.) The most interesting methods are toward the bottom of the list (`append`, `clear`, `copy`, etc.).

# %% [markdown]
# ## Tuples
# 
# Tuples are almost exactly the same as lists. They differ in just two ways.
# 
# **1:** The syntax for creating them uses parentheses instead of square brackets

# %% [code]
t = (1, 2, 3)

# %% [code]
t = 1, 2, 3 # equivalent to above
t

# %% [markdown]
# **2:** They cannot be modified (they are *immutable*).

# %% [code] {"tags":["raises-exception"]}
t[0] = 100

# %% [markdown]
# Tuples are often used for functions that have multiple return values.
# 
# For example, the ``as_integer_ratio()`` method of float objects returns a numerator and a denominator in the form of a tuple:

# %% [code]
x = 0.125
x.as_integer_ratio()

# %% [markdown]
# These multiple return values can be individually assigned as follows:

# %% [code]
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

# %% [markdown]
# Finally we have some insight into the classic Stupid Python Trick™ for swapping two variables!

# %% [code]
a = 1
b = 0
a, b = b, a
print(a, b)

# %% [markdown]
# # Your Turn
# 
# You learn best by writing code, not just reading it. So try **[the coding challenge](https://www.kaggle.com/kernels/fork/1275173)** now.

# %% [markdown]
# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
