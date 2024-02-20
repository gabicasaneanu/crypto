import random


plaintext = ("gronk")
numbers = ''.join(map(str, map(ord,plaintext)))
x = int(numbers)
def isprime (inp):
    if inp == 2 :
        return True
    if not inp & 1:
        return False
    return pow(2,inp-1, inp) == 1
    
def makenum():    
    lak  = random.randint(10000000000,1000000000000000000000000000000000000000000000)
    if (isprime(lak)) == False:
        return(makenum())
    else:
        return(lak)
    
        
        
tableSize = makenum()
print(tableSize)
print(x)
hashKey = tableSize % x
print(hashKey)
