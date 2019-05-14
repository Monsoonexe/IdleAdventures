#characterClass.py
#bitches love characters!
import battleModule
import equipmentModule
import math
from playerBackpack import *
import random
from SPECIALmodule import *

EXPRequired = [1, 5, 10, 20, 30, 50, 75, 100, 150, 200, 300, 500, 750, 1000, 1250,
               1555, 1750, 2000]

class Character():
    def __init__(self, name, level):
        self.__dead = False #HP went WWAAAYYY beyond 0 and is now out for good
        self.__hero = False #distinguishes false for enemy, true for hero
        self.__incap = False #incapacitated or not, probs HP <= 0, or paralyzed, or scared, etc
        self.__name = "DerpFace BucketHead"
        self.__level = 1
        self.__EXP = 1

        self.setName(name)
        self.setLevel(level)#set starting level
        self.setEXP(calculateEXP(level))#set EXP starting point based on starting level

        #Special stats

        self.__strength = 1
        self.__perception = 1
        self.__endurance = 1
        self.__charisma = 1
        self.__intelligence = 1
        self.__agility = 1
        self.__luck = 1        

        #randomized base stats
        
        self.__baseBattleSpeed = random.randint(5, 8)
        self.__baseHPRegenRate = random.randint(0, 3)
        self.__baseMPRegenRate = random.randint(0, 3)
        self.__baseWalkingSpeed = random.randint(1, 3) + 10

        #stats to be derived from base stats
        #will be filled in when renderStats() is called
        self.__attack = 0
        self.__accuracy = 0
        self.__battleSpeed = 0
        self.__defense = 0
        self.__evasion = 0        
        self.__hpRegenRate = 0
        self.__maxHP = 0
        self.__magic = 0
        self.__maxMP = 0
        self.__mpRegenRate = 0
        self.__walkingSpeed = 0
        
        #equipment and gear slots
        self.__primary = equipmentModule.Equipment("none", "PRIMARY", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.__secondary = equipmentModule.Equipment("none", "SECONDARY", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.__headgear = equipmentModule.Equipment("none", "HEADGEAR", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.__footgear = equipmentModule.Equipment("none", "FOOTGEAR", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.__body = equipmentModule.Equipment("none", "BODY", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.__shoulders = equipmentModule.Equipment("none", "SHOULDERS", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.__legs = equipmentModule.Equipment("none", "LEGS", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        #for easy list processing
        self.__gearList = []
        
        # self.__rings = [] #TODO
        self.__backpack = Backpack()
        self.__statusEffects = []
        
        #render stats derived from base stats
        self.renderStats()#RENDER STATS!!!!!
        self.__HP = self.__maxHP
        self.__MP = self.__maxMP

    def allocateSpecialPoint(self):
        #this function can become more sophisticated -- adding points "smarter"
        #random for now
        statUp = random.randint(0, len(SPECIAL) - 1) #random SPECIAL STAT
        if(statUp == SPECIAL.STRENGTH):
            self.__strength += 1
        elif(statUp == SPECIAL.PERCEPTION):
            self.__perception += 1
        elif(statUp == SPECIAL.ENDURANCE):
            self.__endurance += 1
        elif(statUp == SPECIAL.CHARISMA):
            self.__charisma += 1
        elif(statUp == SPECIAL.INTELLIGENCE):
            self.__intelligence += 1
        elif(statUp == SPECIAL.AGILITY):
            self.__agility += 1
        elif(statUp == SPECIAL.LUCK):
            self.__luck += 1
        #renderStats() not used due to this func called in self.levelUp()
            
    def attack(self, dfdr):#friends and foes TODO
        #choose what kind of attack, normal, magic, item, etc
        #determineAttack
        attackChoice = self.determineAttack(dfdr)
        if(attackChoice < 500):#TODO list different attacks and %
            return self.basicAttack(dfdr)

    def basicAttack(self, dfdr): #effect)
        print("*" if self.getHero() else " ", end='')
        print(self.__name, "attacks", dfdr.getName(), end='') #dialogue
        dmg = 0 #damage done to defender
        
        #resolve miss
        attackRoll = random.randint(0, 100)
        ## accuracy check with 1/20 chance of miss
        if (attackRoll + self.__accuracy <= dfdr.getEvasion() + 5):#defender dodges attack!
            dmg = 0# no damage
            print(dfdr.getName(), "blocks the attack!")
        else:#attack hits!                
            #resolve crit 5% chance of dealing 1.525% damage
            critPower = 1.525 if(attackRoll >= 95 - 1.75 * math.sqrt(self.getLuck() * 10)) else 1 #change to do critical hit -- fun equation
               
            mod = (random.randint(85, 100)) / 100 #damage modifier between 85%-100%
            dmg = 1 + int((((self.getAttack() / float(dfdr.getDefense())) * 2) * critPower) * mod)#damage equation
            print(" and deals", dmg, "damage!") # show damage                   
        return dmg #damage calculated
    
    def calcGearAccuracyBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getAccuracyBonus()
        return bonus

    def calcGearAttackBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getAttackBonus()
        return bonus
    
    def calcGearBattleSpeedBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getBattleSpeedBonus()
        return bonus
    
    def calcGearDefenseBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getDefenseBonus()
        return bonus

    def calcGearEvasionBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getEvasionBonus()
        return bonus

    def calcGearHPBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getHPBonus()
        return bonus

    def calcGearHPRegenBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getHPRegenBonus()
        return bonus

    def calcGearMagicBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getMagicBonus()
        return bonus

    def calcGearMPBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getMPBonus()
        return bonus

    def calcGearMPRegenBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getMPRegenBonus()
        return bonus

    def calcGearWalkingSpeedBonus(self):
        bonus = 0 #accumulator
        for gear in self.__gearList:
            bonus += gear.getWalkingSpeedBonus()
        return bonus

    def damageHP(self, damageAmount):
        self.__HP -= int(damageAmount) #update defender's current HP
        if(self.__HP < 0):
            self.__HP = 0
        
        #self.__incap = True

    def determineAttack(self, dfdr):
        #TODO determines best move based on paramteters (unfinished)
        #friends foes, their HP and statsus ailments
        return random.randint(0, 99)

    def equipBody(self, item):
        if(item.slotType == "BODY"):
            self.__body = item
            self.renderStats()
        else:
            print("ERROR! INCORRECT EQUIPPING!")

    def equipFootgear(self, item):
        if(item.slotType == "FOOTGEAR"):
            self.__footgear = item
            self.renderStats()
        else:
            print("ERROR! INCORRECT EQUIPPING!")

    def equipHeadgear(self, item):
        if(item.slotType == "HEADGEAR"):
            self.__headgear = item
            self.renderStats()
        else:
            print("ERROR! INCORRECT EQUIPPING!")
    
    def equipLegs(self, item):
        if(item.slotType == "LEGS"):
            self.__legs = item
            self.renderStats()
        else:
            print("ERROR! INCORRECT EQUIPPING!")

    def equipPrimary(self, item):
        if(item.slotType == "PRIMARY"):
            self.__primary = item
            self.renderStats()
        else:
            print("ERROR! INCORRECT EQUIPPING!")

    def equipSecondary(self, item):
        if(item.slotType == "SECONDARY"):
            self.__secondary = item
            self.renderStats()
        else:
            print("ERROR! INCORRECT EQUIPPING!")

    def equipShoulders(self, item):
        if(item.slotType == "SHOULDERS"):
            self.__shoulders = item
            self.renderStats()
        else:
            print("ERROR! INCORRECT EQUIPPING!")

    def fallInBattle(self):
        print("!!!!"+self.__name, "is defeated!!!!!")

    def fullRevive(self):
        self.healHP("full")
        self.healMP("full")
        self.__incap = False

    def gainEXP(self, amount):
        amount = int(amount)
        print(self.__name, "earns", amount, "EXP!")
        self.__EXP += amount
        while(checkLevel(self.__level, self.__EXP)):
            self.levelUp()
            print(self.__name, "reached Level", str(self.__level) + "!")

    #fetchers
    def getAttack(self):
        return int(self.__attack)
    def getAccuracy(self):
        return int(self.__accuracy)
    def getBattleSpeed(self):
        return int(self.__battleSpeed)
    def getDefense(self):
        return int(self.__defense)
    def getEvasion(self):
        return int(self.__evasion)
    def getFriendly(self):
        return bool(self.__hero)
    def getWalkingSpeed(self):
        return int(self.__walkingSpeed)
    def getHP(self):
        return int(self.__HP)
    def getHero(self):
        return bool(self.__hero)
    def getIncap(self):
        return int(self.__incap)
    def getMaxHP(self):
        return int(self.__maxHP)
    def getLevel(self):
        return int(self.__level)
    def getMP(self):
        return int(self.__MP)
    def getMaxMP(self):
        return int(self.__maxMP)
    def getMagic(self):
        return int(self.__magic)
    def getName(self):
        return str(self.__name)

    #SPECIAL GETTERS

    def getStrength(self):
        return self.__strength
    def getPerception(self):
        return self.__perception
    def getEndurance(self):
        return self.__endurance
    def getCharisma(self):
        return self.__charisma
    def getIntelligence(self):
        return self.__intelligence
    def getAgility(self):
        return self.__agility
    def getLuck(self):
        return self.__luck
    

    def healHP(self, healAmount):
        #determine heal amount
        if(healAmount in ["full", "max", "all"]):
            self.__HP = self.__maxHP
        else:
            self.__HP += int(healAmount) #add health to hp
        self.__HP = self.__maxHP if self.__HP > self.__maxHP else self.__HP           
                
    def healMP(self, healAmount):
        #determine heal amount
        if(healAmount in ["full", "max", "all"]):
            self.__MP = self.__maxMP
        else: 
            self.__MP += int(healAmount) #add health to hp
        self.__MP = self.__maxMP if self.__MP > self.__maxMP else self.__MP

    def isAlive(self):
        True if self.__HP > 0 else False

    def levelUp(self):
        self.__level += 1
        self.allocateSpecialPoint()
        self.renderStats()

    def passiveRegen(self, modifier):
        if(self.__HP > 0 and not self.__incap):#only regen if not KO            
            self.healHP(modifier * self.__HPRegenRate)
            self.healMP(modifier * self.__HPRegenRate)

    def randomizeSpecial(self):
        print("initializingSpecial().....")#print test
        int_statPoints = 7 # seems like a good starting stat number
        str_statUp = " " #init        
        while int_statPoints > 0 :
            str_statUp = random.choice("s", "p", "e", "c", "i", "a", "l") # 
            if(str_statUp == "s"):
                self.__strength += 1
            elif(str_statUp == "p"):
                self.__perception += 1
            elif(str_statUp == "e"):
                self.__endurance += 1
            elif(str_statUp == "c"):
                self.__charisma += 1
            elif(str_statUp == "i"):
                self.__intelligence += 1
            elif(str_statUp == "a"):
                self.__agility += 1
            elif(str_statUp == "l"):
                self.__luck +=1

            statPoints -= 1 # subtract used point

        self.renderStats() #always render your stats after a change!

    def renderStats(self):
        #MUST BE RAN AFTER LEVELLING
        #prolly should be ran after any stat mods.  i forget.

        #create gearList to make more easily processed
        self.__gearList = [self.__body, self.__footgear, self.__headgear, self.__legs,
            self.__primary, self.__secondary, self.__shoulders]

        #calculate each stat point
        self.__accuracy = int(math.sqrt(self.__level * self.__perception) + self.calcGearAccuracyBonus())
        self.__attack = int(math.sqrt(self.__level * self.__strength) + self.calcGearAttackBonus())
        
        self.__battleSpeed = int((((self.__baseBattleSpeed + self.calcGearBattleSpeedBonus()) *
                                   2) * self.__level) / 100 + self.__level + 5)
        
        self.__defense = int(math.sqrt(self.__level * (self.__endurance + self.__strength)) + self.calcGearDefenseBonus())

        self.__evasion = int(math.sqrt(self.__level * (self.__perception + self.__agility + (self.__luck / 2))  +
                             self.__battleSpeed) / 13)

        self.__hpRegenRate = int(math.sqrt(self.__level * (self.__baseHPRegenRate + self.__endurance)) + 
                                self.calcGearHPRegenBonus())
        
        self.__magic = int(math.sqrt(self.__level * (self.__perception + self.__intelligence) + self.calcGearMagicBonus()))
        
        self.__maxHP = int(self.__level + math.sqrt(self.__level * (self.__strength * 5) + (self.__endurance * 10)) + self.calcGearHPBonus())
        
        self.__maxMP = int(self.__level + math.sqrt(self.__level * (self.__perception * 5) + (self.__intelligence * 10)) + self.calcGearMPBonus())

        self.__mpRegenRate = int(self.__baseMPRegenRate + self.calcGearMPRegenBonus())

        self.__walkingSpeed = int(self.__baseWalkingSpeed + self.calcGearWalkingSpeedBonus())
                
       #mutators 
    def setName(self, newName):
        self.__name = str(newName)
    def setAttack(self, amount):
        self.__baseAttack = int(amount)
    def setBattleSpeed(self, amount):
        self.__battleSpeed = amount
    def setDefense(self, amount):
        self.__defense = amount
    def setEXP(self, amount):
        self.__EXP = int(amount)
    def setHero(self, friendOrFoe):
        if(type(friendOrFoe) == bool):#input validation check
            self.__hero = friendOrFoe #normal behavior
        else:
            print("ERROR:  FRIENDORFOE not boolean value!!!")
            print("TERMINATING....")
            exit(1)
    def setLevel(self, level):
        level = int(level)
        self.__level = 1 if level < 1 else level
        self.__EXP = EXPRequired[level]

    def setMaxHP(self, amount):
        self.__MaxHP = int(amount)
    def setMaxMP(self, amount):
        self.__MaxMP = int(amount)
    def setWalkingSpeed(self, amount):
        self.__walkingSpeed = int(amount)

    def showHP(self):
        print(self.__name, "HP:", self.__HP, "/", self.__maxHP, end=" ")

    def showMP(self):
        print("MP:", self.__MP, "/", self.__maxMP, end=" ")
    
    def showStats(self):
        print()
        self.showHP()
        self.showMP()
        print()
        print("attack:\t" + str(self.__attack),
        "accuracy:\t" + str(self.__accuracy),
        "battleSpeed:\t" + str(self.__battleSpeed),
        "defense:\t" + str(self.__defense),
        "evasion:\t" + str(self.__evasion),
        "hpRegen:\t" + str(self.__hpRegenRate),
        "magic:\t" + str(self.__magic),
        "MP Regen:\t" + str(self.__mpRegenRate),
        "walking speed:\t" + str(self.__walkingSpeed))

    def useMP(self, amount):
        self.__mp -= int(amount)
        if (self.__MP <= 0):
            self.__MP = 0
            print("ERROR!! TOO MUCH MP SPENT ON SPELL")#error message

def calculateEXP(level):
    return EXPRequired[level]

def checkLevel(charLevel, charEXP):
    if(charEXP >= EXPRequired[charLevel + 1]):
        return True
    return False




                
                
            
            
    
    

    
