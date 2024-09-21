# slice : [start:stop:step]
# slice work on collection, not only lists
# If step is positive : default start is 0, default stop is end of the collection
# If step is negative : default start is end of the collection, default start is start of the collection
x = [1,2,8,8,-98,77,0,2,69,41,-56,12,3.2]
slice = x[1:len(x):2]
print(slice)
slice = x[:5]
print(slice)
slice = x[2:]
print(slice)
slice = x[::2]
print(slice)
slice = x[5:len(x)]
print(slice)
# Easiest way to reverse a list
slice = x[::-1]
print(slice)