def deadlines(player):
<<<<<<< HEAD
    global euduroam_money
    global player_money
    global player_location
    global hotels_location
    global houses_location
    global location_price
    d = random.randint(1,11)
    if d==1:   #You missed a deadline. Pay k 50.
        println("You missed a deadline. Pay k 50.")
=======
    d = random.randint(1,11)
    if d==1:   #You missed a deadline. Pay k 50.
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
        player_money[player] -= 50
        eduroam_money += 50

    if d==2:  #You need to add optimisation to your code. Pay k 75.
<<<<<<< HEAD
        println("You need to add optimisation to your code. Pay k 75.")
=======
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
        player_money[player] -= 75
        eduroam_money += 75

    if d==3: # You are behind with your work. Go to the tutor's room and ask for help. If you pass through Startx collect k 200.
<<<<<<< HEAD
        println("You are behind with your work. Go to the tutor's room and ask for help. If you pass through Startx collect k 200.")
=======
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
        if player_location[player] >10:
            player_money[player] += 200
        player_location[player] = 10

    if d==4: # Your new coursework is raising your concerns. You do not know if you will finish it on time. Go to Tooltil O and work. If you pass through Startx collect k200. If owned pay the rent, if unowned can buy it.
<<<<<<< HEAD
        println("Your new coursework is raising your concerns. You do not know if you will finish it on time. Go to Tooltil O and work. If you pass through Startx collect k200. If owned pay the rent, if unowned can buy it.")
=======
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
        if(player_location[player]>37):
            player_money[player] +=200
        player_location[player] = 37

    if d==5: #Midterms are rapidly approaching and you should focus on your work. Collect k 100 that would help you throughout this time.
<<<<<<< HEAD
        println("Midterms are rapidly approaching and you should focus on your work. Collect k 100 that would help you throughout this time.")
        player_money[player] += 100

    if d==6: # You have finished your work on time. You deserve a treat. Collect k 50.
        println("You have finished your work on time. You deserve a treat. Collect k 50.")
=======
        player_money[player] += 100

    if d==6: # You have finished your work on time. You deserve a treat. Collect k 50.
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
        player_money[player] += 50


    if d==7: # You need to finish your work on time. Go to LF 31. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 5 times the amount thrown.  If you pass through Startx collect k 200.
<<<<<<< HEAD
        println("You need to finish your work on time. Go to LF 31. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 5 times the amount thrown.  If you pass through Startx collect k 200.")
=======
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
        if player_location[player] > 6:
            player_money[player]+=200
        player_location[player] = 6
        if location[6] >0:
<<<<<<< HEAD
            print("Throw dice again! ")
            x= random.randint(1,7)
            y = random.randint(1,7)
            println("You have thrown " + x + " "+ y)

            player_money[player] = player_money[player] -5*(x+y)




    if d==8: #You need to give your final presentation. Pay each player k 25.
        println("You need to give your final presentation. Pay each player k 25.")
=======
            # throw the dice ----


    if d==8: #You need to give your final presentation. Pay each player k 25.
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
        for i in range(0, no_remaining_player):
            player_money[player] -= 25
            player_money[i] += 25


    if d==9:#   Demo presentation before holiday. Pay k75.
<<<<<<< HEAD
        println("Demo presentation before holiday. Pay k75")
        player_money[player] -= 75

    if d==10: # Final report deadline. Go to the Quiet Room and finish your report. If owned, pay 2 times the rent. If unowned, you may buy it. If you pass through Startx collect k200.
        println("Final report deadline. Go to the Quiet Room and finish your report. If owned, pay 2 times the rent. If unowned, you may buy it. If you pass through Startx collect k200.")
        if player_location[player] > 26:
            player_money[player] += 200
        player_location[player] = 26

        if location[26]>0:
            if hotels_location[26] == 1:
                rent = 5 * location_price[26]
            elif houses_location[26] == 4:
                rent = 4 * location_price[26]
            elif houses_location[26] == 3:
                rent = 7 * location_price[26]
                rent = rent / 2
            elif houses_location[26] == 2:
                rent = 3 * location_price[26]
                rent = rent / 2
            elif houses_location[26] == 1:
                rent = location_price[26] / 4
            elif houses_location[26] == 0:
                rent = location_price[26] / 10

        player_money[player] -= 2*rent
=======
        player_money[player] -= 75

    if d==10: # Final report deadline. Go to the Quiet Room and finish your report. If owned, pay 2 times the rent. If unowned, you may buy it. If you pass through Startx collect k200.
        if player_location[player] > 26:
            player_money[player] += 200
        player_location[player] = 26
        if location[26]>0:
            player_money[player] -= rent*2 ### need to change variable
        
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
