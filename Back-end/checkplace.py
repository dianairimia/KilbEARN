def check_place(player):
    if(location[player] == -1): # deadlines
        continue
    elif(location[player] == -2): # mitigating_circumstances
        continue

    elif(location[player] == 30):
        global skip = 1
        player_location[player] = 10
    elif(location[player] == 20):
        player_money[player] = 
