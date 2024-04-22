#Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_char(word,n):
    print("Orginal string is",word)
    x = word[n: ]
    return x
print("Removing characters from a string")
print(remove_char("pynative", 4))
print(remove_char("pynative", 2))