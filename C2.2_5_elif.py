#variables
rm = input("Please enter your RM: ")
age = input("Please enter your age: ")
#conditional to check if the student is over 18
if int(age) >= 18:
    print("Thank for enrolling!")
    print("{} you will receive an email with details".format(rm))

# creating an chained "elif" for underage students

elif int(age) == 17:
    print("You might turn 18 before enrolling day")
elif int(age) == 16:
    print("You can subscribe but not enrol")
else: print("Sorry try again in 2 years")