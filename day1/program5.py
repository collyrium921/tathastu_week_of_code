run1 = int(input("Enter scores of player1: "))
run2 = int(input("Enter scores of player2: "))
run3 = int(input("Enter scores of player3: "))
sr1 = (run1/60)*100
sr2 = (run2/60)*100
sr3 = (run3/60)*100
print("strike rate of player1 is: ", sr1)
print("strike rate of player2 is: ", sr2)
print("strike rate of player3 is: ", sr3)
print("runs scored by player1 if 60 more balls are played is: ", sr1*2)
print("runs scored by player2 if 60 more balls are played is: ", sr2*2)
print("runs scored by player3 if 60 more balls are played is: ", sr3*2)
print("maximum number of sixes by player1 can be: ", sr1//6)
print("maximum number of sixes by player2 can be: ", sr2//6)
print("maximum number of sixes by player3 can be: ", sr3//6)
