# Functions : Objects than make a treatment and/or return a value
def func():
    print("I'm func original")
# Can define a function inside a function
def func2():
    print("func2")
    def func():
        print("func in func2")
    func()
func()
func2()

# You can add arguments
def plus(x, y):
    print(x, "+", y, "=", x+y)
plus(1,2)

# You can return many values
def plus_minest(x, y):
    return x+y, x-y
x, y = plus_minest(4,3)
print(x,y)

# You can return functions because they're just objects
def funcfunc():
    def func(word):
        print(word)
    return func  
funcfunc()("the word")

# You can affect them in variables, because they're just objects
x = funcfunc()
x("funcs are objs")

# You can add optional value, with it's name
def full_name(first_name, last_name=None):
    print("Full name is ", first_name, last_name)

full_name("Hassane")
full_name("Hassane","Mamane")