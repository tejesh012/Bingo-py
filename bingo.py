import random
playerscap = 5
players = int(input(f"Enter number of players [2 to {playerscap}] : "))
leaderboard = {}
totalplayerlists = []
totalmarked = []
status = True

playernames = []

def createplayer():
    playerlist = []
    dump = []
    for i in range(1,26):
        dump.append(i)
    random.shuffle(dump)
    index = 0
    for i in range(5):
        collist = []
        for j in range(5):
            num = dump[index]
            if num<10:
                num = "0"+str(num)
            collist.append(str(num))
            index+=1
        playerlist.append(collist)
    totalplayerlists.append(playerlist)
    

def printboard(curplayer):
    for i in range(5):
        print(*totalplayerlists[curplayer][i])
    print()
            

def startgame(status):
    currentplayer = -1
    # count = 0
    while(status):
        currentplayer = (currentplayer+1)%players
        print(f"Player to choose a number is {playernames[currentplayer]}")
        printboard(currentplayer)
        choosenumber(currentplayer)
        # markallboards(markednumber)
        win = winningpositions(currentplayer)
        leaderboard[currentplayer] = win*1000
        if win >= 5:
            status =False
            print("*******Score-board**********")
            print()
            for i in range(players):
                print(f"{playernames[i]} : {leaderboard[i]} points")
            print()
            print(f"winner : {playernames[currentplayer]}")
            print()
            print("****************************")

            

def choosenumber(curplayer):
    number = input("Enter a number to mark : ")
    if number.isdigit():
        number = int(number)
        if number <= 0 or number > 25 :
            print("Choose the number which is present in the board :")
            choosenumber(curplayer)
        else:
            if number in totalmarked:
                print("The number is already marked pick again: ")
                choosenumber(curplayer)
            else:
                markallboards(markednumber=number)
                totalmarked.append(number)
    else:
        choosenumber(curplayer)



def winningpositions(currentplayer):
    wincount = 0
    row = checkrow(currentplayer)
    col = checkcol(currentplayer)
    dia = checkdiagonals(currentplayer)
    wincount = row + col+dia
    return wincount

def checkrow(currentplayer):
    totalrowcount = 0
    for i in range(5):
        count =0 
        for j in range(5):
            if totalplayerlists[currentplayer][i][j] == "⭐":
                count+=1
        if count == 5:
            totalrowcount +=1
            
                
    return totalrowcount

def checkcol(currentplayer):
    totalcolcount = 0
    for i in range(5):
        count =0 
        for j in range(5):
            if totalplayerlists[currentplayer][j][i] == "⭐":
                count+=1
        if count == 5:
            totalcolcount +=1
            
    return totalcolcount

def checkdiagonals(currentplayer):
    totaldia1count = 0
    dia1 = 0
    dia2= 0
    for j in range(5):
        if totalplayerlists[currentplayer][j][j] == "⭐":
            dia1+=1
        if dia1 == 5:
            totaldia1count+=1
    for j in range(5):
        if totalplayerlists[currentplayer][j][5-j-1] == "⭐":
            dia2+=1
        if dia2 == 5:
            totaldia1count+=1
            
    return totaldia1count


def markallboards(markednumber):
    for i in range(players):
        for j in range(5):
            for x in totalplayerlists[i][j]:
                if x.isdigit():
                    integerval =int(x)
                else:
                    integerval = x
                if integerval == markednumber:
                    ind = totalplayerlists[i][j].index(x)
                    totalplayerlists[i][j][ind] = "⭐"
                    break
    


if 1<players <=playerscap:
    for i in range(players):
        playername = str(input(f"Enter player {i+1} name : "))
        playernames.append(playername)
        createplayer()

    startgame(status)
else:
    print(f"⚠️  You can only choose a number between 2 and {playerscap}")