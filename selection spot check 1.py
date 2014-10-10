#Euan McElhoney
#10/10/14
#Selection spot check task 1

attendance = int(input("Please enter our attendance as a percentage: "))

if attendance >= 101 or attendance < 0:
    print("Invalid input")
elif attendance >=85:
    print("Your attendance is {0}%. Keep up the good attendance.".format(attendance))
else:
    print("Your attendance is only {0}%. You must improve your attendance".format(attendance))
