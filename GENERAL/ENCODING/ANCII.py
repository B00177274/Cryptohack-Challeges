# ASCII Cryptohack - Windy Arya - 5027202071
from os import sep

acode = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
atext = []

for i in acode:
    atext.append(chr(i))

print(*atext, sep="")

#Solution

#The code takes a list of ASCII values (acode) and converts each value into its corresponding character using the chr() function.

#These characters are appended to a list named atext during iteration, effectively building the decoded string character by character.

#Finally, the print function concatenates the characters in atext and outputs the complete string crypto{ASCII_pr1nt4bl3} without any separators between them.

#The import of sep from the os module is unnecessary as it is not used anywhere in the script.

#The code demonstrates a basic application of ASCII decoding to reveal a hidden message, often used in simple cryptographic challenges.