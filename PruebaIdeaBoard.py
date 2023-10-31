import board
from time import sleep
from ideaboard import IdeaBoard

ib = IdeaBoard()

switch= ib.DigitalIn(board.IO27)
pot = ib.AnalogIn (board.IO33)

def capturarvalor():

    while switch.value:
        val= pot.value
        map= ib.map_range(val,2819,62655,0,255)
        print(val, map)
        ib.arcoiris = map
    
    ib.pixel = (255,0,0)

    return val

print ("valor capturado = "  ,capturarvalor())


