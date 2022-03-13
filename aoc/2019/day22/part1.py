

def dealWithIncrement(n):
    
    new_deck = [0 for i in range(end)]
    new_deck[0] = deck[0]

    for m in range(1, 10):
        new_deck[(m * n) % end] = deck[m]
    
    print(f"new deck: {new_deck}")

def dealNewStack(deck):

    deck.sort(reverse=True)




def cutNcards(n):
    
    if n < 0:
        # cut from bottom onto top
        n = abs(n)
        aux = deck[:-n - 1:-1]
        aux.sort()
        
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
dealWithIncrement(3)








    
    
    