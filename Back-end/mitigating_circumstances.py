def mitigating_circumstances(player):
    m = random.randint(1,11);
    if m == 1:    # Advance to "Startx". (Collect K 200)
        player_location[player] == 0;
        player_money[player] += 200;

    if m==2: # Advance to "Byte Cafe" and relax. If you pass through the Startx, collect k 200. If owned, you do not need to pay, if unowned, you can buy it from the Bank.
        if(player_location[player]>27):
            player_money[player] +=200
        player_location[player] = 27
        if(location[27]>0):
            player_money[player] += rentprice ## need to change it later

    if m ==3: # You have been elected the chair of the tutorials for the rest of the semester. Collect k 25 from each player.
        player_money[player] += 25 * no_remaining_player;
        for i in range(no_remaining_player):
            if i!=player:
                player_money[i] -= 25


    if m ==4: # Go directly to the tutor's room. If you pass through Startx do not collect K 200.
        player_location[player]=10

    if m == 5: # Advance token to nearest the server2. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown.
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
