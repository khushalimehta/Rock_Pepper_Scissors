print("Please pick one: Rock Scissors Paper")
while True:
    dict1 = {'rock':1,'scissors':2,'paper':3}
    playera = str(input("Player a:"))
    playerb = str(input("Player b:"))
    a = dict1.get(playera)
    b = dict1.get(playerb)
    dif = a - b
    if dif in [-1,2]:
        print("Player a win")
        str = input("Do you want to play another game,yes or no?")
        if str == "yes":
            continue
        else:
            break
    elif dif in [-2,1]:
        print("Player b win")
        str = input("Do you want to play another game,yes or no?")
        if str == "yes":
            continue
        else:
            break
    else:
        print("Invalid input")

