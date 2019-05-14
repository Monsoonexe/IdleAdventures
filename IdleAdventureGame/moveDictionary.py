#moveDictionary

def moveDictionary():
    basicAtk =      {"Name" : "Basic Attack", \
                     "Kind" : "atk",\
                     "Pwr" : 25, \
                     "Acc" : 95, \
                     "Crit" : 80, \
                     "Txt" : "attacks!"}
                     #special                 
    heal =          {"Name" : "Heal", \
                     "Kind" : "heal",\
                     "Pwr" : 34, \
                     "Acc" : 25, \
                     "Crit" : 5, \
                     "Txt" : "attempts to put itself back together"}
    robot_punch =   {"Name" : "Robot Punch", \
                     "Kind" : "atk",\
                     "Pwr" : 35, \
                     "Acc" : 67, \
                     "Crit" : 20, \
                     "Txt" : "reels back and slugs hard"}
    robot_slap =    {"Name" : "Robot Slap", \
                     "Kind" : "atk",\
                     "Pwr" : 27, \
                     "Acc" : 90, \
                     "Crit" : 20, \
                     "Txt" : "slaps a hoe"}
    robot_headbutt = {"Name" : "Robot Headbutt", \
                     "Kind" : "atk",\
                     "Pwr" : 45, \
                     "Acc" : 20, \
                     "Crit" : 80, \
                     "Txt" : "attempts a powerful attack"}
                        #special
    
    moveDic = {"basicAtk" : basicAtk,\
               "heal" : heal, \
               "robot punch" : robot_punch,\
               "robot slap" : robot_slap,\
               "robot headbutt" : robot_headbutt}
    
    return moveDic

##dictionary = moveDictionary() #module testing
##print(type(dictionary)) #module print test
