Weight=int(input("Enter your weight"))
Unit=input("K or ps ?")
u_upper=Unit.upper()
if u_upper =="K":
    print("Weight in pounds is :", Weight/0.45)
else:
    print("Weight in kilo-gram is :", Weight*0.45)