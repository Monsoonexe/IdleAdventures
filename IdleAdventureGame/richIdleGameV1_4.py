#richIdleGameV1.2

import battleModule
import characterClass
import enemyModule
import GameState
import itemModule
import moveDictionary
import partyModule
import playerBackpack
import random
import time

def enterTown():
    innCost = 50
    sleepTime = .5

    print("***The Party rests in a town\n")
    if(PARTY.getMoney() >= innCost and PARTY.HPLow()):
        print("***The Party spends the night at the inn\n")
        PARTY.rest()
        PARTY.spendMoney(innCost)
        time.sleep(sleepTime)
    else:
        print("***The Party decides not to sleep at the inn\n")

    if(PARTY.getMoney() > 100):
        visitShop()

def visitShop():
    pass
    print("The Party visits the shop\n")
    swordCost = 500
    potionCost = 15
    manaPotionCost = 20
    spellBookCost = 50
    armorUpgradeCost = 25

##
##    while(PARTY.getMoney() > 75):
##        choice = random.randint(0, 4)
##        if(Arpa.money == potionCost and choice == 0):
##            print(Arpa.name, "buys a potion!\n")
##            Arpa.money -= potionCost
##            Arpa.potions += 1
##            
##        if(Arpa.money > swordCost and choice == 1):
##            print("***", Arpa.name, "buys a fancy new sword!\n")
##            Arpa.money -= swordCost
##            Arpa.baseAtk += 2
##
##        if(Arpa.money > spellBookCost and choice == 2):
##            print(Arpa.name, "buys a new spell book!\n")
##            Arpa.money -= spellBookCost
##            Arpa.magicPower += 2
##
##        if(Arpa.money > armorUpgradeCost and choice == 3):
##            print(Arpa.name, "gets his armor chiseled!\n")
##            Arpa.money -= armorUpgradeCost
##            Arpa.dfs += 1
##        else:
##            break

def checkForTown(totalDistance, distanceRemaining, KMSinceLastTown):#returns True or False
    numOfTowns = 12 #default 12
    townRate = totalDistance / numOfTowns
    if(KMSinceLastTown > townRate):
        townCheckRoll = random.randint(0, 99)
        if(townCheckRoll < 20): #21% chance to run into a town
            return True    
    else: False

def setDestination():
    destinationRoll = random.randint(0, 99)#destination roll
    distance = 0 #distance to goal
    if(destinationRoll < 32):
        print("The Party gathers together and decides to hunt for treasure!")
        print("Rumor has it the greedy Dragon of Uuragorn keeps a hoard of rightous gold")
        print("stolen from church keeps and storerooms.")
        distance = random.randint(3000, 5000)
    elif(destinationRoll < 65):
        print("The party decides that the harassment of Kimona Village by the")
        print("Gadiantan Raiders has gone on long enough!")
        print("They devise a daring strategy to cut of the snake's head")
        print("They plan to target the leader of the nefarious Gadiantan Raiders")
        print("Spies inform of a route he is taking.  Cut him off at the pass!")
        distance = random.randint(2000, 4000)
    else:
        print("Take this ring to Mordor, Frodo!")
        distance = random.randint(5000, 7000) 
    return distance

def checkStats():
    PARTY.showPartyStats()
    exit(0)
    
def main():
    random.seed()
    roundTime = 1
    goalDistance = setDestination()
    goalDistanceRemaining = goalDistance
    print("Distance to next Dungeon:", int(goalDistanceRemaining))
    print("Our heroes wave goodbye to their hometown, and set off on their first adventure!")
    #print()#line break
    KMSinceLastTown = 0
    while (PARTY.isAlive() and goalDistanceRemaining > 0):
        print("Distance to go:", int(goalDistanceRemaining))#show distance to target
        print("The party treks forward...")#dialogue
        #checkStats()
        #PARTY.passiveRegen() #party heals over time
        print()#line break
        partyMoveDistance = int(roundTime * PARTY.getWalkingSpeed()) #party's likely move distance
        partyMoveDistance *= random.randint(95, 105) / 100 #random +- 5% distance
        if (goalDistanceRemaining < 1):
            print("THE PARTY ARRIVED AT ITS DESTINATION!!!  YOU WIN!!!")
            break
        #If party is w/n proximity of a town...
        if (checkForTown(goalDistance, goalDistanceRemaining, KMSinceLastTown)):
            enterTown()
            KMSinceLastTown = 0 #at a town
            partyMoveDistance = 0 #does not move
        #does party come across baddies?
        elif(enemyModule.encounterCheck(PARTY.getLevel())):
            if(battleModule.initBattle(PARTY)):
                print("The heroes won the battle!\n")
            else:
                print("The party has died in battle")
                break
            print("The party trudges on...\n")
            partyMoveDistance /= 10 #party didn't move as much due to battle
            
            
        #elif(True):#party decides to make camp

            
        #time.sleep(roundTime) #time-based mechanic
        goalDistanceRemaining -= int(partyMoveDistance) #move towards goal
        KMSinceLastTown += int(partyMoveDistance) #increase distance from town
    print("Distance Remaining:", goalDistanceRemaining)   
    print("GAME OVER")

#initialize game
MOVES = moveDictionary.moveDictionary()            
PARTY = partyModule.Party()
main()
