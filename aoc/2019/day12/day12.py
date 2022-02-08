import re
# Io, Europa, Ganymede, and Callisto.
input = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

pos = re.findall(r'[-\d]+', input)
pos = [ int(x) for x in pos ]
n = len(pos)
vel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(pos)



for x in range(3, n, 3):

    if pos[x] > pos[0]:
        vel[0] += 1
    else:
        vel[0] -= 1

for x in range(0, n, 3):
    
    if x == 3:
        continue
    if pos[x] > pos[3]:
        vel[3] += 1
    else:
        vel[3] -= 1
        
for x in range(0, n, 3):

    if x == 6:
        continue

    if pos[x] > pos[6]:
        vel[6] += 1
    else:
        vel[6] -= 1

for x in range(0, n, 3):
    if x == 9:
        continue
    if pos[x] > pos[9]:
        vel[9] += 1
    else:
        vel[9] -= 1


# ---------------------------------------------------------------------------


for y in range(4, n, 3):

    if pos[y] > pos[1]:
        vel[1] += 1
    else:
        vel[1] -= 1

for y in range(1, n, 3):
    
    if y == 4:
        continue
    if pos[y] > pos[4]:
        vel[4] += 1
    else:
        vel[4] -= 1
        
for y in range(1, n, 3):

    if y == 7:
        continue

    if pos[y] > pos[7]:
        vel[7] += 1
    else:
        vel[7] -= 1

for y in range(1, n, 3):
    if y == 10:
        continue
    if pos[y] > pos[10]:
        vel[10] += 1
    else:
        vel[10] -= 1



# -------------------------------------------------------------------------------------

for z in range(5, n, 3):

    if pos[z] > pos[2]:
        vel[2] += 1
    else:
        vel[2] -= 1

for z in range(2, n, 3):
    
    if z == 5:
        continue
    if pos[z] > pos[5]:
        vel[5] += 1
    else:
        vel[5] -= 1
        
for z in range(2, n, 3):

    if z == 8:
        continue

    if pos[z] > pos[8]:
        vel[8] += 1
    else:
        vel[8] -= 1

for z in range(2, n, 3):
    if z == 11:
        continue
    if pos[z] > pos[11]:
        vel[11] += 1
    else:
        vel[11] -= 1





print(vel)




def gravity():
    return False



def velocity():
    return False
