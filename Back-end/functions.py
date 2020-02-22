# function for buying houses
def buy_houses(buy, location, money, location_price):
    if(buy):
        global money = money - location_price * 0.25 # the player pays for the house
        global house_location[location]++; # the number of houses on that location increases

# function that moves players
def move_player(player, location, money, value_dice):
    player_location[player] = player_location[player] + value_dice
    if(player_location[player]>42): # checks if the player has passed the start line
        player_money[player] = player_money[player] + 200
    elif(player_location[player]== 42):
        player_money[player] = player_money[player] + 400



# function that checks why is skipped
def checkskip(skip, escape, pay, player):
    if(skip == 1): # skip =1 when the player is in the tutors room
            if(escape ==2):# check for escape card from prison: if =2 then the player wants to use it
                skip ==0
    if(skip == 2): # check if the player lost so that it is skipped each round until the end of the game
            player = player +1    # moves to the next player
