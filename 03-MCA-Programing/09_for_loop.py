# for loop
# syntax - for <var> in <iterable>:
# var represent the lopping variable

fruits = ["apple", "banana", "cherry"] 
for x in fruits: 
    print(x) 

fruits_tuple = ("apple", "banana", "cherry")
for x in fruits_tuple:
    print(x)

for x in "python":
    print(x)

# nested loop
color = ["grean", "red", "orange"]

for x in color:
    for y in fruits:
        print(x + " " + y)

# using else statement in loop
# else is only functional when the loop is terminated normally
for x in range(5):
    print(x)
else:
    print("End of the loop") 

# else will not work if we forcefully terminate the loop
for x in range(5):
    print(x)
    if x == 3:
        break
else:
    print("End of the loop") 