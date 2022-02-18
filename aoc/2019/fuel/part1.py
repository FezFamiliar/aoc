
from array import array
from operator import truediv


total_ores_spent = 0
all_chemicals = {}
leftover_chemicals = {}
acquired = {}

def printChemicalStatus():
    

    print(f"You have thus far these chemicals:")

    for k, v in acquired.items():
        print(f"{k} - {v}")


    print(f"Your leftover chemicals are:")

    for k, v in leftover_chemicals.items():
        print(f"{k}:{v}")


    print(f"Total ores spent thus far: {total_ores_spent}")



def consume(chemicals):
    global total_ores_spent

    for c in chemicals:
        for k, v in all_chemicals.items():
            if c[1] == k[1]:                
                if type(v) == list:
                    for i in v:
                        v[1]
                        print(f"k - {i}") 
                else:                
                    if int(c[0]) < int(k[0]):            # check quantity & buy
                        if v[1] == 'ORE':                # check if its directly ORE, if not, somehow recurse

                            acquired[c[1]] = int(c[0]) 
                            if not checkLeftovers(c):
                                total_ores_spent += int(v[0])

                            leftover_chemicals[c[1]] = int(k[0]) % int(c[0])
                        else:
                            consume()


def checkLeftovers(chemical_tuple):

    for k, v in leftover_chemicals.items():
        if k == chemical_tuple[0] and v >= chemical_tuple[1]:
            v -= chemical_tuple[1]
            return True

    return False



input = '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL'''

input = input.split('\n')


for i in input:
    bridge = i.find('=')
    value_tuple = (i[bridge + 3:].split(' ')[0], i[bridge + 3:].split(' ')[1])

    if ',' in i[0:bridge - 1]:
        multiple_chemical = i[0:bridge - 1].split(',')
        multiple_chemical = [i.strip() for i in multiple_chemical]
        cc = []

        for m in multiple_chemical:
            stripped = m.split(' ')
            key_tuple = (stripped[0], stripped[1])
            cc.append(key_tuple)
        
        all_chemicals[value_tuple] = cc
    else:
        key_tuple = (i[0:bridge - 1].split(' ')[0], i[0:bridge - 1].split(' ')[1])
        all_chemicals[value_tuple] = key_tuple


print(f"All chemical reactions: (k, v)")


for k, v in all_chemicals.items():
    print(f"{k} => {v}")
    if k[1] == 'FUEL':
        print(f"Chemicals needed for fuel: {v}")
        consume(v)
        #printChemicalStatus()
        break







