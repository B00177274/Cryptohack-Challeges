#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))


#Solution
#The code checks the version of Python being used and issues a warning if it's Python 2, advising the user to upgrade to Python 3. 
# Then, it defines a list of integers (ords), which represent characters encoded with an XOR operation. 
# The code performs an XOR operation with each value in the list using the value 0x32 and converts the result back to characters. 
# Finally, it prints the decoded string, which is presumably the flag.
