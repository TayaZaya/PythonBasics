"""
age = input("What is your age?: ")

if int(age) < 18:
	print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
	print("Powering On. Enjoy the ride!");
elif int(age) == 18:
	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.
"""

"""
def checkDriverAge(age = 0):
	if int(age) < 18:
		print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
		print("Powering On. Enjoy the ride!");
	elif int(age) == 18:
		print("Congratulations on your first year of driving. Enjoy the ride!")
# Tests
# Test 1 default age 0
checkDriverAge()

# test 1 young age
checkDriverAge(1)
checkDriverAge(2)
checkDriverAge(-7)
checkDriverAge(14)
#checkDriverAge(a)
checkDriverAge(3)
checkDriverAge(9)

# Test case 2
# testing legal age
checkDriverAge(17.9999999999999999)
checkDriverAge(18)
checkDriverAge(17.787)

# Test case 3
# testing above legal age
checkDriverAge(28)
checkDriverAge(90)
checkDriverAge(29)
checkDriverAge(57.8)

"""

"""
def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()
"""
"""
def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge(18)
"""
help(help)