UserInput = '88.8'
try:
    int(float(UserInput))
except:
    UserInput = 0
print(UserInput)