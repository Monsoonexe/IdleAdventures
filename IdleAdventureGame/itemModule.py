#item module

from random import *

def itemDictionary():
    #create individual items
    
    blowtorch =  {"Name" : "blowtorch", \
                  "Kind" : "restore",\
                  "Pwr" : 50,\
                  "Price" : 600}

    defense_upgrade = {"Name" : "Defense Upgrade",\
                       "Kind" : "upgrade",\
                       "Type" : "defense",\
                       "Pwr" : 1.08,\
                       "Price" : "1000"}
    
    firmware_upgrade = {"Name" : "Firmware Upgrade",\
                        "Kind" : "upgrade",\
                        "Type" : "MAXHP",\
                        "Pwr" : 1.1,\
                        "Price" : "1000"}

    grenade = {"Name" : "Grenade", \
               "Kind" : "damage",\
               "Pwr" : 35,\
               "Price" : 475}

    power_upgrade = {"Name" : "Power Upgrade",\
                     "Kind" : "upgrade",\
                     "Type" : "attack",\
                     "Pwr" : 1.08,\
                     "Price" : "1000"}
    potion = {"Name" : "Potion", \
              "Kind" : "restore",\
              "Pwr" : 25,\
              "Price" : 500}
    
    uber_potion = {"Name" : "Uber Potion", \
                   "Kind" : "restore",\
                   "Pwr" : 150,\
                   "Price" : 2000}
    
    wrench = {"Name" : "Wrench", \
              "Kind" : "restore",\
              "Pwr" : 20,\
              "Price" : 250}
    

    #include all items in this dictionary
    itemDic = {"wrench" : wrench,\
               "blowtorch" : blowtorch,\
               "potion" : potion,\
               "uber_potion" : uber_potion,\
               "grenade" : grenade,\
               "firmware_upgrade" : firmware_upgrade,\
               "power_upgrade" : power_upgrade,\
               "defense_upgrade" : defense_upgrade}
    
    return itemDic

def useItem(itemDic, backpack):
    print("Choose an ITEM to use or type 'cancel' to return.")
    itemsTuple = getItemsTuple() #make items a tuple for easier search
    playerIsViewingBackpack = 'TRUE' #set pretest for while loop
    while playerIsViewingBackpack:
        print("***BACKPACK***") #dialogue
        print("Item in Backpack:", backpack.getNumItems) #number of items in back
        count = 1 #line counter
        for key in backpack.getItems():
            print(count, "---", key["Name"])
            count += 1
        print("---------------")
        print("To find out more about an item, type in item name now.")
        print("Type 'n' to continue on.")
        action = input(">>>")
        if action == 'n':
            playerIsViewingBackpack = 'FALSE'
        else:            
            if action in self.__backpack:
                print('\n', self.__backpack[action]["Description"])
            else:
                print("Type either a valid item or 'n'")   

def activateItem(item, atkr, dfndr):
    if item["Kind"] == "restore":
        restoreItem(item, atkr)
    elif item["Kind"] == "damage":
        damageItem(item, atkr, dfndr)
    elif item["Kind"] == "upgrade":
        upgradeItem(item, atkr)
        
def getItemsTuple(items):
    itemsTuple = ()
    for key in items:
        itemsTuple.append(key["Name"])
    return itemsTuple.sort #make alphabetical

def aOrAn(name):
    name = tuple(name.lower())
    if name[0] in ("a", "e", "i", "o", "u"):
        return "an"
    else:
        return "a"

def restoreItem(item, user):
    print(user.getName(), "used", aOrAn(item["Name"]), item["Name"]) #dialogue

def damageItem(item, user, dfndr):
    print(user.getName(), "used", aOrAn(item["Name"]), item["Name"]) #dialogue

def upgradeItem(item, user):
    print(user.getName(), "used", aOrAn(item["Name"]), item["Name"]) #dialogue
    if item["Type"] == "attack":
        statChange = item["Pwr"] * int(user.getAttack)
        user.setAttack(statChange)
        print(str(user.getName) + "'s " + str(item["Type"]) + "raised to " + \
              str(user.getAttack) + "!")
    elif item["Type"] == "defense":
        statChange = item["Pwr"] * int(user.getDefense)
        user.setDefense(statChange)
        print(str(user.getName) + "'s " + str(item["Type"]) + "raised to " + \
            str(user.getDefense) + "!")
    elif item["Type"] == "MAXHP":
        statChange = item["Pwr"] * int(user.getAttack)
        print(str(user.getName) + "'s " + str(item["Type"]) + "raised to " + \
              str(user.getMAXHP) + "!")        
        user.setAttack(statChange)
    
#####test functions
##itemDic = itemDictionary()
##activateItem(itemDic["grenade"])
