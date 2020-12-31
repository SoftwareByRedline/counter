players = input("Enter players (comma separated): ").replace(" ", "").replace("+", "").replace("-", "")
players = players.split(",")

balances = [0 for i in range(len(players))]

def add(player, amount, other_player = ""):
    global balances
    try:
        index = players.index(player)
    except:
        index = int(player)
    balances[index] += amount
    if other_player:
        try:
            other_index = players.index(other_player)
        except:
            other_index = other_player

        balances[other_index] -= amount

def subtract(player, amount, other_player = ""):
    global balances
    try:
        index = players.index(player)
    except:
        index = int(player)
    balances[index] -= amount
    if other_player:
        try:
            other_index = players.index(other_player)
        except:
            other_index = other_player
        balances[other_index] += amount



while True:
    for i in range(len(players)):
        player = players[i]
        balance = balances[i]
        print(str(i) + " " + player + (" " * (10 - len(player))) + str(balance) + "\n")
    muvelet = input("Enter command or \"h\" to open help   \n").replace(" ","")
    #try:
    if muvelet == "s" or muvelet == "S":
        print("Commands: \n\n Add balance: player + amount \n Subtract balance: player - amount \n Get money from another player: player_who_gets + amount < player_who_pays \n Pay money to another player: player_who_pays - amount > player_who_gets")
    elif "+" in muvelet:
        muvelet = muvelet.split("+")
        try:
            muvelet[1] = muvelet[1].split("<")
            add(muvelet[0], int(muvelet[1][0]), muvelet[1][1])
        except:
            add(muvelet[0], int(muvelet[1]))


    elif "-" in muvelet:
        muvelet = muvelet.split("-")
        try:
            muvelet[1] = muvelet[1].split(">")
            subtract(muvelet[0], int(muvelet[1][0]), muvelet[1][1])
        except:
            subtract(muvelet[0], int(muvelet[1]))
            
            
