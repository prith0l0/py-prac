D=input("Enter is it cold or hot ? ")

if D.upper()=="HOT":
    print("""It is a hot day
          Drink plenty of water""")
elif D.upper() =="COLD":
    print("""It is a cold day
          Wear warm clothes""")
else:
    print("It is a lovely day")


print("*"*70)
is_hot=True
#is_hot=False

if is_hot:
    print("""
It is a very hot day.""")
else:
    print("Enjoy your day")