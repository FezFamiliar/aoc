

def dealWithIncrement(n):
    global deck
    new_deck = [0 for i in range(end)]
    new_deck[0] = deck[0]

    for m in range(1, 10):
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

 

end = 10
deck = [i for i in range(end)]
print(deck)

dealNewStack(deck)
cutNcards(-2)
dealWithIncrement(7)
cutNcards(8)
cutNcards(-4)
dealWithIncrement(7)
cutNcards(3)
dealWithIncrement(9)
dealWithIncrement(3)
cutNcards(-1)
print(deck)








    
    
    
