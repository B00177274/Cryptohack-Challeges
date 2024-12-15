from operator import xor

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    for i in matrix:
        for j in i:
            print(chr(j), end="")

def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = xor(s[i][j], k[i][j])
    
    matrix2bytes(matrix)

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

add_round_key(state, round_key)


#Solution
#The add_round_key function in the AES encryption algorithm performs an XOR operation between the state matrix and the round key matrix. 
# This step is critical as it combines the state with the key material to progress through the encryption rounds. 
# The matrix2bytes function prints the resulting matrix by converting each byte to its corresponding character. 
# After calling add_round_key, the modified state is displayed as a string of characters, showing the intermediate encrypted result.