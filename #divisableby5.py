def div(num_list):
    print("The given list is",num_list)
    for num in num_list:
        if num % 5==0:
            return(num)
        
print("Divisible by 5 ",div(num_list=[10,20,3,5]))