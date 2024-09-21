# Opérateurs conditionnels

# Egalité : ==
print("hello"=="hello") # True
# Différence : !=
print(5!=2) # True
# Supérieur : >
print('a'>'z') # False
# Supérieur ou Egal : >=
print(1>=0.5) # True
# Inférieur : <
print('ali'<='1z') # False
# Inférieur ou Egal : <=
print(1<=0.5) # False
# not, and, or : A traiter toujours dans cet ordre (notandor)
print(True and False) # False
print(True or not(8>=2)) # True
print(not(not(True and not(len(["Dalton",8,[{"Maria":12},"Boubacar"],78])==4)))) # False
print(not True or ('71'>'Morloc') and not('z'>'bibi') or False and not False) # False