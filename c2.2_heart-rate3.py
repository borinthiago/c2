# Ask HR and AGE to user:

hr = int(input("Please enter your Heart Rate:  "))
age = int(input("Please enter your age: "))

# Creating conditional to assess HR:

# Until 2y old
if age <= 2:
    if hr >=120 and hr <=140:
        print("hr normal")
    else:
        print("hr out of range")
elif age >=8 and age <=17:
    if hr >=80 and hr <=100:
        print("hr normal")
        else:
        print("hr out of range")
elif age >=18 and age <=60:
    if hr >=60 and hr <=80:
        print("hr normal")
        else:
        print("hr out of range")
elif age > 60:
    if hr >=50 and hr <=60:
        print("hr normal")
        else:
        print("hr out of range")
else:
    print("it not possible to calculate")



