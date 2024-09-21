# Tuples : Tuples are immutables lists
# They can't be changed after being defined

x = (0,2,'Nevada', [{"Chickens": {"Morlock" : 5}}])
print(x)
print(x[len(x)-1][0])

# Cannot change or append or add or extend or pop
x[0] = 1 # Error
