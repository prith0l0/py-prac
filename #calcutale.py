#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def multiorsum (num1,num2):
    sum=num1+num2
    product=num1*num2
    if product <=1000:
        return product
    else:
        return sum
result=multiorsum(20,30)
print("The result is{} ".format(result)) #using .format()

result=multiorsum(40,50)
print(f"The result is {result}") #using f string


