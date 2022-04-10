# creating the buy condition:
value = input("Enter the total value: ")
vaucher = input("Please enter your vaucher: ")

# converting value to float:
value = float(value)

#creating conditional to acceprt or not the vaucher:
if vaucher.upper() == "NIVER10":
    total_value = float(value) * 0.9
else:
    total_value = float(value)
    print("Your vaucher does not aplly")
print("The total amount is {}".format(total_value))