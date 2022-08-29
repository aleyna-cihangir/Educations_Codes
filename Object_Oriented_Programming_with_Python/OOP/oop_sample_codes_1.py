#%%   ENCAPSULATION :

class BankAccount(object):
    def __init__(self, name, money, address):
        self.name = name
        self.__money = money       # '__xyz' is private
        self.address = address
            
        def getMoney(self):
            return self.__money
            
        def setMoney(self, amount):
           self.__money = amount
           
        def  __increase(self):
            self.__money = self.__money + 500
#%%
p1 = BankAccount('x', 1000, 'Y')
p2 = BankAccount('M', 3000, 'N')  
#p2.money = p2.money + p1. money  # result = 4000
#%%

print(p1.getMoney())
p1.setMoney(5000)
print(p1.getMoney())

#%%
p1.__increase()
print(p1.getMoney())

#%%

class Animal:
    def __init__(self):
        print("animal is created")
    
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")
    
#%% child

class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init of parent(animal) class
        print("monkey is created")
    
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")
#%%

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    
    def fly(self):
        print("fly") 
#%%

m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()
print("----")
b1 = Bird()
b1.walk()
# b1.climb()
b1.fly()   

#%%

