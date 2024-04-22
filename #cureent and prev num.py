"""Write a program to iterate the first
10 numbers, and in each iteration,print the
sum of the current
and previous number."""
print("Printing current and previous number and their sum in a range(10)")
previous_num=0

# loop from 1 to 10
for i in range(1,11):
    sum=previous_num+ i
    print(f"Current Number {i} Previous Number{previous_num} Sum:{sum}")
    previous_num=i