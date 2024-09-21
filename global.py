# use "global" keyword to modify global variables from functions : not advised
x = "jill"

def func(name):
    x = name

def func_global(name):
    global x 
    x = name

func("claire") 
print(x) # jill

func_global("claire")
print(x) # claire