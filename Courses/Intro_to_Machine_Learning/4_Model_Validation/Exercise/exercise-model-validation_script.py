# %% [markdown]
# **This notebook is an exercise in the [Introduction to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) course.  You can reference the tutorial at [this link](https://www.kaggle.com/dansbecker/model-validation).**
# 
# ---
# 

# %% [markdown]
# ## Recap
# You've built a model. In this exercise you will test how good your model is.
# 
# Run the cell below to set up your coding environment where the previous exercise left off.

# %% [code]
# Code you have previously used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor()
# Fit Model
iowa_model.fit(X, y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

# Set up code checking
from learntools.core import binder

binder.bind(globals())
from learntools.machine_learning.ex4 import *

print("Setup Complete")

# %% [markdown]
# # Exercises
# 
# ## Step 1: Split Your Data
# Use the `train_test_split` function to split up your data.
# 
# Give it the argument `random_state=1` so the `check` functions know what to expect when verifying your code.
# 
# Recall, your features are loaded in the DataFrame **X** and your target is loaded in **y**.
# 

# %% [code]
# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split

# fill in and uncomment
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Check your answer
step_1.check()

# %% [code]
# The lines below will show you a hint or the solution.
# step_1.hint() 
# step_1.solution()


# %% [markdown]
# ## Step 2: Specify and Fit the Model
# 
# Create a `DecisionTreeRegressor` model and fit it to the relevant data.
# Set `random_state` to 1 again when creating the model.

# %% [code]
# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)

# Check your answer
step_2.check()

# %% [code]
# step_2.hint()
# step_2.solution()

# %% [markdown]
# ## Step 3: Make Predictions with Validation data
# 

# %% [code]
# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# Check your answer
step_3.check()

# %% [code]
# step_3.hint()
# step_3.solution()

# %% [markdown]
# Inspect your predictions and actual values from validation data.

# %% [code]
# print the top few validation predictions
print("First out-of-sample predictions:", iowa_model.predict(val_X.head()))
# print the top few actual prices from validation data
print("Actual target values for those homes:", val_y.head().tolist())

# %% [markdown]
# What do you notice that is different from what you saw with in-sample predictions (which are printed after the top code cell in this page).
# 
# Do you remember why validation predictions differ from in-sample (or training) predictions? This is an important idea from the last lesson.
# 
# ## Step 4: Calculate the Mean Absolute Error in Validation Data
# 

# %% [code]
from sklearn.metrics import mean_absolute_error

val_mae = mean_absolute_error(val_y, val_predictions)

# uncomment following line to see the validation_mae
print(val_mae)

# Check your answer
step_4.check()

# %% [code]
# step_4.hint()
# step_4.solution()

# %% [markdown]
# Is that MAE good?  There isn't a general rule for what values are good that applies across applications. But you'll see how to use (and improve) this number in the next step.
# 
# # Keep Going
# 
# You are ready for **[Underfitting and Overfitting](https://www.kaggle.com/dansbecker/underfitting-and-overfitting).**
# 

# %% [markdown]
# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [Learn Discussion forum](https://www.kaggle.com/learn-forum/161285) to chat with other Learners.*
