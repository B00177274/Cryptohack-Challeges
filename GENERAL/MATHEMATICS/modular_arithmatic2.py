def fermat_theorem_mod(base, exp, prime):
    if exp == prime:
        return base
    elif exp + 1 == prime and base % prime != 0:
        return 1
    else:
        return -1;
        
print(fermat_theorem_mod(273246787654, 65536, 65537))


#Solution
#The function fermat_theorem_mod implements a simplified version of Fermat's Little Theorem to perform modular exponentiation checks. 
# It checks three conditions: if the exponent is equal to the prime, it returns the base; if the exponent is one less than the prime and the base is not divisible by the prime, it returns 1;
#  otherwise, it returns -1. In the given example, the function is called with base = 273246787654, exp = 65536, and prime = 65537, and the result returned is 1 based on Fermat's theorem.