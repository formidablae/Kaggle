# %% [markdown]
# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/booleans-and-conditionals).**
# 
# ---
# 

# %% [markdown]
# # Try It Yourself
# 
# Think you are ready to use Booleans and Conditionals? Try it yourself and find out.
# 
# To get started, **run the setup code below** before writing your own code (and if you leave this notebook and come back later, don't forget to run the setup code again).

# %% [code]
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

print('Setup complete.')

# %% [markdown]
# # Exercises

# %% [markdown]
# ## 1.
# 
# Many programming languages have [`sign`](https://en.wikipedia.org/wiki/Sign_function) available as a built-in function. Python doesn't, but we can define our own!
# 
# In the cell below, define a function called `sign` which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

# %% [code]
# Your code goes here. Define a function called 'sign'
def sign(num):
    return 1 if num > 0 else (-1 if num < 0 else 0)

# Check your answer
q1.check()

# %% [code]
q1.solution()

# %% [markdown]
# ## 2.
# 
# We've decided to add "logging" to our `to_smash` function from the previous exercise.

# %% [code]
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)

# %% [markdown]
# What happens if we call it with `total_candies = 1`?

# %% [code]
to_smash(1)

# %% [markdown]
# That isn't great grammar!
# 
# Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular "candy" instead of the plural "candies")

# %% [code]
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

# %% [code]
# Check your answer (Run this code cell to receive credit!)
q2.solution()

# %% [markdown]
# ## 3. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
# 
# In the main lesson we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...
# - I have an umbrella...
# - or if the rain isn't too heavy and I have a hood...
# - otherwise, I'm still fine unless it's raining *and* it's a workday
# 
# The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?
# 
# To prove that `prepared_for_weather` is buggy, come up with a set of inputs where either:
# - the function returns `False` (but should have returned `True`), or
# - the function returned `True` (but should have returned `False`).
# 
# To get credit for completing this question, your code should return a <font color='#33cc33'>Correct</font> result.

# %% [code]
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
q3.check()

# %% [code]
q3.hint()
#q3.solution()

# %% [markdown]
# ## 4.
# 
# The function `is_negative` below is implemented correctly - it returns True if the given number is negative and False otherwise.
# 
# However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by *75%* while keeping the same behaviour. 
# 
# See if you can come up with an equivalent body that uses just **one line** of code, and put it in the function `concise_is_negative`. (HINT: you don't even need Python's ternary syntax)

# %% [code]
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0

# Check your answer
q4.check()

# %% [code]
q4.hint()
#q4.solution()

# %% [markdown]
# ## 5.
# 
# The boolean variables `ketchup`, `mustard` and `onion` represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:

# %% [code]
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

# %% [markdown]
# For each of the remaining functions, fill in the body to match the English description in the docstring. 

# %% [code]
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

# Check your answer
q5.a.check()

# %% [code]
q5.a.hint()
#q5.a.solution()

# %% [code]
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)

# Check your answer
q5.b.check()

# %% [code]
q5.b.hint()
#q5.b.solution()

# %% [code]
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return not ketchup and mustard or ketchup and not mustard

# Check your answer
q5.c.check()

# %% [code]
q5.c.hint()
q5.c.solution()

# %% [markdown]
# ## 6. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
# 
# We’ve seen that calling `bool()` on an integer returns `False` if it’s equal to 0 and `True` otherwise. What happens if we call `int()` on a bool? Try it out in the notebook cell below.
# 
# Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"?

# %% [code]
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return ketchup + mustard + onion == 1

# Check your answer
q6.check()

# %% [code]
q6.hint()
#q6.solution()

# %% [markdown]
# ## 7. <span title="A bit spicy" style="color: darkgreen ">🌶️</span> (Optional)
# 
# In this problem we'll be working with a simplified version of [blackjack](https://en.wikipedia.org/wiki/Blackjack) (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:
# 
# - The player is dealt two face-up cards. The dealer is dealt one face-up card.
# - The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
# - The dealer then deals additional cards to himself until either:
#     - the sum of the dealer's cards exceeds 21, in which case the player wins the round
#     - the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
#     
# When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)
# 
# For this problem, you'll write a function representing the player's decision-making strategy in this game. We've provided a very unintelligent implementation below:

# %% [code]
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False

# %% [markdown]
# This very conservative agent *always* sticks with the hand of two cards that they're dealt.
# 
# We'll be simulating games between your player agent and our own dealer agent by calling your function.
# 
# Try running the function below to see an example of a simulated game:

# %% [code]
q7.simulate_one_game()

# %% [markdown]
# The real test of your agent's mettle is their average win rate over many games. Try calling the function below to simulate 50000 games of blackjack (it may take a couple seconds):

# %% [code]
q7.simulate(n_games=50000)

# %% [markdown]
# Our dumb agent that completely ignores the game state still manages to win shockingly often!
# 
# Try adding some more smarts to the `should_hit` function and see how it affects the results.

# %% [code]
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False

q7.simulate(n_games=50000)

# %% [markdown]
# # Keep Going
# 
# Learn about **[lists and tuples](https://www.kaggle.com/colinmorris/lists)** to handle multiple items of data in a systematic way.

# %% [markdown]
# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [Learn Discussion forum](https://www.kaggle.com/learn-forum/161283) to chat with other Learners.*
