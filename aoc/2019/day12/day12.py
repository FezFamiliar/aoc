import re
# Io, Europa, Ganymede, and Callisto.
input = '''<x=12, y=0, z=-15>
<x=-8, y=-5, z=-10>
<x=7, y=-17, z=1>
<x=2, y=-11, z=-6>'''

pos = re.findall(r'[-\d]+', input)
pos = [ int(x) for x in pos ]
n = len(pos)
vel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#print(pos)
steps = 1000

for step in range(0, steps):
#x
    for x in range(3, n, 3):

        if pos[x] > pos[0]:
            vel[0] += 1
        elif pos[x] == pos[0]:
            pass
        else:
            vel[0] -= 1

    for x in range(0, n, 3):
        
        if x == 3:
            continue
        if pos[x] > pos[3]:
            vel[3] += 1
        elif pos[x] == pos[3]:
            pass
        else:
            vel[3] -= 1
            
    for x in range(0, n, 3):

        if x == 6:
            continue

        if pos[x] > pos[6]:
            vel[6] += 1
        elif pos[x] == pos[6]:
            pass
        else:
            vel[6] -= 1

    for x in range(0, n, 3):
        if x == 9:
            continue
        if pos[x] > pos[9]:
            vel[9] += 1
        elif pos[x] == pos[9]:
            pass
        else:
            vel[9] -= 1


    # ---------------------------------------------------------------------------y


    for y in range(4, n, 3):

        if pos[y] > pos[1]:
            vel[1] += 1
        elif pos[y] == pos[1]:
            pass
        else:
            vel[1] -= 1

    for y in range(1, n, 3):
        
        if y == 4:
            continue
        if pos[y] > pos[4]:
            vel[4] += 1
        elif pos[y] == pos[4]:
            pass
        else:
            vel[4] -= 1
            
    for y in range(1, n, 3):

        if y == 7:
            continue

        if pos[y] > pos[7]:
            vel[7] += 1
        elif pos[y] == pos[7]:
            pass
        else:
            vel[7] -= 1

    for y in range(1, n, 3):
        if y == 10:
            continue
        if pos[y] > pos[10]:
            vel[10] += 1
        elif pos[y] == pos[10]:
            pass
        else:
            vel[10] -= 1



    # -------------------------------------------------------------------------------------z

    for z in range(5, n, 3):

        if pos[z] > pos[2]:
            vel[2] += 1
        elif pos[z] == pos[2]:
            pass
        else:
            vel[2] -= 1

    for z in range(2, n, 3):
        
        if z == 5:
            continue
        if pos[z] > pos[5]:
            vel[5] += 1
        elif pos[z] == pos[5]:
            pass
        else:
            vel[5] -= 1
            
    for z in range(2, n, 3):

        if z == 8:
            continue

        if pos[z] > pos[8]:
            vel[8] += 1
        elif pos[z] == pos[8]:
            pass
        else:
            vel[8] -= 1

    for z in range(2, n, 3):
        if z == 11:
            continue
        if pos[z] > pos[11]:
            vel[11] += 1
        elif pos[z] == pos[11]:
            pass
        else:
            vel[11] -= 1






    prev_state = pos

    for i in range(0, n):
        pos[i] += vel[i]
    print(prev_state)
    exit()
    print()
    exit()

    if pos == prev_state and step != 1:
        print(pos)
        print(prev_state)
        print(f"The number is: {step}")
        exit()

    # print(f"velocity after {step}: {vel}")
    # print(f"position after {step}: {pos}")



# A moon's potential energy is the sum of the absolute values of its x, y, and z position coordinates.

def potentialEnergy(x, y, z):
    return abs(x) + abs(y) + abs(z)


# A moon's kinetic energy is the sum of the absolute values of its velocity coordinates.
def kineticEnergy(x, y, z):
    return abs(x) + abs(y) + abs(z)


def totalEnergy(xp, yp, zp, xk, yk, zk):
    return potentialEnergy(xp, yp, zp) * kineticEnergy(xk, yk, zk)

total = 0
for i in range(0, n, 3):    
    total += totalEnergy(pos[i], pos[i + 1], pos[i + 2], vel[i], vel[i + 1], vel[i + 2])

print(f"Total energy after {steps} steps is {total}")
    







