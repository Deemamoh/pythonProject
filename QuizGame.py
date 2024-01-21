print("welcome to my computer quiz!")

playing = input("Do u wnat to play?")

if playing != "yes":
    quit()

print("okay let us play")

answer = input("What does CPU stands for? ")
if answer == "central processing unit":
    print("correct")
else:
    print("incorrect")
