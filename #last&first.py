def f_l(number_list):
    print("Given list ",number_list)
    first_num=number_list[0]
    last_num=number_list[-1]
    if first_num==last_num:
        return True
    else:
        return False
    
print("The result is ",f_l(number_list=[22,23,2,3,32,22]))


