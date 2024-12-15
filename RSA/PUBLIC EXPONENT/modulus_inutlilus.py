from Crypto.Util.number import long_to_bytes

def find_cube_root(n):
       low = 0
       high = n
       while low < high:
           mid = (low+high)//2
           if mid**3 < n:
               low = mid+1
           else:
               high = mid
       return(low)

ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

print(long_to_bytes(find_cube_root(ct)))


#Solution
#The code defines a function find_cube_root(n) that calculates the integer cube root of a given number n using binary search.
#The function starts by setting low to 0 and high to n, and repeatedly narrows the search range until it finds the integer whose cube is closest to n.
#The ciphertext ct is a large integer, and the code applies the find_cube_root() function to extract its cube root
#Finally, the cube root is converted to bytes using the long_to_bytes() function from the Crypto.Util.number module and printed as the decrypted message.