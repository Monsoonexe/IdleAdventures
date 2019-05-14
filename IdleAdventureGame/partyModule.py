#partyModule
import characterClass
import itemModule
import random

class Party():
    def __init__(self):
        self.__deadMembers = []
        self.__members = []#list of characters
        self.__money = 100
        self.__passiveRegenRate = .5
        
        self.initParty(3)#start with 3 members

    def addMember(self, level):
        newChar = characterClass.Character(self.genRandomName(), level)
        newChar.setHero(True)
        self.__members.append(newChar)
        self.__money += random.randint(0, int(self.getLevel() * 10))

    def divideEXP(self, amount):
        for member in self.__members:
            if(member.getHP() > 0 and not member.getIncap()):
                member.gainEXP(amount)
        #every party member gets full amount of EXP

    def earnMoney(self, amount):
        self.__money += amount

    def getWalkingSpeed(self):
        #walking speed is the lowest speed out of all party members
        woundedParty = False #lowers party move speed if true
        #print("size of members:", len(self.__members))#print test
        slowestWalkingSpeed = self.__members[0].getWalkingSpeed()
        for member in self.__members:
            if(member.getWalkingSpeed() < slowestWalkingSpeed):
                slowestWalkingSpeed = member.getWalkingSpeed()
            if(member.getHP() < 0):
                woundedParty = True
        if(woundedParty): #halves speed
            slowestWalkingSpeed /= 2
        return slowestWalkingSpeed

    def genRandomName(self):
        nameList = ["Arpa", "Bang", "Chinko", "Cloud", "Dinz", "Eckor", "Fin-Ram",
                    "Gine", "Haytham", "Iris", "Jorg", "Kanter", "Lorg", "MegaMan",
                    "Mopp", "Mynn", "Nocxious", "Pinka", "Rake",  "Shann", "Zack", "Zingk"]
        nameIsTaken = True
        name = "NullMan"
        while(nameIsTaken):
            name =  nameList[random.randint(0, len(nameList)-1)]
            if(name not in self.__members or name  not in self.__deadMembers):
                nameIsTaken = False
        return name

    def getLevel(self):#returns average party member level
        totalLevel = 0 #accumulator for each party member's level
        #levelAverage = 0 #and the average thereof
        for member in self.__members:
            totalLevel += member.getLevel()
        return int(totalLevel / ( 1 if len(self.__members) <= 1 else len(self.__members)))

    def getMoney(self):
        return self.__money

    def getMembers(self):
        return self.__members

    def getPassiveRegenRate(self):
        return self.__passiveRegenRate

    def getSize(self):
        return len(self.__members)

    def HPLow(self):
        lowHP = False #false until true
        totalMaxHP = 0
        totalCurrentHP = 0

        for member in self.__members:
            totalMaxHP += member.getMaxHP()
            totalCurrentHP += member.getHP()
            if(member.getHP() / member.getMaxHP() < 1/5 or member.getIncap()): #if lower than 1/5th max
                lowHP = True               
        
        #if average party hp percent is below 50%
        #or if any 1 member is below 1/5th max hp flag True
        #or if any 1 member HP = 0 or incapped
        if(totalCurrentHP / totalMaxHP > 1/2):
            lowHP = True

        return lowHP #boolean
        

    def initParty(self, initialSize):
        for member in range(0, initialSize):
            self.addMember(3)#starting level 3 now

    def isAlive(self):
        for member in self.__members:
            if(member.getHP() > 0):
                return True
        return False

    def lowestMemberHP(self):
        lowestHP = self.__members[0].getHP()
        for member in self.__members:
            if(member.getHP() < lowestHP):
                lowestHP = member.getHP()
        return lowestHP

    def passiveRegen(self):
        #print("The party heals slightly over time.") #print test
        for member in self.__members:
            member.passiveRegen(self.__passiveRegenRate)

    def rest(self):
        for member in self.__members:
            member.fullRevive()

    def setPassiveRegenRate(self, newRate):
        self.__passiveRegenRate = newRate

    def showFallenMembers(self):
        incappedMembers = []
        for member in self.__members:
            if(member.getHP() < 1 or member.getIncap()):
                incappedMembers.append(member.getName())                   
        if(len(incappedMembers) > 0):
            for name in incappedMembers:
                print(name, end=" ")
            print("fell during battle.")

    def showPartyStats(self):
        for member in self.__members:
            member.showStats()
            print()#line break

    def spendMoney(self, amount):
        self.__money = 0 if self.__money - amount < 0 else self.__money - amount

    def showNames(self):
        for member in self__members:
            print(member.getName(), end=" ")
        print()#line break





        
