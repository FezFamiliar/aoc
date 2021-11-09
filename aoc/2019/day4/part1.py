min_r = 387638
max_r = 919123

def passesAll(x):
    
    x = str(x)
    
    if adjacentDigits(x) == False:
        return False
        
    if decrease(x):
        return False
        
        
    return True
    
def adjacentDigits(x):
    
    for i in range(5):
        if x[i] == x[i + 1]:
            return True
            
    return False
    


def decrease(x):
    for i in range(5):
        if x[i] > x[i + 1]:
            return True
            
    return False

result = 0

for i in range(min_r, max_r):
    if passesAll(i):
        result += 1
        
    
print("ffff")
print(result)
        