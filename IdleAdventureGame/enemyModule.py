#enemyModule

import characterClass
import math
import random
import partyModule

class Enemy(characterClass.Character):
    def __init__(self, name, level, baseEXPYield, baseCommonYield, baseScarceYield, baseRareYield):
        characterClass.Character.__init__(self, name, level) 
        self.__baseEXPYield = baseEXPYield
        self.__baseCommonYield = baseCommonYield
        self.__baseScarceYield = baseScarceYield
        self.__baseRareYield = baseRareYield
        self.setHero(False)

    def yieldEXP(self): #returns an int
        return int(math.sqrt(self.__baseEXPYield * self.getLevel()))
    def yieldCommon(self):#returns rate at which drop occurs
        return math.sqrt(self.__baseCommonYield * self.getLevel())
    def yieldScarce(self):
        return math.sqrt(self.__baseScarceYield * self.getLevel())
    def yieldRare(self):
        return math.sqrt(self.__baseScareYield * self.getLevel())

    #check that yieldEXP is yielding whole numbers and all is being distributed
    
class Mettuar(Enemy):
    def __init__(self, level):
        # self, name, lvl, exp, common, scarce, rare
        Enemy.__init__(self,
                       "Mettuar",#name
                       random.randint(level-5, level-1), # level
                       9,# base EXP Yield
                       5, #base CommonYield
                       1,#baseScarceYield
                       0) #base Rare Yield

class SniperJoe(Enemy):
    def __init__(self, level):
        Enemy.__init__(self, "SniperJoe", random.randint(level-3, level), 12, 6, 3, 1)      

class KernalKiller(Enemy):
    def __init__(self, level):
        Enemy.__init__(self, "Kernal Killer", random.randint(level-1, level+1), 17, 8, 5, 2) 

class FaceKicker(Enemy):
    def __init__(self, level):
        Enemy.__init__(self, "FaceKicker", random.randint(level, level+3), 26, 13, 8, 2) 

def assignEnemyNo(enemy, party):
    similarEnemyCount = 1# does not count self #starts at one so second enemy generated will be Dude2 and so forth
    for member in party:
        if(enemy.getName()[0 : 5] == member.getName()[0 : 5]):#if first 5 letters of each string identical
            similarEnemyCount += 1
    enemy.setName(enemy.getName() + " " + str(similarEnemyCount))

def averageEnemyLevel(enemyTeam):
    levelTotal = 0
    for member in enemyTeam:
        levelTotal += member.getLevel()
    return int(levelTotal / len(enemyTeam))

def encounterCheck(partyLevel):
    baseEncounterRate = 25
    if(random.randint(0, 100) < baseEncounterRate + partyLevel):
        print("Some enemies are approaching!")
        return True
    else:
        return False

def isAlive(enemyTeam):
    for member in enemyTeam:
        if(member.getHP() > 0 and not member.getIncap()):
            return True
    return False

def randomEnemyTeam(teamSize, level):
    #print("building enemy team...")
    party = []
    memberCount = 1
    enemyLevel = 5#TODO for now!
    while(memberCount <= teamSize):
        enemy = randomEnemy(enemyLevel)# get a randomly generated baddie
        assignEnemyNo(enemy, party)# Mettuar 2, SniperJoe 4
        party.append(enemy)#add to list of enemies
        memberCount += 1#increment counter
    return party#return fully made party of baddies

def randomEnemy(level):
    #print("building single enemy at a time")
    choice = random.randint(0, 10)
    if(choice == 0):
        return FaceKicker(level)
    elif(choice < 5):
        return Mettuar(level)
    elif(choice < 7):
        return KernalKiller(level)
    else:
        return SniperJoe(level)

def rewardEXP(enemyTeam):
    totalEXP = 0
    for enemy in enemyTeam:
       totalEXP += enemy.yieldEXP() #EXP reward
    print("rewardEXP() totalEXP:", totalEXP)#Print test
    return totalEXP

def rewardItem(enemyTeam):
    #TODO reward items
    for enemy in enemyTeam:
        #item rewards
        if(random.randint(0, 100) < enemy.yieldCommon()):
           pass #return commonLootList[random.randint(0, 100)]
        elif(random.randint(0, 100) < enemy.yieldScarce()):
            pass #return scarceLootList[random.randint(0, 100)]
        elif(random.randint(0, 100) < enemy.yieldRare()):
            pass #return rareLootList[random.randint(0, 100)]



        
    
