#references - https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/
#https://github.com/dkushagra/DES-Python/blob/master/DES.py
#https://www.tutorialspoint.com/cryptography/data_encryption_standard.html
#https://github.com/anishLearnsToCode/DES
import sys 

#to use this with the tkinter GUI make sure the button call on tkinter calls
#varname = subprocess.run(['python','crypto.py',var]),capture_output = True).stdout
#and initialize var with an input from the user using a tkinter field
#this script works by performing the call - python3 crypt.py plaintext


#Retrieving user input from the CLI
plaintext = sys.argv[1]

#Retrieving user key from the CLI
if len(sys.argv[2]) < 8:
    print("input key needs to be 8 characters long")
    quit()
key = sys.argv[2]



# DES P-box and S-boxes: Core components of the Data Encryption Standard (DES) algorithm,
# providing essential bit permutation and substitution operations for secure encryption.
# Refer to DES standard documentation (e.g., FIPS PUB 46-3) for detailed specifications.
Sboxes = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],

    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],

    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],

    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],

    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],

    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],

    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],

    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]


roundMatrix =  [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# DES Final Permutation (FP) Matrix:
# Specifies the final permutation of the ciphertext bits in the DES algorithm.
# This 64-bit permutation matrix defines the arrangement of bits after the last round of encryption.
# It essentially reverses the effect of the initial permutation.


finalMatrix = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# DES Initial Permutation (IP) Matrix:
# Specifies the initial permutation of the input plaintext or ciphertext bits in the DES algorithm.
# This 64-bit permutation matrix defines the initial arrangement of bits before encryption or decryption.
# Refer to DES standard documentation (e.g., FIPS PUB 46-3) for the exact permutation table.

initialMatrix =  [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# DES Expansion Permutation (E) Matrix:
# Specifies the expansion of the 32-bit half-block to 48 bits in the DES Feistel function.
# This 32-to-48 bit permutation matrix replicates certain bits of the input to create a 48-bit output.
# The expanded half-block is XORed with the round subkey to introduce diffusion in DES.

expansionMatrix  = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# DES Key Permutation (PC1) Matrix:
# Specifies the permutation of the original 64-bit encryption key to derive the 56-bit key used in DES.
# This 64-to-56 bit permutation matrix selects the key bits used in each round's subkey generation.
# Refer to DES standard documentation (e.g., FIPS PUB 46-3) for the exact permutation table.

firstKeyMatrix = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# DES Key Schedule Compression (PC2) Matrix:
# Specifies the compression of a 56-bit round key to a 48-bit subkey used in each round of DES.
# This 56-to-48 bit permutation matrix selects the bits for the final subkey used in each round.
# Refer to DES standard documentation (e.g., FIPS PUB 46-3) for the exact permutation table.

secondKeyMatrix = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]




keyShift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

#Performs permutation on input array depending on the indices of the reference array
def permute(box1,box2):
    return ([box1[index -1] for index in box2])
    
# Performs a bitwise XOR operation between corresponding elements of box1 and box2.    
def xor(box1,box2):
    return ([index1 ^ index2 for index1,index2 in zip(box1,box2)])

#Identical operation to the permute function    
def expand(box1,box2):
    return ([box1[index - 1] for index in box2])

#Bitwise shift corresponding to input shift. Then concatenates both box inputs.    
def leftShift(box1,box2,shift):
    return (box1[shift:] + box1[:shift], box2[shift:] + box2[:shift])

# Splits a given list into sublists of size n.
def splitArray(list, n):
    return [list[i : i + n] for i in range(0, len(list), n)]

#Converts the input value to its binary representation with a specified size, padding with zeros if necessary.   
def binaryVal(box1,size):
    binary = bin(box1)[2:] if isinstance(box1,int) else bin(ord(box1))[2:]
    while len(binary) < size:
        binary = '0' + binary
    return (binary)
    
# Converts a string to a binary representation as a list of integers.    
def stringToBinary(box1):
    arr = []
    for box in box1:
        binary = binaryVal(box,8) 
        #calls binaryVal function with a size of 8 bits(byte)
        binArr = [int(x) for x in list(binary)]
        arr += binArr
    return (arr)
 
# Converts a binary representation (list of integers) to a string.
def binaryToString(box1):
    split_bytes = splitArray(box1, 8)
    out_bytes = []
    for byte in split_bytes:
        bits = []
        for bit in byte:
            bits += str(bit)
        out_bytes.append(''.join(bits))
    result = ''.join([chr(int(b, 2)) for b in out_bytes])
    return result


# Pads the input string to ensure its length is a multiple of 8.    
def pad(box1):
    pad = 8 - (len(box1) % 8)
    box1 += chr(pad) * pad
    return (box1)  

# Removes padding from the input string.    
def unpad(box1):
    pad = ord(box1[-1])
    return data[ : -pad]
      
  
    
# Generates subkeys for DES encryption based on the given key.
def keyGen(key):
    subkeys = []
    key_binary = stringToBinary(key)
    key_permuted = permute(key_binary, firstKeyMatrix)
    left_half, right_half = splitArray(key_permuted, 28)

    for i in range(16):
        left_half, right_half = leftShift(left_half, right_half, keyShift[i])
        key_blocks = left_half + right_half
        subkeys.append(permute(key_blocks, secondKeyMatrix))

    return subkeys
    
# Computes the substitution values for the S-boxes in DES encryption.
def computeSBoxes(box1):
    chunks = splitArray(box1, 6)
    output = []
    
    for x in range(len(chunks)):
        chunk = chunks[x]
        index = int(str(chunk[0]) + str(chunk[5]), 2)
        line = int(''.join([str(i) for i in chunk[1:-1]]), 2)
        sbox_value = Sboxes[x][index][line]
        binary = binaryVal(sbox_value, 4)
        output += [int(ind) for ind in binary]
    
    return output

    
# Performs DES encryption or decryption depending on the 'enc' flag.
def encryption(input_text, key, pad, enc):
    keys = keyGen(key)
    blocks = splitArray(input_text, 8)
    output = []
    
    for block in blocks:
        block = stringToBinary(block)
        block = permute(block, initialMatrix)
        left_half, right_half = splitArray(block, 32)
        var = None
        
        for x in range(16):
            expanded_right = expand(right_half, expansionMatrix)
            if enc == False:
                var = xor(keys[x], expanded_right)
            elif enc == True:
                var = xor(keys[15 - x], expanded_right)
            var = computeSBoxes(var)
            var = permute(var, roundMatrix)
            var = xor(left_half, var)
            left_half = right_half
            right_half = var
        
        output += permute(right_half + left_half, finalMatrix)
    
    final_output = binaryToString(output)
    return final_output



# Orchestrates the encryption process using the provided key and plaintext.
# If padder is True, pads the plaintext before encryption using a padding function.
def driver(key,text,padder):
    if padder == True:
        text = pad(text)
    output = encryption(text,key,padder,False)
    return(output)

# Entry point for DES encryption, taking plaintext and encryption key as input.
# Determines if padding is needed for the plaintext and calls the driver function for encryption.           
def main(plaintext,key):
    padding = (len(plaintext)% 8 != 0)
    output = driver(key,plaintext,padding)
    print(output)
    
main(plaintext,key)
    
    
    
    
