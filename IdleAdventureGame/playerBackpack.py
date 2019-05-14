#bitches love backpacks
class Backpack():
    def __init__(self):
        self.__numItems = 0
        self.__items = {}
        self.__size = 8
        self.__wallet = 100

    def getNumItems(self):
        return self.__numItems
    def getItems(self):
        return self.__items
    def getSize(self):
        return self.__size
    def getWallet(self):
        return self.__wallet

    def walletIncrease(self, amount):
        self.__wallet += amount
    def walletDecrease(self, amount):
        self.__wallet -= amount

    def addNumItems(self, amount):
        self.__numItems += amount
    def lessNumItems(self, amount):
        self.__numItems -= amount

    def checkFullBackpack(self):
        if self.getNumItems() >= self.getSize():
            return True
        else:
            return False
        
    def checkHasItem(self, item):
        itemName = item["Name"].lower()
        if itemName in self.__items:
            return True
        else:
            return False
            
    def addItem(self, item, amount):
        print("Var amount: ", amount) #print test
        if self.checkFullBackpack():
            print(self.checkFullBackpack()) #print test
            print("Your backpack is full!\n" +\
                  "You can't take any more items right now.")
            print("Space in Backpack: ", end = '')
            print(self.getNumItems(), "/", self.getSize())
        else:
            if (amount + self.getNumItems()) > self.getSize():
                amount = (self.getSize() - self.getNumItems())
                
            itemKey = item["Name"].lower()
##            print(item["Name"]) #print test
##            print(itemKey) #print test
            if self.checkHasItem(item):
                print(self.__items) #print test
                self.__items[itemKey]["Quant"] += amount
            else:
                itemEntry = {"Name" : item["Name"],\
                             "Quant" : amount}
                self.__items[itemKey] = itemEntry #add item to dictionary
            self.__numItems += amount #increase number of items in bag
            print("Space in Backpack: ", end = '')
            print(self.getNumItems(), "/", self.getSize())

    def removeItem(self, item, amount):
        self.__numItems -= amount #increase number of items in bag
        if self.getNumItems < 0:
            self.__numItems = 0
        itemKey = (item["Name"]).lower()
        self.getItems()[itemKey]["Quant"] -= amount
        if self.getItems()[itemKey]["Quant"] < 0:
            self.getItems()[itemKey]["Quant"] = 0
        print("Space in Backpack: ")
        print(getNumItems(), "/", getSize())

#module testing
##from itemmodule import *
##itemDic = itemDictionary()
##item = itemDic["grenade"]
##item2 = itemDic["blowtorch"]
##BACKPACK = Backpack()
##BACKPACK.addItem(item, 1)
##BACKPACK.addItem(item2, 2)

