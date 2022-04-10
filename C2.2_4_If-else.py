#variables
rm = input("Please enter your RM: ")
age = input("Please enter your age: ")
#conditional to check if the student is over 18
if int(age) >= 18:
    print("Thank for enrolling!")
    print("{} you will receive an email with details".format(rm))

# creating an chained "if" for underage students
else:
    authorization = input("Do you have a responsible agreement signed? Enter y (yes) or n (no): ")
    if str(authorization) = "y":
        print("{},you will receive an email to upload your authorization".format(rm))
    else:
        print("Unfortunatelly {} you do not match the requirements to join, please consider do it next year".format(rm))

