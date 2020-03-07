def mitigating_circumstances(player):
<<<<<<< HEAD
    global player_money
    global player_location
    global no_remaining_player
    global eduroam_money

=======
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
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
<<<<<<< HEAD
        for i in range(3):
            if skip[i] != 2 and i!= player:
                player_money[i] -= 25
                player_money[player] +=25
=======
        for i in range(no_remaining_player):
            if i!=player:
                player_money[i] -= 25
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e


    if m ==4: # Go directly to the tutor's room. If you pass through Startx do not collect K 200.
        player_location[player]=10

<<<<<<< HEAD
    if m == 5: # Advance token to nearest the server2. If unowned, you may buy it from the Bank. If owned, pay owner a total 10 times the amount thrown.
=======
    if m == 5: # Advance token to nearest the server2. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown.
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
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
<<<<<<< HEAD
            println("Roll dice again")
            x= random.randint(1,7)
            y = random.randint(1,7)
            println("You have thrown" + x+ " "+ y+ " ")
            player_money[player] -= 10 * (x+y)

    if m==6: #Congratulations! You won a hackathon. Collect k 100.
        println("Congratulations! You won a hackathon. Collect k 100.")
        player_money[player] += 100

    if m ==7: # Get out of the tutor's room.
        println("Congratulations! You won a hackathon. Collect k 100.")
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
=======

        if m==6: #Congratulations! You won a hackathon. Collect k 100.
            player_money[player] += 100

        if m ==7: # Get out of the tutor's room.
            escape[player] = 2  ## the player can escape the tutors room

        if m==8:  #Ah for crying out loud. You got to an infinite loop and do not know how to solve it. Ask for help and pay k 50.
            player_money[player] -= 50
            eduroam_money +=50

        if m==9:# Unfortunately, you were not able to sit the exams. Go to Startx. Do not collect k200.
            player_location[player] = 0

        if m==10: #Advance to the Lecture Theatre 1.2. If you pass through Startx do not collect k200. If owned, you do not have to pay the rent. If unowned, you may buy it from the Bank.
            player_location[player] = 13
>>>>>>> 01da6567f7e5aaa3400989ed2ab30322e242333e
