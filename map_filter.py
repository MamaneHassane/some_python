# Map and filter use functions or lambda function to map or to filter
x = [1,2,4,7,8,-5,3,-9,-2,3]

# Filter with a lambda function directly or write it outside
positives = filter(lambda x:x>=0, x)
print(list(positives))

# Filter with a function
def even(x):
    return x%2==0
evens = filter(even, x)
print(list(evens))

# Map with a lambda function directly or write it outside
plus_two = map(lambda x: x+2, x)
print(list(plus_two))

# Map with a function
def add_three(x):
    return x+3
plus_three = map(add_three, x)
print(list(plus_three))