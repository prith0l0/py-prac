secret_num= 9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=(int(input("Enter any num   ")))
    guess_count += 1
    if guess==9:
        print("You win")
        break
else:
    print("You failed.")
    