# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17 
# 935 = 5 * 11 * 17

N = 935
mod1 = 5
mod2 = 11
mod3 = 17

n1 = N / mod1 # 187
n2 = N / mod2 # 85
n3 = N / mod3 # 55

# 187 * 3 = 561 = 1 [5]
# 85 * 7 = 595 = 1 [11]
# 55 * 13 = 715 = 1 [17]

e1 = 561
e2 = 595
e3 = 715

x = 2 * e1 + 3 * e2 + 5 * e3

print("FLAG =", x % N)



#Solution
#The code solves a system of congruences using the Chinese Remainder Theorem. 
# It calculates the partial results using the given moduli and their respective modular inverses, and combines them to find the value of x. Finally, it prints the result x % N as the FLAG.