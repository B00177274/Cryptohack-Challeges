text = "label"
result = ""

for i in text:
    result += chr(ord(i)^13)

print(result)



#Solution
#The code iterates over each character in the string "label", performs a bitwise XOR operation between the ASCII value of the character (ord(i)) and the number 13, and then converts the result back to a character (chr()). 
# The XOR operation alters the ASCII value of each character, resulting in a transformed string. After processing all characters, the transformed string is printed as the final result.

#In this case, applying XOR with 13 to each character of "label" will give a different string, which is the output of the XOR operation.