import re

input = '''cut 3334
deal into new stack
deal with increment 4
cut -342
deal with increment 30
cut -980
deal into new stack
cut -8829
deal with increment 10
cut -7351
deal with increment 60
cut -3766
deal with increment 52
cut 8530
deal with increment 35
cut -6979
deal with increment 52
cut -8287
deal with increment 34
cut -6400
deal with increment 24
deal into new stack
deal with increment 28
cut 7385
deal with increment 32
cut -1655
deal with increment 66
cut -2235
deal with increment 40
cut 8121
deal with increment 71
cut -2061
deal with increment 73
cut 7267
deal with increment 19
cut 2821
deal with increment 16
cut 7143
deal into new stack
deal with increment 31
cut 695
deal with increment 26
cut 9140
deal with increment 73
cut -4459
deal with increment 17
cut 9476
deal with increment 70
cut -9832
deal with increment 46
deal into new stack
deal with increment 62
cut 6490
deal with increment 29
cut 3276
deal into new stack
cut 6212
deal with increment 9
cut -2826
deal into new stack
cut -1018
deal into new stack
cut -9257
deal with increment 39
cut 4023
deal with increment 69
cut -8818
deal with increment 74
cut -373
deal with increment 51
cut 3274
deal with increment 38
cut 1940
deal into new stack
cut -3921
deal with increment 3
cut -8033
deal with increment 38
cut 6568
deal into new stack
deal with increment 68
deal into new stack
deal with increment 70
cut -9
deal with increment 32
cut -9688
deal with increment 4
deal into new stack
cut -1197
deal with increment 54
cut -582
deal into new stack
cut -404
deal into new stack
cut -8556
deal with increment 47
cut 7318
deal with increment 38
cut -8758
deal with increment 48'''


def dealWithIncrement(n):
    global deck
    new_deck = [0 for i in range(end)]
    new_deck[0] = deck[0]

    for m in range(1, end):
        new_deck[(m * n) % end] = deck[m]
    
    deck = new_deck

def dealNewStack(deck):

    for i in range(0, end // 2):
        aux = deck[i]
        deck[i] = deck[end - i - 1]
        deck[end - i - 1] = aux




def cutNcards(n):
    
    if n < 0:
        # cut from bottom onto top
        n = abs(n)
        aux = [0 for i in range(n)]
        j = 0
        for i in range(end - n, end):
            aux[j] = deck[i]
            j = j + 1
        #apped onto top
        
        first_half = deck[:end - n]
        
        deck[:n] = aux
        deck[n:] = first_half
        


    else:
        # cut from top onto bottom
        aux = deck[:n]

        deck[:end - n] = deck[n:] # shift everything left
        deck[end - n:] = aux      # append onto bottom

 
end = 119315717514047
k = 101741582076661
def compose(a, b, c, d):

    return (a * c % end, (b * c + d) % end)

def calFinal(a, b, x):
    
    return (x - b) * pow(a, -1, end) % end


def pow_compose(f, k):
    g = (1, 0)
    
    while k > 0:
        if k % 2 == 1:
            g = compose(g[0], g[1], f[0], f[1])
        k = k // 2
        f = compose(f[0], f[1], f[0], f[1])
        
    return g
    
lcfs = []
input = input.split('\n')
for i in input:
    if i[0] == 'c':   # cut
        amount = re.findall('-?\d+', i)
        lcfs.append((1, -int(amount[0])))
    elif 'deal into' in i:
        lcfs.append((-1, -1))
    else:
        amount = re.findall('\d+', i)
        lcfs.append((int(amount[0]), 0))
    

lcf_length = len(lcfs)
F = (lcfs[0][0], lcfs[0][1])

for i in range(1, lcf_length):

    F = compose(F[0], F[1], lcfs[i][0], lcfs[i][1])



F = pow_compose(F, k)


print(f"F is: {F}")
print(f"this is it: {calFinal(F[0], F[1], 2020)}")




