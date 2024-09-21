# Lambda functions are inline small functions
x = lambda x, y: x+y
print(x(2,3))

even = lambda x: x%2==0
print(even(6)) # True
print(even(7)) # False