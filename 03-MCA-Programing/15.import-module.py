# basic import
import math

print(math.pi)

# import with alias.
import math as mt

print(mt.pi)

# selective import.
from datetime import datetime

print(datetime.now())

# wildcard import 
from math import *

print(pi)

# handling import error
try:
    import pandas as pd
except ImportError:
    print("Pandas library not found. Install using pip to proceed.")

# import custom module.
import calculator

# use functions from the calculator module
print(calculator.add(4, 6))
print(calculator.divide(10, 3))

# we can also choose to import specific attributes using Selective Import.
from calculator import subtract

print(subtract(10, 4))


