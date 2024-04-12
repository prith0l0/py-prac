course="Python is for beginners"
print(len(course))
print(course.upper())#here "."is a dot operator its specipic for string so its a method 
print(course)#main string does not change
print(course.find("i"))#it can find the index num its case sensitive
print(course.find("A"))
print(course.find("is")) #the word is starts from index 7
print(course.replace("Python","Java"))#case sensitive
print(course.replace("P","J"))
print("Python" in course)#case sensitive
print("python" in course)

#".find"return the index value but the in operator give us bollean exprssion 
