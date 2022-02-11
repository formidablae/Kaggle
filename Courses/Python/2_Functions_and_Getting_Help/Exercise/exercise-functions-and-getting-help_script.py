# %% [markdown]
# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/functions-and-getting-help).**
# 
# ---
# 

# %% [markdown]
# # Try It Yourself
# 
# Functions are powerful. Try writing some yourself.
# 
# As before, don't forget to run the setup code below before jumping into question 1.

# %% [code] {"_kg_hide-input":true,"_kg_hide-output":true}
# SETUP. You don't need to worry for now about what this code does or how it works.
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex2 import *

print('Setup complete.')

# %% [markdown]
# # Exercises

# %% [markdown]
# ## 1.
# 
# Complete the body of the following function according to its docstring.
# 
# HINT: Python has a built-in function `round`.

# %% [code]
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num, 2)

# Check your answer
q1.check()

# %% [code]
# Uncomment the following for a hint
q1.hint()
# Or uncomment the following to peek at the solution
#q1.solution()

# %% [markdown]
# ## 2.
# The help for `round` says that `ndigits` (the second argument) may be negative.
# What do you think will happen when it is? Try some examples in the following cell?
# 
# Can you think of a case where this would be useful?

# %% [code]
# Put your test code here
round(137, -1)

# %% [code]
# Check your answer (Run this code cell to receive credit!)
q2.solution()

# %% [markdown]
# ## 3.
# 
# In a previous programming problem, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# 
# Below is a simple function that will calculate the number of candies to smash for *any* number of total candies.
# 
# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
# 
# Update the docstring to reflect this new behaviour.

# %% [code]
def to_smash(total_candies, numb_of_friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % numb_of_friends

# Check your answer
q3.check()

# %% [code]
q3.hint()

# %% [code]
q3.solution()

# %% [markdown]
# ## 4. (Optional)
# 
# It may not be fun, but reading and understanding error messages will be an important part of your Python career.
# 
# Each code cell below contains some commented-out buggy code. For each cell...
# 
# 1. Read the code and predict what you think will happen when it's run.
# 2. Then uncomment the code and run it to see what happens. (**Tip**: In the kernel editor, you can highlight several lines and press `ctrl`+`/` to toggle commenting.)
# 3. Fix the code (so that it accomplishes its intended purpose without throwing an exception)
# 
# <!-- TODO: should this be autochecked? Delta is probably pretty small. -->

# %% [code]
round_to_two_places(9.9999)

# %% [code]
x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), y)

# %% [code]
def f(x):
    y = abs(x)
    return y

print(f(5))

# %% [markdown]
# # Keep Going
# 
# Nice job with the code. Next up, you'll learn about *conditionals*, which you'll need to write interesting programs. Keep going **[here](https://www.kaggle.com/colinmorris/booleans-and-conditionals)**

# %% [markdown]
# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [Learn Discussion forum](https://www.kaggle.com/learn-forum/161283) to chat with other Learners.*
