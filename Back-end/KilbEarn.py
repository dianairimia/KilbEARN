def pay(player, amount, optionality):                   #we use this function to pay
                                                        #player is the player who has to pay
                                                        #amount is the sum the player has to pay
                                                        #optinality tells us if the player is forced to pay: 1-he doesn't; 0-he does
    global player_money, skip
    if player_money[player] > amount:                   #if the player has enough money, he pays
        player_money[player] = player_money[player] - amount
    elif optionality == 0:
        #how do I do this?...
        skip = 1                                        #the player lost if he ran out of money


def check_ownable_locations(checked_location, player):  #you get into the function only if location[check_location] >= 0
                                                        #(location is ownable)
                                                        #checked_location is the location currently checked
                                                        #player is the number of the player for which we do those checks
    global location, player_money, location_price
    if location[checked_location] > 0:                    #this means the location is owned by somebody
        if location[checked_location] != player:          #this means that the location is owned by somebody else
            pay(player, location_price[checked_location], 0)
                                                        #player pays the rent
    else:
        answer = input("Do you want to buy this location? (y/n)")
        if answer[0] == 'y':
            pay(player, location_price[checked_location], 1)
            location[checked_location] = player


location = []               #this list tells us what kind of location each location is
player_money = []           #this list tells us the amount of money each player has
location_price = []         #this list tells us what is the price of each location
skip = []                   #this list tells use which players are in prison or lost



#these are just gonna be some checks for check_ownable_locations()

location.append(1)
location.append(0)

#check_ownable_locations(0, 1)

#player_money.append(0)
#player_money.append(0)
#player_money.append(1500)
#location_price.append(250)
#check_ownable_locations(0, 2)
#print(player_money[2])

location_price.append(250)
location_price.append(350)
player_money.append(0)
player_money.append(1500)
check_ownable_locations(1, 1)
print(player_money[1])
print(location[1])