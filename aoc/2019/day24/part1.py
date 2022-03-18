
from copy import copy, deepcopy


input = '''.......
.#.##..
.###.#.
.#...#.
.##..#.
..#....
.......'''

input = input.split('\n')

cols = len(input[0])
rows = len(input)

print(f"Inital state...")
for i in range(0, rows):
    for j in range(0, cols):
        print(input[i][j], end="")
    print()




def calculateResults(mgp):

    c = 0
    result = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            c += 1
            if mgp[i][j] == '#':
                result += pow(2, c - 1)


    return result

minutes = 400
totals = []


for m in range(0, minutes):
    mgp = ['.......']
    aux = ''
    for i in range(1, rows - 1):
        aux += '.'
        for j in range(1, cols - 1):

            bugs = 0

            if input[i][j + 1] == '#':
                bugs += 1
            if input[i][j - 1] == '#':
                bugs += 1
            if input[i - 1][j] == '#':
                bugs += 1
            if input[i + 1][j] == '#':
                bugs += 1


            if input[i][j] == '.':          # empty space
                if bugs == 1 or bugs == 2:          # gets infested
                    aux += '#'
                else:
                    aux += '.'

            elif input[i][j] == '#':                       # bug 
                if bugs == 1:           # bug dies
                    aux += '#'
                else:
                    aux += '.'

        aux += '.'
        mgp.append(aux)
        aux = ''
    mgp.append('.......')

    # check if this mgp has been repeated already

    for k in range(0, m):

        if totals[k] == mgp:
            print(f"Repeater found!")
            print(mgp)
            print(f"The answer is: {calculateResults(mgp)}")
            exit(1)

    
    totals.append(mgp)
    input = totals[m]







for t in range(0, minutes):
    print(f"{t}--------------------------------------------")
    for i in range(0, rows):
        for j in range(0, cols):
            print(totals[t][i][j], end="")

        print()
