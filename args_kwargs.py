# Unpacking operator

x = {"Hassane", 2 , 3}
print(*x)

y = ["larry", "le", "homard", ["the","goat"]]
print(*y)

def func(x,y):
    print(x, y)
    
# Single asterix for tuples
pairs = [(1,2),(3,4)]
for pair in pairs:
    func(*pair)
    
# Double asterix for dictionnaries
# It puts automatically in order based on the name of the keys
pairs2 = [{'x':1,'y':2},{'y':4,'x':3}]
for pair in pairs2:
    func(**pair)
    
# args stands for the positionnal arguments
# kwargs stands for keywords arguments
# Used for functions where you don't know the arguments
def mysterious_func(*args, **kwargs):
    print(args, kwargs)
    print(*args)
    print(**kwargs) # Error
    
mysterious_func(1,2,name="hassane",age=20)