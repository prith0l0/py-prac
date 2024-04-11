#using if-else statement
a=(int(input("Enter a num: ")))
b=(int(input("Enter another num: ")))
if a>b:
    print(f"Maximum={a}Minimum={b}")
else:
    print(f"Maximum={b}Minimum={a}")
print("*"*70)

#using lambda func
a=(int(input("Enter a num: ")))
b=(int(input("Enter another num: ")))
maximum = lambda a,b:a if a>b else b
print(f"Maximum={a}Minimum={b}")
print("*"*70)


