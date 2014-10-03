#Euan McElhoney
#30/09/2014
#Selection excercises - Grade Boundary - stretch

grade = int(input("Please enter the recieved grade: "))

if 81 <= grade <= 100:
    print("Grade A")
elif 71<= grade <= 80:
    print("Grade B")
elif 61<= grade <= 70:
    print("Grade C")
elif 51<= grade <= 60:
    print("Grade D")
elif 41 <= grade <= 50:
    print("Grade E")
elif 101 <= grade:
    print("Invalid score")
else:
    print("Fail")
