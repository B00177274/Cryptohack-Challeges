def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    for i in matrix:
        for j in i:
            print(chr(j), end="")

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

matrix2bytes(matrix)

#Solution
#The function matrix2bytes iterates over the 2D matrix and prints each value as its corresponding ASCII character.
#  The matrix provided consists of integer values that represent ASCII codes. 
# When these integers are printed, they correspond to the characters "c r y p t o { i n m a t r i x }". 
# This shows how byte values can be mapped to readable text characters in Python