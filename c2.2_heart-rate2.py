# Ask HR and AGE to user:

hr = int(input("Please enter your Heart Rate:  "))
age = int(input("Please enter your age: "))

# Creating conditional to assess HR:

# Until 2y old
if age <= 2:
    if hr >=120:
        if hr <=140:
            print("hr normal")
        else:
            print("hr over limit")
    else:
        print("hr under limit")
elif age >= 8:
    if age <=17:
        if hr >= 80:
            if hr <= 100:
                print("hr normal")
            else:
                print("hr over limit")
        else:
            print("hr under limit")
    if age >=18
        if age<=60
            if hr >=70:
                if hr <=80:
                    print("hr normal")
                else:
                    print("hr over limit")
            else:
                print("hr under limit")
        else:
            if hr >= 50:
                if hr <=60:
                    print("hr normal")
                else:
                    print("hr over limit")
            else:
                print("hr under limit")
else:
    print("It is not possible to analyze")
