#### Digial System Course - Logical Gates Class ###
#The basic Logical gates - OR,AND,NOT,NOR,NAND,XOR.
#These will function as the atomic components for us for later in more advanced logical components.



#OR gate
def or_logic(x,y):
    if x == 1 or y == 1:
        return 1
    else:
        return 0

#AND gate
def and_logic(x,y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0

#NOT gate
def not_logic(x):
    if x == 1:
        return 0
    else:
        return 1

#NOR gate
def nor_logic(x,y):
    if or_logic(x,y) == 1:
        return 0
    else:
        return 1
    
#NAND gate
def nand_logic(x,y):
    if and_logic(x,y) == 1:
        return 0
    else:
        return 1

def xor_logic(x,y):
    if (x == 0 and y == 1):
        return 1
    elif (x == 1 and y == 0):
        return 1
    else:
        return 0


#### Gate Class ####
class Gate:
    def __init__(self,name,num_inputs,logic):
        self.name = name
        self.num_inputs = num_inputs
        self.logic = logic

    def __call__(self,*args):
        return self.logic(*args)

AND = Gate("AND", 2, and_logic)
print (AND(1, 0))   # should return 0
print (AND(1, 1))   # should return 1