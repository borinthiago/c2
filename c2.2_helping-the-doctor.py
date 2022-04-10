# Asking for students name and score
name = input("Please enter your name: ")
score = input("Please enter your score: ")


# Crating conditional to assess if student matches requirement
if float(score) >= 8.5:
    print("Dear {} you will receive an email with trip details".format(name))
else: print("Dear {}, unfortunatelly your score is too low.".format(name))