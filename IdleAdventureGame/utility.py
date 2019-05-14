#utility.py
#bitches love utilities

def sortByBattleSpeed(actors): #highest speed first
    temp = None
    swapMade = True
    while swapMade:
        swapMade = False
        for counter in range(0, len(actors) - 1):
            if(actors[counter].getBattleSpeed() < actors[counter + 1].getBattleSpeed()):
                temp = actors[counter]
                actors[counter] = actors[counter + 1]
                actors[counter + 1] = temp
                swapMade = True

    return actors
