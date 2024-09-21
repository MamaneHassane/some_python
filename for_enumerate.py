# for loops

# Given the (start, stop, step)
# If one number, it is by default the stop
# Does not include the stop (here 10)
for i in range(10):
    print(i) # 0 1 2 3 4 5 6 7 8 9
    
for i in range(0,12,2):
    print(i) # 0 2 4 6 8 10

# Looping on lists
x = ["Hello", 1, 3, {"name":"Jack"}]
for i in range(len(x)):
    print(x[i])
    
for i, el in enumerate(x):
    print(el)