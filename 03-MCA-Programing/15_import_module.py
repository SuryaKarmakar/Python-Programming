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
    import math
except ImportError:
    print("Pandas library not found. Install using pip to proceed.")

# import custom module.
import calculator_module

# use functions from the calculator module
print(calculator_module.add(4, 6))
print(calculator_module.divide(10, 3))

# we can also choose to import specific attributes using Selective Import.
from calculator_module import subtract

print(subtract(10, 4))


