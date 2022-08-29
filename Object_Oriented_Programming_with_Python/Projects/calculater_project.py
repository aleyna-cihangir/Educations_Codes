#%%

# Calculater Project : 
    
class Calculater(object):
    
    def __init__(self, a, b):
        "Initialize values"
        self.value1 = a
        self.value2 = b 
    
    
    def Add(self):
        "Addition a + b = result -> return result"
        return self.value1 + self.value2

        
    def Multiply(self):
        "Multiplication a * b = result -> return result"
        return self.value1 * self.value2
    
    def Division(self):
        "Division a / b = result -> return result"
        return self.value1 / self.value2
    


print("Choose add(1), multiply(2), division(3)")
selection = input("Select 1, 2 or 3")
v1 = input('First  value ')
v2 = input('Second  value ')
c1 = Calculater(v1,v2)
if selection =='1':
    c_add = c1.Add()
elif selection == '2':
    c_mult = c1.Multiply()
elif selection =='3':
    c_div = c1.Division()
else :
    print('There is no proper selection.')

print("Add : {},Multiply : {}, Division : {}".format(c_add, c_mult, c_div)) 

#%%
