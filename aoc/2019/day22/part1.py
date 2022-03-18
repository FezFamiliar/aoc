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

 

end = 10007
deck = [i for i in range(end)]

# dealNewStack(deck)
# cutNcards(-2)
# dealWithIncrement(7)
# cutNcards(8)
# cutNcards(-4)
# dealWithIncrement(7)
# cutNcards(3)
# dealWithIncrement(9)
# dealWithIncrement(3)
# cutNcards(-1)
# print(deck)


# #deal into new stack: f(x) = -x - 1 mod m -> a = -1 , b = -1
# a = (-1, -1) # representing the coefficients of a LCF (linear congruental function)  f(x) = ax + b mod m 


# # cut n: f(x) = x- n mod m -> a = 1, b = -n
# b = (1, -n)

# #deal with increment n: f(x) = n*x mod m => a = n, b = 0
# c = (n, 0) 

def compose(a, b, c, d):

    return (a * c % end, (b * c + d) % end)

def calFinal(a, b, x):
    return (a * x + b) % end 

tuples = []
input = input.split('\n')
for i in input:
    if i[0] == 'c':   # cut
        amount = re.findall('-?\d+', i)
        lcf = (1, -int(amount[0]))
        tuples.append(lcf)
        #cutNcards(int(amount[0]))
    elif 'deal into' in i:
        lcf = (-1, -1)
        tuples.append(lcf)
        #dealNewStack(deck)
    else:
        amount = re.findall('\d+', i)
        lcf = (int(amount[0]), 0)
        tuples.append(lcf)
        #dealWithIncrement(int(amount[0]))
    



nn = len(tuples)
for i in range(0, nn - 1):

    a = compose(tuples[i][0], tuples[i][1], tuples[i + 1][0], tuples[i + 1][1])

        

print(f"this is ti: {calFinal(a[0], a[1], 2019)}")
# for i in range(0, end):
#     if deck[i] == 2019:
#         print(f"position of card 2019 is at: {i}")



# def calculateX(a, b, x):
#     return (a * x + b) % end


# end = 10
# def composeTwoTuples(a, b):

#     return ((a[0] * b[0]) % end, (a[1] * b[0] + b[1]) % end)

# a = (7, 0)
# b = (-1, -1)

# c = composeTwoTuples(a, b)
# d = composeTwoTuples(c, b)

# print(d)   # (7, 0) ---> f(x) = ax + b mod m



# print(f"Result after caulculating x from lcf: {calculateX(d[0], d[1], 1)}")
# exit(1)





# 0 1 2 3 4 5 6 7 8 9 ---> end = 10

# deal into new stack => f(x) = -m -x - 1 => f(x) = ax + b mod end => a, b = -1

# => f(x) = -x - 1 mod 10

# end = 10

# deck = [i for i in range(end)]
# dealWithIncrement(7)
# dealNewStack(deck)
# dealNewStack(deck)
# print(deck)


# def dealIntoNewStackModWay(x):          # a = -1, b = -1 
#     return (-x - 1) % end


# def cutNCardsModWay(x, n):   # a = 1, b = -n
#     return (x - n) % end


# def dealWithIncremenetModWay(x, n):         # move the card at position x to (n * x) % end, a = n, b = 0
#     return (n * x) % end 


# x = 1
# n = 7


# # for i in range(0, end):
# #     print(f"dealing with increment, n: {n}, : x = {i}: {cutNCardsModWay(i, n)}")



# # f(x) = ax + b mod m

# # g(x) = cx + d mod m

# # g(f(x)) = c(ax + b mod m) + d mod m => cax + cb + d mod m 





# # deal with increment 7 => f(x)
# # deal into new stack   => g(x)
# # deal into new stack   => h(x)



# print(f"compose: {compose(-1, -1, compose(-1, -1, n, 0)[0], compose(-1, -1, n, 0)[1])}")


# #(7, 0) => F(X) = 7x + 0 mod end







# for i in range(0, end):
#     print(f"This is it: {calFinal(7, 0, i)}")

