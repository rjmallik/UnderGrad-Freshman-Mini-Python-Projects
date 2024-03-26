import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes
class Steganography():
    
    def __init__(self):
        self.text = ""
        self.binary = ""
        self.delimiter = "#"
        self.codec = None
    def encode(self, filein, fileout, message, codec):
        img = cv2.imread(filein)
        print(img) # for debugging
        
        # calculate available bytes
        max_bytes = img.shape[0] * img.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)
        # convert into binary
        if codec == "binary":
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == "caesar":
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == "huffman":
            self.codec = HuffmanCodes(delimiter = self.delimiter)
        binary = self.codec.encode(message)
        
        # check if possible to encode the message
        numOfBytes = ceil(len(binary)//8) + 1 
        if  numOfBytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", numOfBytes) 
            self.text = message 
            self.binary = binary + self.codec.encode(self.delimiter)
            # your code goes here
            # you may create an additional method that modifies the image array
            index = 0
            for i in range(len(img)): 
                for j in range(len(img[i])):
                    for k in range(len(img[i][j])):
                        
                        if self.binary[index] == "1":
                            if img[i][j][k] %2 == 0:
                                img[i][j][k] += 1
                                
                        if self.binary[index] == "0":
                            if img[i][j][k] %2 != 0:
                                img[i][j][k] -=  1
                                
                        index += 1
                        if index == len(self.binary):
                            cv2.imwrite(fileout, img) 
                            return
   
               
    def decode(self, filein, codec):
        img = cv2.imread(filein)
        print(img) # for debugging      

        # convert into text
        check = True
        if codec == "binary":
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == "caesar":
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == "huffman":
            if self.codec == None or self.codec.name != "huffman":
                print("A Huffman tree is not set!")
                check = False

        if check:
            bin_data = ""
            # your code goes here
            # you may create an additional method that extract bits from the image array
            for i in np.nditer(img):
                if i % 2 != 0:
                    bin_data += "1"
                if i %2 == 0:
                    bin_data += "0"
                if self.codec.encode(self.delimiter) in bin_data:
                    break
            self.text = self.codec.decode(bin_data)
            self.binary = bin_data
            return
        
    def print(self):
        if self.text == "":
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)    

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()