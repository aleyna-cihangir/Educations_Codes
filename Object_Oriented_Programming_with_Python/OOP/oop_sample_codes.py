
#%%  Create a block: 

int1 = 33
str1 = "messi"

class Employee :
    pass # without pass give us an error 

e1 = Employee()


class Footballer :
    football_club = "barcelona"
    age = 30
    

f1 = Footballer()
print(f1)        # object from Footballer
print(f1.age)    # int value 

f1.football_club = "real madrid"  # change the club name 
print(f1.football_club)  # now club name is real madrid 

#% %% 
class Square(object):
    edge = 5 # meter
    area = 0 
    
    # why self? 
    # we want to use Square artt. so write self on name of def function :
    def Area(self) :
        self.area = self.edge*self.edge
        print(self.area)

s1 = Square()
print(s1.Area())

s1.edge = 7
s1.Area()

# %%   Methods and Functions :

class Emp(object):
    
    age = 25 
    salary = 1000 
    def AgeSalaryRatio(self):
        a = self.age / self.salary
        print('Age Salary Ratio Method is: ', a)

emp1 = Emp()
emp1.AgeSalaryRatio()

#╦ ----------------------------------------------------------------------------
def ageSalaryRatio(age, salary):
    
     a = age / salary
     print("Age Salary Ratio Function is: ",a)  
     
ageSalaryRatio(30, 3000)
#╦ ----------------------------------------------------------------------------
def findArea(x, y): 
    #area = x*y**2
    #return area
    return x*y**2
    
pi= 3.14
r =7
print(findArea(pi, r))
print(findArea(pi, 10))

#%% Constructor and Initializer :


class Animal(object):
    def __init__(self, a, b):
        self.name = a
        self.age = b 
        
    
    def getAge(self):
        return self.age
    def getName(self):
        print(self.name)

a1 = Animal('dog', 2)
a2 = Animal("cat",4)

#%%


    















































