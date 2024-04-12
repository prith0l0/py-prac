name=(input("Enter your namre "))
if name.__len__<3:
    print("Name must be at least 3 characters")
elif name.__len__>50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")
    
