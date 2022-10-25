#characters  have less freqency have more space
#charecters  have more frequency have less space

#Datastructures for huffman coding - Compressing part
#1)Hashmap for storing the frequency of the elements 
#2) Tree for tree like structure
#3) min heap for finding minimum frequency element
import heapq
import os


class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None
        
    def __it__(self,other):
        return self.freq < other.freq
    
    def __eq__(self,other):
        return self.freq == other.freq
    

class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        self.__heap=[]
        self.__codes={}
        self.__reverseCodes={}
        
    
    def __make_frequency_dict(self,text):
        
        freq_dict={}
        for char in text:
            if char not in freq_dict:
                freq_dict[char]=0
            freq_dict[char]+=1
        return freq_dict
    
    def __buildHeap(self,freq_dict):
        for key in freq_dict:
            frequency=freq_dict[key]
            binaryTreeNode=BinaryTreeNode(key,frequency)
            heapq.heappush(self.__heap,binaryTreeNode)
    
    def __buildTree(self):
        while (len(self.__haeap)>1 ):
            binary_tree_node_1=heapq.heappop(self.___heap) 
            binary_tree_node_2=heapq.heappop(self.__heap)
            
            freq_sum=binary_tree_node_1.freq +binary_tree_node_2.freq
            newNode=BinaryTreeNode(None,freq_sum)
            newNode.left=binary_tree_node_1
            newNode.right=binary_tree_node_2
            heapq.heappush(self.__heap,newNode)
        return 
        
    def __buildCodesHelper(self,root,curr_bits):
        
        if root ==None:
            return 
        if root.value is not None:
            self.__codes[root.value]=curr_bits
            self.__reverseCodes[curr_bits]=root.value
            return
        
        self.__buildCodesHelper(root.left,curr_bits+"0")    
        self.__buildCodesHelper(root.right,curr_bits+"1")
        
    def __buildCodes(self):
        root=heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")
        
    def __getEncodedText(self,text):
        encoded_text=""
        
        for char in text  :
            encoded_text+= self.__codes [char]
        return encoded_text
    
    def __getPaddedEncodedText(self,encoded_text):
        
        padded_amount=8-(len(encoded_text)%8)
        for i in range(padded_amount):
            encoded_text+='0'
        
        padded_info ="{0:08b}".format(padded_amount)
        padded_encoded_text=padded_info+encoded_text

        return padded_encoded_text        
    def __getBytesArray(self,padded_encoded_text):
        array=[]
        for i in range(0,len(padded_encoded_text),8):
            byte=padded_encoded_text[i:i+8]
            array.append(int(byte,2))
        return array
            
                
    def compress(self):
        #get file from path
        #read text file
        file_name,file_extension=os.path.splitext(self.path)
        output_path=file_name+".bin"
        
        with open(self.path,'r+') as file,open(output_path,'wb') as output:

        #make frequency dictionary using text
            text=file.read()
            text=text.rstrip()
            freq_dict=self.__make_frequency_dict(text)
            self.__buildHeap(freq_dict) #constructing the heap for intial

            #constuct the heap from frequencey dictionay
            #construct the binary tree from heap
            self.__buildTree()
            
            #construct the codes from binary tree
            self.__buildCodes()
            
            #Creating the encoded text using the codes
            encoded_text =self.__getEncodedText(text)
            
            #put this  encoded text into the binary file 
            
            #pad this encoded text
        
            padded_encoded_text=self.__getPaddedEncodedText(text) 
            bytes_array=self.__getBytesArray(padded_encoded_text)
            #return this binary file as output
            final_bytes=bytes(bytes_array)
            output.write(final_bytes)
        print("Compressed")
        return output_path
    def __removePadding(self,text):
        padded_info=text[:8]
        extra_padding=int(padded_info,2)
        
        text=text[8:]
        text_after_paddding_removed= text[:-1*extra_padding]
        return text_after_paddding_removed
        
    def __decodeText(self,text):
        decoded_text=""
        current_bit=""
        
        for bit in text:
            current_bit+= bit
            if current_bit in self.__reverseCodes:
                character=self.__reverseCodes[current_bit]
                decoded_text+= character
                current_bit=""
        return decoded_text
        
    def decompress(self,input_path):
        filename,file_extension=os.path.splitext(self.path)
        output_path=filename+"decompressed"+".txt"
        
        with open (input_path,'rb' ) as file,open (output_path,'w' ) as output:
            bit_string=""
            byte=file.read(1)
            while byte:
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,'0')
                bit_string+= bits
                byte=file.read(1)
            
            actual_text=self.__removePadding(bit_string)
            decompressed_text=self.__decodeText(actual_text)
            output.write(decompressed_text)
        
        
        #return this binary file as output 
  
path=r'C:\Users\harisn\Documents\Ds\Git\Ds_algo\Ds_algo\Milestones\mileStone4\HuffHan_coding\Compress.txt'
h=HuffmanCoding(path)
output_path=h.compress()
h.decompress(output_path)