#Euan McElhoney
#10/10/14
#Selection spot check task 2

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
gender = input("Please enter your gender as either 'M' for males or 'F' for females: ")

if gender == "M" or gender == "m":
    print("Mr {0} {1}".format(first_name, last_name))
elif gender == "F" or gender == "f":
    print("Ms {0} {1}".format(first_name, last_name))
else:
    print("Please enter an appropriate gender")

