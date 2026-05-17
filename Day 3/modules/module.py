# 1. What is a Module?
# A module is simply a Python file (.py) containing functions, classes, or variables.

#Different import style
# 1.Import whole module
# import math
# print(math.sqrt(16))

#2.Import specific function
# from math import sqrt
# print(sqrt(25))

#3Import with alias
# import numpy as np

# Built-in Modules

# Common built-in modules:
# math
# random
# datetime
# os
# json

# import random
# print(random.randint(1, 10))

# What is a Package?

# A package is a folder containing multiple modules.

# Project Structure
# project/
# │── main.py
# │── utils/
# │   │── __init__.py
# │   │── math_utils.py
# │   │── file_utils.py


# __name__ == "__main__"

# Used to distinguish between:

# Running a file directly
# Importing it as a module

# def greet():
#     print("Hello")

# if __name__ == "__main__":
#     greet()

import requests

response = requests.get("https://api.github.com")
print(response.status_code)