
# %% [markdown]
# In this tutorial, you will learn about **imports** in Python, get some tips for working with unfamiliar libraries (and the objects they return), and dig into **operator overloading**.
import math
​
# %% [markdown]
# # Imports
#
# So far we've talked about types and functions which are built-in to the language.
#
# But one of the best things about Python (especially if you're a data scientist) is the vast number of high-quality custom libraries that have been written for it.
#
# Some of these libraries are in the "standard library", meaning you can find them anywhere you run Python. Other libraries can be easily added, even if they aren't always shipped with Python.
#
# Either way, we'll access this code with **imports**.
#
# We'll start our example by importing `math` from the standard library.
​
# %% [code]
​
print("It's math! It has type {}".format(type(math)))
​
# %% [markdown]
# `math` is a module. A module is just a collection of variables (a *namespace*, if you like) defined by someone else. We can see all the names in `math` using the built-in function `dir()`.
​
# %% [code]
print(dir(math))
​
# %% [markdown]
# We can access these variables using dot syntax. Some of them refer to simple values, like `math.pi`:
​
# %% [code]
print("pi to 4 significant digits = {:.4}".format(math.pi))
​
# %% [markdown]
# But most of what we'll find in the module are functions, like `math.log`:
​
# %% [code]
math.log(32, 2)
​
# %% [markdown]
# Of course, if we don't know what `math.log` does, we can call `help()` on it:
​
# %% [code]
help(math.log)
​
# %% [markdown]
# We can also call `help()` on the module itself. This will give us the combined documentation for *all* the functions and values in the module (as well as a high-level description of the module). Click the "output" button to see the whole `math` help page.
