import random


#we use this function to pay
#player is the player who has to pay, it's from 0-5
#amount is the sum the player has to pay
#optinality tells us if the player is forced to pay: 1-he doesn't; 0-he does
def pay(player, amount, optionality):



    #global variables
    global player_money, skip, hotels_location, houses_location, location, location_price, no_remaining_player



    #if the player has enough money, he pays
    if player_money[player] > amount:
        player_money[player] = player_money[player] - amount


    #check if the player HAS to pay
    elif optionality == 0:


        #we want to calculate the amount of money a player owns with it's properties...
        #...to determine if he lost or not, without making him manually have to sell all his properties
        properties_value = 0


        for i in range (40):


            #if the player owns a location, we calculate how much he would get for selling everything on it
            if location[i] == player + 1:

                #note: when we sell something, we get half(1/2) the money we spent on it

                #we calculate how much the hotels are worth
                if hotels_location[i] == 1:
                    properties_value = properties_value + location_price[i]
                    #the prices of 4 houses + a hotel is location_price[i] * 2

                #we calculate how much the houses are worth
                if houses_location[i] > 0:
                    properties_value = properties_value + (location_price[i]*2/5)/2 * houses_location[i]
                    #the price of a house is locarion_price[i] * 2/5


                # we calculate how much the locations are worth
                properties_value = properties_value + location_price[i]/2



        # the player lost if he ran out of money
        if properties_value < amount:
            print("YOU LOST!")
            skip[player] = 2
            no_remaining_player = no_remaining_player - 1

            #if a player loses, he loses all his locations and houses and hotels

            for i in range(40):
                if location[i] == player + 1:
                    hotels_location[i] = 0
                    houses_location[i] = 0
                    location[i] = 0



        #we ask the player what he wants to sell
        #this is mostly a place-holder for the final version, but it's still good cause...
        #...except the way the player chooses what he sales, everything is still the same
        else:
            while(player_money[player] < amount):
                answer = input("Do you want o sell a hotel?[y/n]")
                if answer[0] == 'y':
                    where = input("From which location do you want to sell it?[insert the number(0-39)]")
                    where = int(where)
                    if hotels_location[where] == 0 or location[where] != player + 1:
                        print("You don't own a hotel on that location!!!")
                    else:
                        player_money[player] = player_money[player] + location_price[where]
                        hotels_location[where] = 0

                answer = input("Do you want o sell some houses?[y/n]")
                if answer[0] == 'y':
                    where = input("From which location do you want to sell them?[insert the number(0-39)]")
                    where = int(where)
                    if houses_location[where] == 0 or location[where] != player + 1:
                        print("You don't own a house on that location!!!")
                    else:
                        number_houses = input("How many houses do you want to sell?[insert the number]")
                        number_houses = int(number_houses)
                        #for now I'm ignoring that you have to also sell houses from locations...
                        #...with the same color, I'll get back to this in the nearby future.......
                        #also ignoring that you maaaaaay insert too many houses, oooops....
                        player_money[player] = player_money[player] + (location_price[where]*2/5)/2 * number_houses
                        houses_location[where] = houses_location[where] - number_houses

                answer = input("Do you want o sell a location?[y/n]")
                if answer[0] == 'y':
                    where = input("Which location do you want to sell?[insert the number(0-39)]")
                    where = int(where)
                    if location[where] != player + 1:
                        print("You don't own that location!!!")
                    else:
                        player_money[player] = player_money[player] + location_price[where] / 2
                        location[where] = 0

            #now that the player has money after selling stuff he can pay what he has to pay
            player_money[player] = player_money[player] - amount






#pretty clear I guess
def mitigating_circumstances(player):
    global player_money
    global player_location
    global no_remaining_player
    global eduroam_money

    m = random.randint(1,11)
    if m == 1:    # Advance to "Startx". (Collect K 200)
        player_location[player] == 0
        player_money[player] += 200

    if m==2: # Advance to "Byte Cafe" and relax. If you pass through the Startx, collect k 200. If owned, you do not need to pay, if unowned, you can buy it from the Bank.
        if(player_location[player]>27):
            player_money[player] +=200
        player_location[player] = 27
        if(location[27]>0):
            player_money[player] += rentprice ## need to change it later

    if m ==3: # You have been elected the chair of the tutorials for the rest of the semester. Collect k 25 from each player.
        player_money[player] += 25 * no_remaining_player;
        for i in range(3):
            if skip[i] != 2 and i!= player:
                player_money[i] -= 25
                player_money[player] +=25


    if m ==4: # Go directly to the tutor's room. If you pass through Startx do not collect K 200.
        player_location[player]=10

    if m == 5: # Advance token to nearest the server2. If unowned, you may buy it from the Bank. If owned, pay owner a total 10 times the amount thrown.
        if player_location[player] >=0 and player_location[player]<5:
            player_location[player] = 5
        if player_location[player] >=5 and player_location[player]<15:
            player_location[player] = 15
        if player_location[player] >=15 and player_location[player]<25:
            player_location[player] = 25
        if player_location[player] >=25 and player_location[player]<35:
            player_location[player] = 35
        if player_location[player] >=35 and player_location[player]<=39:
            player_location[player] = 5
            player_money[player] += 200
        if location[player]>0:
            ### roll dice -- pay 10 times the amount thrown
            println("Roll dice again")
            x= random.randint(1,7)
            y = random.randint(1,7)
            println("You have thrown" + x+ " "+ y+ " ")
            player_money[player] -= 10 * (x+y)

    if m==6: #Congratulations! You won a hackathon. Collect k 100.
        println("Congratulations! You won a hackathon. Collect k 100.")
        player_money[player] += 100

    if m ==7: # Get out of the tutor's room.
        println("Get out of the tutor's room.")
        escape[player] = 2  ## the player can escape the tutors room

    if m==8:  #Ah for crying out loud. You got to an infinite loop and do not know how to solve it. Ask for help and pay k 50.
        println("Ah for crying out loud. You got to an infinite loop and do not know how to solve it. Ask for help and pay k 50.")
        player_money[player] -= 50
        eduroam_money +=50

    if m==9:# Unfortunately, you were not able to sit the exams. Go to Startx. Do not collect k200.
        println("Unfortunately, you were not able to sit the exams. Go to Startx. Do not collect k200.")
        player_location[player] = 0

    if m==10: #Advance to the Lecture Theatre 1.2. If you pass through Startx do not collect k200. If owned, you do not have to pay the rent. If unowned, you may buy it from the Bank.
        println("Advance to the Lecture Theatre 1.2. If you pass through Startx do not collect k200. If owned, you do not have to pay the rent. If unowned, you may buy it from the Bank.")
        player_location[player] = 13



#Yet again, pretty clear
def deadlines(player):
    global euduroam_money
    global player_money
    global player_location
    global hotels_location
    global houses_location
    global location_price
    d = random.randint(1,11)
    if d==1:   #You missed a deadline. Pay k 50.
        println("You missed a deadline. Pay k 50.")
        player_money[player] -= 50
        eduroam_money += 50

    if d==2:  #You need to add optimisation to your code. Pay k 75.
        println("You need to add optimisation to your code. Pay k 75.")
        player_money[player] -= 75
        eduroam_money += 75

    if d==3: # You are behind with your work. Go to the tutor's room and ask for help. If you pass through Startx collect k 200.
        println("You are behind with your work. Go to the tutor's room and ask for help. If you pass through Startx collect k 200.")
        if player_location[player] >10:
            player_money[player] += 200
        player_location[player] = 10

    if d==4: # Your new coursework is raising your concerns. You do not know if you will finish it on time. Go to Tooltil O and work. If you pass through Startx collect k200. If owned pay the rent, if unowned can buy it.
        println("Your new coursework is raising your concerns. You do not know if you will finish it on time. Go to Tooltil O and work. If you pass through Startx collect k200. If owned pay the rent, if unowned can buy it.")
        if(player_location[player]>37):
            player_money[player] +=200
        player_location[player] = 37

    if d==5: #Midterms are rapidly approaching and you should focus on your work. Collect k 100 that would help you throughout this time.
        player_money[player] += 100

    if d==6: # You have finished your work on time. You deserve a treat. Collect k 50.
        player_money[player] += 50


    if d==7: # You need to finish your work on time. Go to LF 31. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 5 times the amount thrown.  If you pass through Startx collect k 200.
        if player_location[player] > 6:
            player_money[player]+=200
        player_location[player] = 6
        if location[6] >0:
            print("Throw dice again! ")
            x= random.randint(1,7)
            y = random.randint(1,7)
            println("You have thrown " + x + " "+ y)

            player_money[player] = player_money[player] -5*(x+y)




    if d==8: #You need to give your final presentation. Pay each player k 25.
        println("You need to give your final presentation. Pay each player k 25.")
        for i in range(0, no_remaining_player):
            player_money[player] -= 25
            player_money[i] += 25


    if d==9:#   Demo presentation before holiday. Pay k75.
        player_money[player] -= 75

    if d==10: # Final report deadline. Go to the Quiet Room and finish your report. If owned, pay 2 times the rent. If unowned, you may buy it. If you pass through Startx collect k200.
        if player_location[player] > 26:
            player_money[player] += 200
        player_location[player] = 26
        if location[26]>0:
            player_money[player] -= rent*2 ### need to change variable





#you get into the function only if location[check_location] >= 0 (location is ownable)
#checked_location is the location currently checked, it's from 0-39
#player is the number of the player for which we do these checks, it's from 0-5
def check_ownable_locations(checked_location, player):



    #global variables
    global location, player_money, location_price, server_counter, hotels_location, houses_location, utilities_counter, dice_value



    #this means the location is owned by somebody
    if location[checked_location] > 0:


        #this means that the location is owned by somebody else
        if location[checked_location] != player + 1 and location[checked_location] <= 6:
            # player pays the rent
            if hotels_location[checked_location] == 1:
                rent = 5 * location_price[checked_location]
            elif houses_location[checked_location] == 4:
                rent = 4 * location_price[checked_location]
            elif houses_location[checked_location] == 3:
                rent = 7 * location_price[checked_location]
                rent = rent / 2
            elif houses_location[checked_location] == 2:
                rent = 3 * location_price[checked_location]
                rent = rent / 2
            elif houses_location[checked_location] == 1:
                rent = location_price[checked_location] / 4
            elif houses_location[checked_location] == 0:
                rent = location_price[checked_location] / 10
            check_pay = player_money[player]
            pay(player, rent, 0)
            if (check_pay > player_money[player]):
                player_money[location[checked_location] - 1] = player_money[location[checked_location] - 1] + location_price[checked_location]
            else:
                player_money[location[checked_location] - 1] = player_money[location[checked_location] - 1] + check_pay
        elif location[checked_location] > 6 and location[checked_location] <= 12 and location[checked_location] != player + 7:
            #player pays depending on the number of owned servers by the owner
            check_pay = player_money[player]
            pay(player, 25 * (2**(server_counter[location[checked_location] - 7] - 1)), 0)
            if (check_pay > player_money[player]):
                player_money[location[checked_location] - 7] = player_money[location[checked_location] - 7] + 25 * (2**(server_counter[location[checked_location] - 7] - 1))
            else:
                player_money[location[checked_location] - 7] = player_money[location[checked_location] - 7] + check_pay
        elif location[checked_location] > 12 and location[checked_location] != player + 13:
            # player pays depending on the number of owned utilities by the owner
            check_pay = player_money[player]
            amout = 0
            if utilities_counter[location[checked_location] - 13] == 1:
                amount = 4 * dice_value
                pay(player, 4 * dice_value, 0)
            elif utilities_counter[location[checked_location] - 13] == 2:
                amount = 10 * dice_value
                pay(player, 10 * dice_value, 0)
            if (check_pay > player_money[player]):
                player_money[location[checked_location] - 13] = player_money[location[checked_location] - 13] + amount
            else:
                player_money[location[checked_location] - 13] = player_money[location[checked_location] - 13] + check_pay



    else:
        # buying a location
        answer = input("Do you want to buy this location? [y/n]")
        if answer[0] == 'y':
            check_pay = player_money[player]
            pay(player, location_price[checked_location], 1)
            #we check if the player afforded to pay for the location
            if (check_pay > player_money[player]):
                #we check if it's server
                if(checked_location == 5 or checked_location == 15 or checked_location == 25 or checked_location == 35):
                    server_counter[player] = server_counter[player] + 1
                    location[checked_location] = player + 7
                #we check if it's a utility
                elif(checked_location == 12 or checked_location == 28):
                    utilities_counter[player] = utilities_counter[player] + 1
                    location[checked_location] = player + 13
                else:
                    location[checked_location] = player + 1




# function for buying houses or hotels
#player is from 0-5
def buy_houses(player):

    global location, houses_location, player_money, location_price, hotels_location


    #buying houses
    answer = input("Do you want to buy some houses? [y/n]")
    if answer[0] == 'y':
        answer1 = input("Where do you want to place the houses? [insert location(0-39)]")
        answer1 = int(answer1)

        #now let's check if the player actually owns the location
        while(location[answer1] != player + 1):
            print("You don't own that location or this is a server!")
            answer1 = input("Where do you want to place the houses? [insert location(0-39)]")
            answer1 = int(answer1)


        answer2 = input("How many houses do you want to buy? [You can have max 4 houses there!]")
        answer2 = int(answer2)

        # now let's check if those houses can actually be placed there
        while (houses_location[answer1] + answer2 >4):
            answer2 = input("How many houses do you want to buy? [You can have max 4 houses there!]")
            answer2 = int(answer2)


        check_bought = player_money[player]
        pay(player, answer2 * location_price[answer1] * 2/5, 1)
        if(player_money[player] < check_bought):
            houses_location[answer1] = houses_location[answer1] + answer2
        else:
            print("You don't have enough money!!!")



        #now let's see if the player wants to buy a hotel...
        answer = input("Do you want to buy a hotel? [y/n]")
        if answer[0] == 'y':
            answer1 = input("Where do you want to buy the hotel? [insert location(0-39)]")
            answer1 = int(answer1)

            # now let's check if the player actually owns the location
            while (location[answer1] != player + 1):
                print("You don't own that location!")
                answer1 = input("Where do you want to place the hotel? [insert location(0-39)]")
                answer1 = int(answer1)

            # now let's check if the hotel can actually be placed there
            if(houses_location[answer1] != 4 or hotels_location[answer1] != 0):
                print("You can't place a hotel here!!!")

            check_bought = player_money[player]
            pay(player, location_price[answer1] * 2, 1)
            if (player_money[player] < check_bought):
                houses_location[answer1] = 0
                hotels_location[answer1] = 1
            else:
                print("You don't have enough money!!!")


    #Carla's work
    #if(buy):
        #global money = money - location_price * 0.25 # the player pays for the house
        #global house_location[location]++; # the number of houses on that location increases




# function that checks why the player is skipped
#player is from 0-5
def checkskip(player):

    global player_escape, skip, player_money

    #skip = 1 when the player is in the tutors room
    if (skip[player] == 1):
        if(player_escape[player] == 1):
            answer = input("Do you want to use your\"Escape the Tutor's room card\"? [y/n]")
            if(answer[0] == "y"):
                skip[player] = 0
                player_escape[player] = 0
        #if the player either doesn't have the escape card, or doesn't want to use it, he has to pay 50

        check_payed = player_money[player]
        pay(player, 50, 0)
        if(check_payed > player_money[player]):
            skip[player] = 0
            print("You got out of prison!")


    #if skip = 2 we don't do anything cause the player lost and there is nothing we can 'bout that



    #Carla's code

    #if(skip == 1): # skip =1 when the player is in the tutors room
            #if(escape ==2):# check for escape card from prison: if =2 then the player wants to use it
                #skip ==0
    #if(skip == 2): # check if the player lost so that it is skipped each round until the end of the game
            #player = player +1    # moves to the next player



# function that moves players
#player is from 0-5
#value_dice is from 2 to 12
def move_player(player, value_dice):

    global player_location, player_money

    player_location[player] = player_location[player] + value_dice
    # checks if the player has passed startx
    if(player_location[player]>40):
        player_money[player] = player_money[player] + 200
        player_location[player] = player_location[player] % 40
    # checks if the player has landed on startx
    elif(player_location[player]== 40):
        player_money[player] = player_money[player] + 400
        player_location[player] = 0


#this function checks on what type of location the player landed
#player is from 0-5
def check_place(player):

    global player_location, location, player_money, location_price, eduroam_money, skip

    #just a variable
    check_location = player_location[player]

    # deadlines
    if(location[check_location] == -1):
        deadlines(player)
        return

    # mitigating_circumstances
    elif(location[check_location] == -2):
        mitigating_circumstances(player)
        return

    #stuff to pay(vending machine, rent, tuition fees, microwave)
    elif(location[check_location] == -3):
        check_paid = player_money[player]
        #the player pays
        pay(player, location_price[check_location], 0)
        #if he paid, the payed money goes to eduroam
        if (check_paid > player_money[player]):
            eduroam_money = eduroam_money + location_price[check_location]
        #if he didn't pay, he lost and all his money go to eduroam
        else:
            eduroam_money = eduroam_money + player_money[player]


    #if a player lands on tutor's room, nothing happens, he's just visiting


    #landing on eduroam
    elif(location[check_location] == -5):
        player_money[player] = player_money[player] + eduroam_money
        eduroam_money = 0

    #go to tutor's room
    elif(location[check_location] == -6):
        skip[player] = 1
        player_location[player] = 10

    #ownable location...
    elif (location[check_location] >= 0):
        check_ownable_locations(check_location, player)




#GLOBAL DECLARED VARIABLES HERE

location = []                       #this list tells us what kind of location each location is
                                    #(indicies: 0-39)
                                    #values: 0 -> ownable, nobody owns it
                                    #        1-6 -> location where houses can be placed, owned by player i
                                    #        7-12 -> server, owned by player i-6
                                    #        -1 -> deadlines
                                    #        -2 -> mitigating circumstances
                                    #        -3 -> pay stuff (rent, tuition fees)
                                    #        -4 -> tutor's room
                                    #        -5 -> eduroam
                                    #        -6 -> go to tutor's room
                                    #        -7 -> startx
                                    #        13-18 -> utilities(vending machine, microwave)
player_money = []                   #this list tells us the amount of money each player has
                                    #(indicies: 0-5 aka player number - 1)
location_price = []                 #this list tells us what is the price of each location, or the price of a house if someone
                                    #has houses there, or of a hotel if someone owns a hotel there
                                    #(indicies: 0-39)
skip = []                           #this list tells use which players are in prison or lost
                                    #(indicies: 0-5)
                                    #(values; 0->he is not skipped, 1->he is in tutors room, 2->he lost)
hotels_location = []                #this list tells us if there are hotels on a property
                                    #(indicies: 0-39)
                                    #(values: 0-> no hotel here, 1-> hotel here)
houses_location = []                #this list tells us how many houses are on a property
                                    #(indicies: 0-39)
                                    #(values: 0-> no houses here, i-> i houses here)
player_location = []                #this list tells us where each player is
                                    #(indicies: 0-5)
                                    #(values: 0-39-> the player's location)
player_escape = []                  #this list tells us if the player has an escape the tutors room card
                                    #(indicies: 0-5)
                                    #(values: 0-> the player doesn't own a card, 1-> the player owns a card)
server_counter = []                 #this list tells us how many servers each player owns
                                    #(indicies: 0-5)
                                    #(values: 0-4 -> the number of servers owned by the player)
utilities_counter = []              # this list tells us how many utilities each player owns
                                    # (indicies: 0-5)
                                    # (values: 0-2 -> the number of utilities owned by the player)

eduroam_money = 0                   #this variable tells us how many money a player gets for when he lands on eduroam
roll_counter = 0                    #this variable counts how many time a player rolled the dice
dice_value = 0                      #this variable tells us how much a player rolled


#MAIN program starts here


#initialising the board
for i in range (40):
    houses_location.append(0)
    hotels_location.append(0)
    #this is just a place holder for now...
    # we are going to introduce each locations price
    location_price.append(0)
    location.append(0)

#we have to manually update each unownable location
location[0] = -7
location[2] = -2
location[4] = -3
location[7] = -1
location[10] = -4
location[17] = -2
location[20] = -5
location[22] = -1
location[30] = -6
location[33] = -2
location[36] = -1
location[38] = -3


#we initialise all location_price
location_price[1] = 60
location_price[3] = 60
location_price[4] = 200
location_price[5] = 200
location_price[6] = 100
location_price[8] = 100
location_price[9] = 120
location_price[11] = 140
location_price[12] = 150
location_price[13] = 140
location_price[14] = 160
location_price[15] = 200
location_price[16] = 180
location_price[18] = 180
location_price[19] = 200
location_price[21] = 220
location_price[23] = 220
location_price[24] = 240
location_price[25] = 200
location_price[26] = 260
location_price[27] = 260
location_price[28] = 150
location_price[29] = 260
location_price[31] = 300
location_price[32] = 300
location_price[34] = 320
location_price[35] = 200
location_price[37] = 350
location_price[38] = 100
location_price[39] = 400




#finding out the number of players
no_players = input("Insert the number of players(2-6): ")
no_players = int(no_players)


#number of players still playing
no_remaining_player = no_players


#initialising our lists related to the number of players
for i in range (no_players):
    #each player starts with 1500 K...something
    player_money.append(1500)
    #each player starts on the position 0, aka on startx
    player_location.append(0)
    #each player starts with skip = 0
    skip.append(0)
    #each player starts with no escape card
    player_escape.append(0)
    #each player starts with 0 servers
    server_counter.append(0)
    utilities_counter.append(0)



#the main game loop starts here
#the game ends when there is only  1 player left
while no_remaining_player > 1:


    #this for gives each player's turn
    for player_turn in range (no_players):
        print("It's " + str(player_turn + 1) + "'s player turn!")

        #first thing first, if the player is not in prison or didn't lose he can buy houses


        #we check if the player rolls the dice this turn
        if (skip[player_turn] > 0):
            #we check why the player is skiped, like if he is in tutor's room or he lost
            checkskip(player_turn)
        else:
            buy_houses(player_turn)
            #now the dice roll for the players
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice_value = dice1 + dice2
            print("You rolled " + str(dice1) + " with " + str(dice2))
            roll_counter = 1
            move_player(player_turn, dice_value)
            print("You landed on " + str(player_location[player_turn]))
            print("You have " + str(player_money[player_turn])+ " money!")
            check_place(player_turn)
            print("You landed on " + str(player_location[player_turn]))
            print("You have " + str(player_money[player_turn]) + " money!")
            while dice1 == dice2 and roll_counter < 4 and skip == 0:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                dice_value = dice1 + dice2
                print("You rolled " + str(dice1) + " with " + str(dice2))
                roll_counter = roll_counter + 1
                if dice1 == dice2 and roll_counter == 3:
                    skip = 1
                    player_location[player_turn] = 10
                else:
                    move_player(player_turn, dice_value)
                    print("You landed on " + str(player_location[player_turn]))
                    print("You have " + str(player_money[player_turn]) + " money!")
                    check_place(player_turn)
                    print("You landed on " + str(player_location[player_turn]))
                    print("You have " + str(player_money[player_turn]) + " money!")

        if no_remaining_player == 1:
            for k in range (no_players):
                if skip[k] != 2:
                    print("Player " + str(k+1) + "WON!!!")
            break













#these are just gonna be some checks for check_ownable_locations()

#location.append(1)
#location.append(0)

#check_ownable_locations(0, 1)

#player_money.append(0)
#player_money.append(0)
#player_money.append(1500)
#location_price.append(250)
#check_ownable_locations(0, 2)
#print(player_money[2])

#location_price.append(250)
#location_price.append(350)
#player_money.append(0)
#player_money.append(1500)
#check_ownable_locations(1, 1)
#print(player_money[1])
#print(location[1])