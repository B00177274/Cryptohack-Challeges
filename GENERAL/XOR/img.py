import numpy as np
import matplotlib.pyplot as plt
import imageio

def get_flag(input_data):
    flag = np.array(imageio.imread('/home/b00177274/Documents/GIT/Cryptohack-Challeges/GENERAL/XOR/flag.png'),dtype = np.int64)
    lemur = np.array(imageio.imread('/home/b00177274/Documents/GIT/Cryptohack-Challeges/GENERAL/XOR/lemur.png'),dtype = np.int64)

    plt.imshow(flag ^ lemur)
    plt.show()

    return None

input_data = None

get_flag(input_data)


#Solution
#The code reads two images (flag.png and lemur.png) using the imageio.imread() function, and converts them into NumPy arrays of type np.int64. 
# It then performs a bitwise XOR operation between the two image arrays (flag ^ lemur) and displays the resulting image using matplotlib.pyplot.imshow(). 
# The resulting XORed image is shown in a plot window, and the function get_flag() does not return any value. 
# This could be part of an image-based cryptographic challenge where the XOR operation reveals a hidden flag when applied to two images.