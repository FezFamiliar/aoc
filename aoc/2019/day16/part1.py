
input = '59713137269801099632654181286233935219811755500455380934770765569131734596763695509279561685788856471420060118738307712184666979727705799202164390635688439701763288535574113283975613430058332890215685102656193056939765590473237031584326028162831872694742473094498692690926378560215065112055277042957192884484736885085776095601258138827407479864966595805684283736114104361200511149403415264005242802552220930514486188661282691447267079869746222193563352374541269431531666903127492467446100184447658357579189070698707540721959527692466414290626633017164810627099243281653139996025661993610763947987942741831185002756364249992028050315704531567916821944'


phases = 100
input = [int(x) for x in input]
pattern = [0, 1, 0, -1]
n = len(input)

output = [0 for x in range(n)]


def figureOutPattern(j):

    f = []
    for i in pattern:
        for m in range(0, j + 1):
            f.append(i)

    return f


for phase in range(0, phases):
    for j in range(0, n):
        r = 0
        new_pattern = figureOutPattern(j)
        n_new_pattern = len(new_pattern)

        for i in range(0, n):
            r += input[i] * new_pattern[(i + 1) % n_new_pattern]

        if r < 0: 
            r = -1 * r

        output[j] = r % 10

    for c in range(0, n):
        input[c] = output[c]

result = ""
for i in range(0, 8):
    result = result + str(output[i])
print(f"phase: {phases}, output is: {output}")
print(f"First 8 digits are: {result}")


