#Euan McElhoney
#30/10/2014
#Selection Class exersices - Strech 3 - Date Formatter

print("This program will take 3 integers, for example 12 5 03, and display the date as 12th May 2003")
print("It will display any date between 1931 and 2030")
print()

day = int(input("Please enter the day: "))
month = int(input("Please enter the month: "))
year = int(input("Please enter the year: "))

leap_year = 0
leap_year_century = 0

if year % 100 == 0:
    if year % 400 ==0:
        leap_year_century = True
    else:
        leap_year_century = False
elif year % 4:
    leap_year = True
else:
    leap_year = False
        
if day >= 32 or month >=13 or day == 0 or year >= 100:
    print("Invalid date")
else:
    if leap_year_century = True or leap_year = True:
        if day == 1 or day == 21 or day == 31:
            day_formatted_leap = ("{0}st".format(day))
        elif day == 2 or day == 22:
            day_formatted_leap = ("{0}nd".format(day))
        elif day == 3 or day == 23:
            day_formatted_leap = ("{0}rd".format(day))
        else:
            day_formatted_leap = ("{0}th".format(day))
    else:
        
        
    

    if month == 1:
        month_formatted = ("January")
    elif month == 2:
        month_formatted = ("Febuary")
    elif month == 3:
        month_formatted = ("March")
    elif month == 4:
        month_formatted = ("April")
    elif month == 5:
        month_formatted = ("May")
    elif month == 6:
        month_formatted = ("June")
    elif month == 7:
        month_formatted = ("July")
    elif month == 8:
        month_formatted = ("August")
    elif month == 9:
        month_formatted = ("September")
    elif month == 10:
        month_formatted = ("October")
    elif month == 11:
        month_formatted = ("November")
    elif month == 12:
        month_formatted = ("December")
    
    if  year > 30 and year <= 99:
        year_formatted = ("19{0}".format(year))
    else:
        year_formatted = ("20{0}".format(year))
        
    print("The date chosen is the {0} of {1}, {2}".format(day_formatted, month_formatted, year_formatted))

 

