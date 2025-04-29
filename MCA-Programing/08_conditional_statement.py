# if-else statement
age = int(input("Enter your age : "))

if age >= 18:
    print("You can vote")
else:
    print("You are not eligible")

# elif statement (short form of else if)
# this is called chained condition
marks = int(input("Enter your total marks : "))

if marks >= 90:
    print("Very good")
elif marks >= 70:
    print("Good")
elif marks >= 40:
    print("Average")
else:
    print("Fail")

# nested condition
gender = input("Enter gender : (M/F) ")

if age >= 18:
    if gender == "M":
        print("Please wait in left line")
    else:
        print("Please wait in right line")
else:
    print("You are not eligible")

# Composite Expressions (combine two conditional expressions using logical operator)
if age >= 18 and (gender == "M" or gender == "M"):
    print("You can vote")
else:
    print("You are not eligible")


