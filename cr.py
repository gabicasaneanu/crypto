import random
import string
import sys 

plaintext = sys.argv[1]
real_plaintext = plaintext.upper()

#seed between 150 and 225 - ascii chars

seed = random.randint(170,8000)

print('seed is: ',seed)

conversions = []
counter = 0
for i in range(seed):
    while counter != 26:
        conversions.append(chr(seed + counter))
        counter+=1
        

letters = list(string.ascii_uppercase)
con_dict = {}


for i in range(0,25):
    con_dict[letters[i]] = conversions[i]
    
def Encrypt(plaintext):
    encrypted_message = '' 
    for char in plaintext:
        encrypted_message = encrypted_message + con_dict[char]
    encrypted_message
    return (encrypted_message)
    
encrypted_message = Encrypt(real_plaintext)    

def Decode(cyphertext):
    decrypted_message = ''
    for char in cyphertext:
        for key in con_dict:
            if con_dict[key] == char:
                decrypted_message = decrypted_message + key
    return decrypted_message
        

print('Original Plaintext: ' , plaintext)
print('Encrypted Plaintext: ' , encrypted_message)
print('Decrypted Plaintext: ' , Decode(encrypted_message))
     
    




