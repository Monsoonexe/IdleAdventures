#battleModule
#bitches love battles!
import characterClass
import enemyModule
import random
import utility

def initBattle(heroParty): #this module's main() function
    enemyTeam = spawnEnemyTeam(heroParty)
    return battle(heroParty, enemyTeam)

def spawnEnemyTeam(heroParty):#returns list of enemies on team
    if(heroParty.getLevel() < 5):
        enemyTeamSize = random.randint(1, 2)
    elif(heroParty.getLevel() < 10):
        enemyTeamSize = random.randint(1, heroParty.getSize())
    else:
        enemyTeamSize = int(random(1, heroParty.getSize() * 1.5))
    enemyTeam = enemyModule.randomEnemyTeam(enemyTeamSize, heroParty.getLevel())
    return enemyTeam
    

def battle(heroParty, enemyTeam):
    print("The party enters a battle with", len(enemyTeam), "enemies!")#dialogue
    print("Enemy Team:", end=" ")#print test
    for member in enemyTeam:
        print(member.getName(), end=" ")
    print()#line break
    print("Average Enemy Level:", enemyModule.averageEnemyLevel(enemyTeam))#dialogue
    print("Average Hero Level :", heroParty.getLevel()) #dialogue compares enemy and hero team 
    print()#line break #end intro
    partyDamageDealt = 0
    enemyDamageDealt = 0
    spentMembers = []#holds int values of indices of actors who are dead or who have moved
    while(heroParty.isAlive() and enemyModule.isAlive(enemyTeam)):
        #gather actors who are alive
        actors = [] #declare actors as an empty list
        for member in heroParty.getMembers():
            if(member.getHP() > 0 and not member.getIncap()):
                actors.append(member)       
        for member in enemyTeam:
            if(member.getHP() > 0 and not member.getIncap()):
                actors.append(member)
        actors = utility.sortByBattleSpeed(actors)
                
        for actor in actors:
            if(not heroParty.isAlive() or not enemyModule.isAlive(enemyTeam)):#if either party dead
                break
            if(actor.getHP() < 1 or actor.getIncap()):
                continue #if no hp, do nothing; skip actor's turn due to death or paralysis
                
            defendingTeam = getDefendingTeam(actor, heroParty.getMembers(), enemyTeam)
            dfdr = getDefender(defendingTeam)#determine who's getting hit
            if(not dfdr or dfdr.getHP() < 1):
                print("NO DEFENDER EXIT")#print test
                time.sleep(3)#print test
                break
            damageDealt = int(actor.attack(dfdr))#Get damage from attack formula and
            dfdr.damageHP(damageDealt)#hand over damage to be taken
            actor.showHP()
            dfdr.showHP()
            print()#line break
            if(dfdr.getHP() < 1 or dfdr.getIncap()):
                dfdr.fallInBattle()            
            #tally damage
            if(actor.getHero() == heroParty.getMembers()[0].getHero()):
                partyDamageDealt += damageDealt
            else:
                enemyDamageDealt += damageDealt

    if(heroParty.isAlive() and enemyModule.isAlive(enemyTeam)):
        print("ERROR! BATTLE IS OVER; NEITHER PARTY IS DEAD")#print test
        exit(1)
        
    #rewards        
    if(heroParty.isAlive()):
        print("\nThe battle is over, and the dust settles to the ground...")#dialogue
        print("partyDamageDealt:", partyDamageDealt, "\tenemyDamageDealt:", enemyDamageDealt)
        heroParty.earnMoney(random.randint(25, 100))
        heroParty.showFallenMembers()
        heroParty.divideEXP(enemyModule.rewardEXP(enemyTeam))
        return True
    else:#GAME OVER, PROBS
        print("Blood and gore stretch over the spot where a few brave souls made their last stand.")
        print()#line break
        return False

def determineAttack(atkr, dfndr, move): # finds the move and calls damage
    if move["Kind"].lower() == 'atk': # move Kind is an attack
        damage(atkr, dfndr, move) # run damage function
    elif move["Kind"].lower() == 'heal': #move Kind is a restore move
        heal(atkr, move) # run heal function
    elif move["Kind"].lower() == 'magic':
        magic(atkr, dfndr, move)

def getDefendingTeam(atkr, heroTeam, enemyTeam): #teams are lists
    #print("getDefendingTeam:")
    defendingTeam = None
    #print("atkr.getHero():", atkr.getHero(), "heroTeam[0].getHero():", heroTeam[0].getHero())
    if(atkr.getHero() == heroTeam[0].getHero()):
        defendingTeam = enemyTeam
    else:
        defendingTeam = heroTeam
    #print("defendingTeam.getHero():", defendingTeam[0].getHero())
    return defendingTeam
    

def getDefender(team):#returns Character object
    #print("len(team):", len(team)) #print test
    if(len(team) > 1):
        dfdr = team[random.randint(0, len(team) - 1)]
        if(dfdr.getHP() > 0 and not dfdr.getIncap()):
            return dfdr
        else:
            team.remove(dfdr)
            return getDefender(team)
    else:
        return team[0]
            

