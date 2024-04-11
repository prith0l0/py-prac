#using user input
a=(int(input("Enter a num:")))
b=(int(input("Enter another num:")))
sum = lambda a,b: a+b
print(sum(a,b))
print("*"*70)
#not using user input
s=lambda c,d: c+d
print(s(5,8))
