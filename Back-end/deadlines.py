def deadlines(player):
    d = random.randint(1,11)
    if d==1:   #You missed a deadline. Pay k 50.
        player_money[player] -= 50
        eduroam_money += 50

    if d==2:  #You need to add optimisation to your code. Pay k 75.
        player_money[player] -= 75
        eduroam_money += 75

    if d==3: # You are behind with your work. Go to the tutor's room and ask for help. If you pass through Startx collect k 200.
        if player_location[player] >10:
            player_money[player] += 200
        player_location[player] = 10

    if d==4: # Your new coursework is raising your concerns. You do not know if you will finish it on time. Go to Tooltil O and work. If you pass through Startx collect k200. If owned pay the rent, if unowned can buy it.
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
            # throw the dice ----


    if d==8: #You need to give your final presentation. Pay each player k 25.
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
        
