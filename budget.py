from unittest.runner import TextTestRunner

class Category:
    
    def __init__(self, categName):
        self.ledger = []
        self.balance = 0.0
        self.categoryName = categName

    def deposit(self, amount, description = ""):
        
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, categName):
        
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+ categName.categoryName)
            categName.deposit(amount, "Transfer from " + self.categoryName)
            return True
        return False

    def check_funds(self, amount):
       
        if self.balance >= amount:
            return True
        return False

    def __str__(self):
        info = "*"*((30-len(self.categoryName))//2)+self.categoryName+"*"*((30-len(self.categoryName))//2)+"\n"
        for _ in self.ledger:
            info += _["description"][:23] + " "*(23 - len(_["description"][:23])) + " "*(7 - len("{:.2f}".format(_["amount"]))) + "{:.2f}".format(_["amount"])+"\n"
        info += "Total: {:.2f}".format(self.balance)
        return info


def create_spend_chart(categories):
    expenditureDict = {}
    for categs in categories:
        sumAll = 0 
        for _ in categs.ledger:
            if _['amount'] < 0 :
                sumAll += abs(_['amount'])
        expenditureDict[categs.categoryName] = round(sumAll,2)
    total = sum(expenditureDict.values())
    percentageSpent = {}
    for key in expenditureDict.keys():
        percentageSpent[key] = int(round(expenditureDict[key]/total,2)*100)
    output = 'Percentage spent by category\n'
    for i in range(100,-10,-10):
        output += f'{i}'.rjust(3) + '| '
        for percent in percentageSpent.values():
            if percent >= i:
                output += 'o  '
            else:
                output += '   '
        output += '\n' 
    output += ' '*4+'-'*(len(percentageSpent.values())*3+1)
    output += '\n     '
    keyList = list(percentageSpent.keys())
    max_len_category = max([len(i) for i in keyList])
    
    for i in range(max_len_category):    
        for categoryName in keyList:
            if len(categoryName)>i:
                output += categoryName[i] + '  '
            else:
                output += '   '
        if i < max_len_category-1:
            output += '\n     '
        
    return output