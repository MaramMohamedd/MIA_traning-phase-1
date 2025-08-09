class codec:
    def __init__(self):
        print("welcom to our system : ")

    def encode(self , list_command):
        encoded = ""
        for i in list_command:
            index = len(i)
            encoded += f"{index}{":"}{i}" #stacking the string with its length and separator
        print('Encoded Done Succefully !')
        return encoded 
        
    def decode(self , encoded):
        decoded = []
        index = 0 #used slicing 
        while index < len(encoded):
              separator_index = encoded.find( ":" , index )# will return the first separator index
              if separator_index == -1 : #means not found there is no strings 
                  break 
              lengthh = int(encoded[index:separator_index])
              start = separator_index+1#means come after the separator to get the string itself 
              end = start+lengthh 
              stringgg = encoded[start:end] #the end is not included 
              decoded.append(stringgg)
              index = end 
        print("Decoded done successfully")
        return decoded


string = []
n = int(input("Enter the number of strings you want to encode : "))
for i in range(n):
    x = input(f"Input string {(i+1)}\n")
    string.append(x)



#about my trials 
# firstly i tried to put the length of the string only with out usint a separator a
# and this has made a problem with me with 1- string with empty strings ,2- spaces 
#then after searching i found out that the separator was much more better 
#what i have learned #how to search in a string ,  how to use slicing 

system = codec()
print("---------------------")
encodedstr = system.encode(string)
print(encodedstr)
print('-'*50)
decodedstr = system.decode(encodedstr)
print ("here is your decoded string : \n")
print(decodedstr)

# s = "3aml03mar"
# #    012345678
# index = 0 
# print(s[index+1 : index+int(s[index])+1])
# index += int(s[index])+1
# print(index)