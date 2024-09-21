# Lists : Lists are mutable structures
x = [4, True, 'Hi mom']
# Length of the list
print(len(x)) # 3
# Append
x.append('Hello')
print(x) # [4, True, 'Hi mom', 'Hello']
# Extend
x.extend([7, {"Mario":12}, "Jellyfish"])
print(x)
# pop
x.pop(len(x)-1)
x.pop(5)
print(x)
# Lists are mutables
x[0] = 5
print(x)
# Affecting by reference
y = x
x[0] = 6 # Change on x apply on y
print('By reference', x, '\n', y) # Are the same
# Affecting by value
y = x[:]
x[0] = 7 # Change on x apply on y
print('By value', x, '\n', y) # Are the same

