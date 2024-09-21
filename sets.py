# Collection of unique elements
# Only to care if something exists or don't exists
# To create an empty set
x = set()
# Because {} is a dictionnary
print(type({})) # dict
# Create a non-empty set
s = {1,5,4,7,5}
print(s) # Any element one time
# Add an element
s.add(8)
print(s)
# Remove an element
s.remove(5)
print(s)
# Verify an existance
print(5 in s) # False
print(1 in s) # True
# Union with another set
print(s.union({1,5,7,8,9,12}))
# Intersection with another set
print(s.intersection({1,5,7,8}))
