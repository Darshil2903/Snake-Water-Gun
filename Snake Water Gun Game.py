import random


def gamewin():
    if computer==you:
        return None

    if computer != you:
        if computer =="s":
            if you =="w":
                return False
            if you =="g":
                return True
        if computer =="w":
            if you =="g":
                return False
            if you =="s":
                return True
        if computer =="g":
            if you =="w":
                return True
            if you =="s":
                return False
        return



def funtion ():
    randno = random.randint(1,3)
    if randno ==1 :
        return "s"
    if randno ==2 :
        return "w"
    if randno ==3 :
        return "g"


points=0
print("************Welcome To The Snake Water Gun Game Made By Darshil Patel************")
for i in range (1,7):
    computer = funtion()
    you = input("snake(s) water(w) or gun(g) ? " )

    a = gamewin()
    print("computer chose", (computer))
    if a == None:
        print("the game is tie!!")
    elif a == True:
        points+=1
        print("you win!!")
    else:
        print("you lose!!")

print("YOUR SCORE IS ",(points) )




