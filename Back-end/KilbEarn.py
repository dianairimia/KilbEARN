import random


#we use this function to pay
#player is the player who has to pay, it's from 0-5
#amount is the sum the player has to pay
#optinality tells us if the player is forced to pay: 1-he doesn't; 0-he does
def pay(player, amount, optionality):



    #global variables
    global player_money, skip, houses_location, location, no_remaining_player, paid_test



    #if the player has enough money, he pays
    if player_money[player] > amount:
        player_money[player] = player_money[player] - amount
        paid_test = 0


    #check if the player HAS to pay
    elif optionality == 0:


        # the player lost if he ran out of money
        print("YOU LOST!")
        skip[player] = 2
        no_remaining_player = no_remaining_player - 1

        #if a player loses, he loses all his locations and houses and hotels

        for i in range(40):
            if location[i] == player + 1:
                houses_location[i] = 0
                location[i] = 0



def mitigating_circumstances(player):
    global player_money
    global player_location
    global no_remaining_player
    global eduroam_money
    global location_price
    global location
    global skip
    global paid_test
    global dice1, dice2, dice_value
    global no_players


    m = random.randint(1,10)
    if m == 1:    # Advance to "Startx". (Collect K 400)
        print("Advance to Startx. Collect K 400")
        player_location[player] == 0
        player_money[player] += 400

    if m==2: # Advance to "Byte Cafe" and relax. If you pass through the Startx, collect k 200. If owned, you do not need to pay, if unowned, you can buy it from the Bank.
        print("Advance to Byte Cafe and relax. If you pass through the Startx, collect k 200. If owned, you do not need to pay, if unowned, you can buy it from the Bank.")
        if(player_location[player]>27):
            player_money[player] +=200
        player_location[player] = 27
        if location[27]==0:
            check_ownable_locations(27, player)



    if m ==3: # You have been elected the chair of the tutorials for the rest of the semester. Collect k 25 from each player.
        print("You have been elected the chair of the tutorials for the rest of the semester. Collect k 25 from each player.")
        for i in range(no_players):
            if skip[i] != 2 and i != player:
                paid_test = 1   # player didnt pay
                initial_money = player_money[i]
                pay(i, 25, 0)
                if paid_test == 0:
                    player_money[player] = player_money[player] + 25
                else:
                    player_money[player] += initial_money




    if m ==4: # Go directly to the tutor's room. If you pass through Startx do not collect K 200.
        print("Go directly to the tutor's room. If you pass through Startx do not collect K 200.")
        player_location[player] = 10
        skip[player] = 1

    if m == 5: # Advance token to nearest server. If unowned, you may buy it from the Bank. If owned, pay owner a total 10 times the amount thrown.
        print("Advance token to nearest Server. If unowned, you may buy it from the Bank. If owned, pay owner a total 10 times the amount thrown.")
        if player_location[player] >=0 and player_location[player]<5:
            player_location[player] = 5
            loc = 5

        if player_location[player] >=5 and player_location[player]<15:
            player_location[player] = 15
            loc = 15

        if player_location[player] >=15 and player_location[player]<25:
            player_location[player] = 25
            loc = 25

        if player_location[player] >=25 and player_location[player]<35:
            player_location[player] = 35
            loc = 35
        if player_location[player] >=35 and player_location[player]<=39:
            player_location[player] = 5
            loc = 5
            player_money[player] += 200

        if location[player_location[player]]>0:
            ### roll dice -- pay 10 times the amount thrown
            owner = location[player_location[player]] - 7
            dice_roll()
            print("You have thrown" + str(dice1) + " "+ str(dice2) + " ")
            paid_test = 1   # player didnt pay
            initial_money = player_money[player]
            pay(player, 10*dice_value, 0)
            if paid_test == 0:
                player_money[owner] += 10*dice_value
            else:
                player_money[owner] += initial_money
        else:
            check_ownable_locations(loc, player)

    if m==6: #Congratulations! You won a hackathon. Collect k 100.
        print("Congratulations! You won a hackathon. Collect k 100.")
        player_money[player] += 100

    if m ==7: # Learn more about the mitigating circumstances policy. Advance to the Student Support Office. If you pass through STARTX collect k 200. If owned, pay the rent. If unowned, you may buy it from the Bank.
        print("Learn more about the mitigating circumstances policy. Advance to the Student Support Office. If you pass through STARTX collect k 200. If owned, pay the rent. If unowned, you may buy it from the Bank.")
        if player_location[player] > 16:
            player_money[player] += 200
        player_location[player] = 16
        check_ownable_locations(16, player)

    if m==8:  #Ah for crying out loud. You have an infinite loop and do not know how to solve it. Ask for help and pay k 50.
        print("Ah for crying out loud. You have an infinite loop and do not know how to solve it. Ask for help and pay k 50.")
        paid_test = 1   # player didnt pay
        initial_money = player_money[player]
        pay(player, 50, 0)
        if paid_test == 0:
            eduroam_money += 50
        else:
            eduroam_money += initial_money


    if m==9:# Unfortunately, you were not able to sit the exams. Go to Startx. Do not collect k400.
        print("Unfortunately, you were not able to sit the exams. Go to Startx. Do not collect k400.")
        player_location[player] = 0

    if m==10: #Advance to the Lecture Theatre 1.2. If you pass through Startx do not collect k200. If owned, you do not have to pay the rent. If unowned, you may buy it from the Bank.
        print("Advance to the Lecture Theatre 1.2. If you pass through Startx do not collect k200. If owned, you have to pay the rent. If unowned, you may buy it from the Bank.")
        player_location[player] = 13
        check_ownable_locations(13, player)



def deadlines(player):
    global eduroam_money
    global player_money
    global player_location
    global houses_location
    global location_price
    global paid_test
    global location
    global dice1, dice2, dice_value
    global no_players

    d = random.randint(1,10)
    if d==1:   #You missed a deadline. Pay k 50.
        print("You missed a deadline. Pay k 50.")
        paid_test = 1   # player didnt pay
        initial_money = player_money[player]
        pay(player, 50, 0)
        if paid_test == 0:
            eduroam_money += 50
        else:
            eduroam_money += initial_money



    if d==2:  #You need to add optimisation to your code. Pay k 75.
        print("You need to add optimisation to your code. Pay k 75.")
        paid_test = 1   # player didnt pay
        initial_money = player_money[player]
        pay(player, 75, 0)
        if paid_test == 0:
            eduroam_money += 75
        else:
            eduroam_money += initial_money



    if d==3: # You are behind with your work. Go to the tutor's room and ask for help. If you pass through Startx collect k 200.
        print("You are behind with your work. Go to the tutor's room and ask for help. If you pass through Startx collect k 200.")
        if player_location[player] >10:
            player_money[player] += 200
        player_location[player] = 10

    if d==4: # Your new coursework is raising your concerns. You do not know if you will finish it on time. Go to Tooltil O and work. If you pass through Startx collect k200. If owned pay the rent, if unowned can buy it.
        print("Your new coursework is raising your concerns. You do not know if you will finish it on time. Go to Tooltil O and work. If you pass through Startx collect k200. If owned pay the rent, if unowned can buy it.")
        if(player_location[player]>37):
            player_money[player] +=200
        player_location[player] = 37

    if d==5: #Midterms are rapidly approaching and you should focus on your work. Collect k 100 that would help you throughout this time.
        print("Midterms are rapidly approaching and you should focus on your work. Collect k 100 that would help you throughout this time.")
        player_money[player] += 100

    if d==6: # You have finished your work on time. You deserve a treat. Collect k 50.
        print("You have finished your work on time. You deserve a treat. Collect k 50.")
        player_money[player] += 50


    if d==7: # You need to finish your work on time. Go to LF 31. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 5 times the amount thrown.  If you pass through Startx collect k 200.
        print("You need to finish your work on time. Go to LF 31. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 5 times the amount thrown.  If you pass through Startx collect k 200.")
        if player_location[player] > 6:
            player_money[player]+=200
        player_location[player] = 6
        if location[6] >0:
            print("Throw dice again! ")
            dice_roll()
            print("You have thrown " + str(dice1) + " "+ str(dice2))
            paid_test = 1   # player didnt pay
            initial_money = player_money[player]
            pay(player, 5*dice_value, 0)
            if paid_test == 0:
                player_money[location[6]-1] += 5 * dice_value
            else:
                 player_money[location[6]-1] += initial_money



    if d==8: #You need to give your final presentation. Pay each player k 25.
        print("You need to give your final presentation. Pay each player k 25.")
        for i in range(0, no_players):
            if player != i and skip[i] != 2:
                paid_test = 1   # player didnt pay
                initial_money = player_money[player]
                pay(player, 25, 0)
                if paid_test == 0:
                    player_money[i] += 25
                else:
                    player_money[i] += initial_money


    if d==9:#   Demo presentation before holiday. Pay k75.
        print("Demo before holiday. Pay k75.")
        paid_test = 1   # player didnt pay
        initial_money = player_money[player]
        pay(player, 75, 0)
        if paid_test == 0:
            eduroam_money += 75
        else:
            eduroam_money += initial_money



    if d==10: # Final report deadline. Go to the Quiet Room and finish your report. If owned, pay 2 times the rent. If unowned, you may buy it. If you pass through Startx collect k200.
        print("Final report deadline. Go to the Quiet Room and finish your report. If owned, pay 2 times the rent. If unowned, you may not buy it. If you pass through Startx collect k200.")
        if player_location[player] > 26:
            player_money[player] += 200
        player_location[player] = 26
        if location[26]>0:
            if location[6] != player + 1 and location[6] <= 6:
                # player pays the rent
                if houses_location[6] == 5:
                    rent = 5 * location_price[6]
                elif houses_location[6] == 4:
                    rent = 4 * location_price[6]
                elif houses_location[6] == 3:
                    rent = 7 * location_price[6]
                    rent = rent / 2
                elif houses_location[6] == 2:
                    rent = 3 * location_price[6]
                    rent = rent / 2
                elif houses_location[6] == 1:
                    rent = location_price[6] / 4
                elif houses_location[6] == 0:
                    rent = location_price[6] / 10
                paid_test = 1
                initial_money = player_money[player]
                pay(player, 2 * rent, 0)
                if (paid_test == 0):
                    player_money[location[6] - 1] = player_money[location[6] - 1] + 2* rent
                else:
                    player_money[location[6] - 1] = player_money[location[6] - 1] + initial_money





#you get into the function only if location[check_location] >= 0 (location is ownable)
#checked_location is the location currently checked, it's from 0-39
#player is the number of the player for which we do these checks, it's from 0-5
def check_ownable_locations(checked_location, player):



    #global variables
    global location, player_money, location_price, server_counter, houses_location, utilities_counter, dice_value, paid_test



    #this means the location is owned by somebody
    if location[checked_location] > 0:


        #this means that the location is owned by somebody else
        if location[checked_location] != player + 1 and location[checked_location] <= 6:
            # player pays the rent
            if houses_location[checked_location] == 5:
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
            paid_test = 1
            initial_money = player_money[player]
            pay(player, rent, 0)
            if (paid_test == 0):
                player_money[location[checked_location] - 1] = player_money[location[checked_location] - 1] + rent
            else:
                player_money[location[checked_location] - 1] = player_money[location[checked_location] - 1] + initial_money
        elif location[checked_location] > 6 and location[checked_location] <= 12 and location[checked_location] != player + 7:
            #player pays depending on the number of owned servers by the owner
            paid_test = 1
            initial_money = player_money[player]
            pay(player, 25 * (2**(server_counter[location[checked_location] - 7] - 1)), 0)
            if (paid_test == 0):
                player_money[location[checked_location] - 7] = player_money[location[checked_location] - 7] + 25 * (2**(server_counter[location[checked_location] - 7] - 1))
            else:
                player_money[location[checked_location] - 7] = player_money[location[checked_location] - 7] + initial_money
        elif location[checked_location] > 12 and location[checked_location] != player + 13:
            # player pays depending on the number of owned utilities by the owner
            paid_test = 1
            initial_money = player_money[player]
            amout = 0
            if utilities_counter[location[checked_location] - 13] == 1:
                amount = 4 * dice_value
                pay(player, 4 * dice_value, 0)
            elif utilities_counter[location[checked_location] - 13] == 2:
                amount = 10 * dice_value
                pay(player, 10 * dice_value, 0)
            if (paid_test == 0):
                player_money[location[checked_location] - 13] = player_money[location[checked_location] - 13] + amount
            else:
                player_money[location[checked_location] - 13] = player_money[location[checked_location] - 13] + initial_money



    else:
        # buying a location
        answer = input("Do you want to buy this location? [y/n]")
        if answer[0] == 'y':
            paid_test = 1
            pay(player, location_price[checked_location], 1)
            #we check if the player afforded to pay for the location
            if (paid_test == 0):
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
def buy_houses(player, checked_location):

    global location, houses_location, player_money, location_price, paid_test

    #buying houses

    #check if the player actually owns the location or can still place a house
    if location[checked_location] == player + 1 and houses_location[checked_location] < 6:
        paid_test = 1
        pay(player, location_price[checked_location] * 2/5, 1)
        if(paid_test == 0):
            houses_location[checked_location] = houses_location[checked_location] + 1






# function that checks why the player is skipped
#player is from 0-5
def checkskip(player):

    global player_escape, skip, player_money, paid_test

    #skip = 1 when the player is in the tutors room
    if (skip[player] == 1):
        if(player_escape[player] == 1):
            answer = input("Do you want to use your\"Escape the Tutor's room card\"? [y/n]")
            if(answer[0] == "y"):
                skip[player] = 0
                player_escape[player] = 0
        #if the player either doesn't have the escape card, or doesn't want to use it, he has to pay 50

        paid_test = 1
        pay(player, 50, 0)
        if(paid_test == 0):
            skip[player] = 0
            print("You paid 50k and got out of prison!")


    #if skip = 2 we don't do anything cause the player lost and there is nothing we can 'bout that




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

    global player_location, location, player_money, location_price, eduroam_money, skip, paid_test

    #just a variable
    check_location = player_location[player]

    # deadlines
    if(location[check_location] == -1):
        deadlines(player)

    # mitigating_circumstances
    elif(location[check_location] == -2):
        mitigating_circumstances(player)

    #stuff to pay(rent, tuition fees)
    elif(location[check_location] == -3):
        paid_test = 1
        initial_money = player_money[player]
        #the player pays
        pay(player, location_price[check_location], 0)
        #if he paid, the payed money goes to eduroam
        if (paid_test == 0):
            eduroam_money = eduroam_money + location_price[check_location]
        #if he didn't pay, he lost and all his money go to eduroam
        else:
            eduroam_money = eduroam_money + initial_money


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



#a function for rolling the dice
def dice_roll():
    global dice1, dice2, dice_value
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_value = dice1 + dice2



def no_player():


def main():
    #GLOBAL DECLARED VARIABLES HERE
    global location
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
    global player_money
    player_money = []                   #this list tells us the amount of money each player has
                                        #(indicies: 0-5 aka player number - 1)
    global location_price
    location_price = []                 #this list tells us what is the price of each location, or the price of a house if someone
                                        #has houses there, or of a hotel if someone owns a hotel there
                                        #(indicies: 0-39)
    global skip
    skip = []                           #this list tells use which players are in prison or lost
                                        #(indicies: 0-5)
                                        #(values; 0->he is not skipped, 1->he is in tutors room, 2->he lost)
    global houses_location
    houses_location = []                #this list tells us how many houses are on a property
                                        #(indicies: 0-39)
                                        #(values: 0-> no houses here, if i < 5 -> i houses here, if i==5 hotel here)
    global player_location
    player_location = []                #this list tells us where each player is
                                        #(indicies: 0-5)
                                        #(values: 0-39-> the player's location)
    global player_escape
    player_escape = []                  #this list tells us if the player has an escape the tutors room card
                                        #(indicies: 0-5)
                                        #(values: 0-> the player doesn't own a card, 1-> the player owns a card)
    global server_counter
    server_counter = []                 #this list tells us how many servers each player owns
                                        #(indicies: 0-5)
                                        #(values: 0-4 -> the number of servers owned by the player)
    global utilities_counter
    utilities_counter = []              # this list tells us how many utilities each player owns
                                        # (indicies: 0-5)
                                        # (values: 0-2 -> the number of utilities owned by the player)

    global eduroam_money
    eduroam_money = 0                   #this variable tells us how many money a player gets for when he lands on eduroam
    global roll_counter
    roll_counter = 0                    #this variable counts how many time a player rolled the dice
    global dice_value
    dice_value = 0                      #this variable tells us how much a player rolled
    global paid_test
    paid_test = 0                      #this variable tells us if a payment was made succesfully or not
    global dice1, dice2
    dice1 = 0
    dice2 = 0                           #these are the 2 values for the 2 dice


    #ACTUAL MAIN program starts here


    #initialising the board
    for i in range (40):
        houses_location.append(0)
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
    global no_players
    no_players = input("Insert the number of players(2-6): ")
    no_players = int(no_players)


    #number of players still playing
    global no_remaining_player
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
        # each player starts with 0 utilities
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
                #now the dice roll for the players
                dice_roll()
                print("You rolled " + str(dice1) + " with " + str(dice2))
                roll_counter = 1
                move_player(player_turn, dice_value)
                print("You landed on " + str(player_location[player_turn]))
                print("You have " + str(player_money[player_turn])+ " money!")
                check_place(player_turn)
                print("You landed on " + str(player_location[player_turn]))
                print("You have " + str(player_money[player_turn]) + " money!")
                while dice1 == dice2 and roll_counter < 4 and skip[player_turn] == 0:
                    print("You rolled a double!")
                    dice_roll()
                    print("You rolled " + str(dice1) + " with " + str(dice2))
                    roll_counter = roll_counter + 1
                    if dice1 == dice2 and roll_counter == 3:
                        skip[player_turn] = 1
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

main()

