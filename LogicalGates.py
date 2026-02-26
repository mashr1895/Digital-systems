#### Digial System Course - Logical Gates ###
#The basic Logical gates - OR,AND,NOT,NOR,NAND,XOR.
#These will function as the atomic components for us for later in more advanced logical components.

#OR gate
def OR(x,y):
    if x == 1 or y == 1:
        return 1
    else:
        return 0

#AND gate
def AND(x,y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0

#NOT gate
def NOT(x):
    if x == 1:
        return 0
    else:
        return 1

#NOR gate
def NOR(x,y):
    if OR(x,y) == 1:
        return 0
    else:
        return 1
    
#NAND gate
def NAND(x,y):
    if AND(x,y) == 1:
        return 0
    else:
        return 1

def XOR(x,y):
    if ((x == 0 and y == 1) or (x == 1 and y == 0)):
        return 1
    else:
        return 0

