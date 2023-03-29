class Category:
    name = ''
    def __init__(self, x):
        self.name = x
        self.balance = 0.0
        self.ledger = list() #list() or [] are the same ..ledger means expenditures المصروفات
    def get_balance(self):
        return self.balance
    def deposit(self, amount, description):
        self.ledger.append({'amount':amount,'description':description})
        self.balance =self.balance + float(amount)
    def transfer(self, amount, cat):
        if self.check_funds(amount) == False:
            print('you don\'t have enough money')
            return False
        else:
            self.withdraw(amount, ('transfer to '+ cat.name))
            cat.deposit(amount,('transfer from ' + self.name))
            return True
    def withdraw(self, amount, description):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({'amount':(0-amount),'description':description})
            self.balance =self.balance - float(amount)
            return True
    def check_funds(self, amount):
        if float(amount) > self.balance:
            return False
        else:
            return True
    def __str__(self):
        displayer = ''
        fline = self.name
        fline = fline.center(30,'*')
        displayer = displayer + fline + '\n'
        for items in self.ledger:
            item = list(items.values()) #list() instead of [] ...i'm putting every value in a list
            print(item)
            spart = item[0]
            fpart = item[1]
            fpart = fpart[:21]
            displayer = displayer + fpart + str(spart) + '\n'
        displayer = displayer + 'Total' + str(self.balance)
        return displayer
food = Category('food')
food.deposit(1000,'initial deposit')    
food.withdraw(10.15,'supermarket')
print(food.get_balance())
cloth = Category('cloth')
food.transfer(50,cloth)
print(food)
cloth.withdraw(25.55,'day1')
cloth.withdraw(15,'day2')
print(food)
print(cloth)