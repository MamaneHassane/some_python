# Use the keyword "raise" to raise exceptions
x = input("Enter a number \n")
if type(int(x)) != int:
    raise Exception(x, " is not a number")
else:
    print(x, "is a number !")

try:
    y = int(x) / 0 # Will always raise the exception
except Exception as e:
    print(e)
    raise e
finally:
    print("Operation terminated")
    