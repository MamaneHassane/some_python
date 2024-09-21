# One line initialisations of collections

x = [val for val in range(1,5)]
print(x)

x = [val - 2 for val in range(10,0,-2)]
print(x)

x = [val for val in range(10) for val in range(10)]
print(x)

x = {val:val*2 for val in range(5,10) if val % 2 >=0.5}
print(x)

x = tuple(val*2 for val in range(5,10) if val % 2 >=0.5)
print(x)