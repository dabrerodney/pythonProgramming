import math

def checkDartBoard(x, y):
    result = math.sqrt(x**2 + y**2)
    return result <= 10

coordinate = [(0,0),(10,10),(6,6),(7,8)]

for i in coordinate:
    x, y = i
    result = checkDartBoard(x, y)
    print (f"Dart at ({x},{y}) hits the board: {result}")