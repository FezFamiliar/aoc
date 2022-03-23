
total_ores_spent = 0
all_chemicals = {}
leftover_chemicals = {}
acquired = {}
ores = {}

def printChemicalStatus():
    

    print(f"You have thus far these chemicals:")

    for k, v in acquired.items():
        print(f"{k} - {v}")


    print(f"Your leftover chemicals are:")

    for k, v in leftover_chemicals.items():
        print(f"{k}:{v}")


    print(f"Total ores spent thus far: {total_ores_spent}")



def IsInCache(c):
    for k, v in leftover_chemicals.items():
        if c[1] == k and v >= int(c[0]):
            return True
    
    return False

def checkOre(c):
    global total_ores_spent
    for k, v in ores.items():
        if k[1] == c[1]:

            if int(c[0]) <= int(k[0]):
                if IsInCache(c):
                    print(f"OIs in cache")
                    acquired[c[1]] += int(c[0])              # aquire chemical from cache
                    leftover_chemicals[c[1]] -= int(c[0])                                                  # decrease number in cache
                else:
                    
                    if c[1] in acquired:
                        acquired[c[1]] += int(c[0])
                    else:
                        acquired[c[1]] = int(c[0])
                    
                    total_ores_spent += int(v[0])      # increment total_ores_spent
                    print(f"Spent: {int(v[0])} ORES for: {c[1]}")
                    l = int(k[0]) - int(c[0])          # calculate leftover chemicals

                    if c[1] in leftover_chemicals:
                        leftover_chemicals[c[1]] += l 
                    else:
                        leftover_chemicals[c[1]] = l       # save leftover chemicals in chace
                #printChemicalStatus()   
            else:
                aux = 0
                while int(c[0]) > aux:

                    total_ores_spent += int(v[0])
                    aux += int(k[0])
                if c[1] in acquired:
                    acquired[c[1]] += int(c[0])
                else:
                    acquired[c[1]] = int(c[0])

                if c[1] in leftover_chemicals:
                    leftover_chemicals[c[1]] += aux % int(c[0])
                else:
                    leftover_chemicals[c[1]] = aux % int(c[0])       # save leftover chemicals in chace
                #exit(1)
            return True
    
    return False



def consume(chemicals):  # chemicals => [(), (), ()] needed for FUEL

    for c in chemicals:
        if checkOre(c):
            pass
        else:
            for k, v in all_chemicals.items():
 
                if c[1] == k[1]:         
                    for i in range(0, int(c[0])):
                        consume(v)
                        acquired[c[1]] = int(c[0])



input = '''9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL'''

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



for k, v in all_chemicals.items():

    if v[1] == 'ORE':
        ores[k] = v
    if k[1] == 'FUEL':
        print(f"Chemicals needed for fuel: {v}")
        consume(v)
        printChemicalStatus()
        break








