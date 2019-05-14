#equipmentModule.py
import math

class Equipment():
    def __init__(self, name, slotType, level, acc, atk, btlSpd, dfs, evasion, hp, hpRegen,
                 magic, mp, mpRegen, walkSpd):
        self.__acc = acc
        self.__atk = atk
        self.__btlSpd = btlSpd
        self.__dfs = dfs
        self.__evasion = evasion
        self.__hp = hp
        self.__hpRegen = hpRegen
        self.__level = level
        self.__magic = magic
        self.__mp = mp
        self.__mpRegen = mpRegen
        self.__name = name
        self.__slotType = slotType
        self.__walkSpd = walkSpd

    def getAccuracyBonus(self):
        return self.__acc
    def getAttackBonus(self):
        return self.__atk
    def getBattleSpeedBonus(self):
        return self.__btlSpd
    def getDefenseBonus(self):
        return self.__dfs
    def getEvasionBonus(self):
        return self.__evasion
    def getHPBonus(self):
        return self.__hp
    def getHPRegenBonus(self):
        return self.__hpRegen
    def getLevel(self):
        return self.__level
    def getMagicBonus(self):
        return self.__magic
    def getMPBonus(self):
        return self.__mp
    def getMPRegenBonus(self):
        return self.__mpRegen
    def getName(self):
        return self.__name
    def getSlotType(self):
        return self.__slotType
    def getWalkingSpeedBonus(self):
        return self.__walkSpd

    def getValue(self):
        value = 0 #accumulator
        value += math.sqrt(self.__acc)
        value += math.sqrt(self.__atk)
        value += math.sqrt(self.__btlSpd)
        value += math.sqrt(self.__dfs)
        value += math.sqrt(self.__evasion)
        value += math.sqrt(self.__hp)
        value += math.sqrt(self.__hpRegen)
        value += self.getLevel
        value += math.sqrt(self.__magic)
        value += math.sqrt(self.__mp)
        value += math.sqrt(self.__mpRegen)
        value += math.sqrt(self.__walkSpd) / 2

        return int(value * 100)
    

    


