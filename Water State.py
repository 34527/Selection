#Euan McElhoney
#30/09/2014
#Selection Exercises - Water state

state = int(input("Please enter the temperature of the water: "))

if state > 100:
    print("The water has boiled")
elif state < 0:
    print("The water has frozen")
else:
    print("The water has remained a liquid")
