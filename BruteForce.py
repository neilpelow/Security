from Crypto.Cipher import AES
import hashlib
import sys
import binascii

def decrypt(ciphertext,key, mode):
    	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

myFile = open('/Users/neilpelow/dictionary.txt', 'rw')  #Open dictionary file for reading

for line in myFile:     #Iterate through each line in the file 
        #print(line),    #Print each line 
        key = line
        ciphertext = "qϮ�%2Q���6�#��\�j\"�����ՌD��`������ª���~p���    #�$~�A}jx�JK9"
        hextext = decrypt(ciphertext, key, AES.MODE_ECB)
        hextext.strip("0")
        plaintext = hextext.decode("hex")
        print(plaintext)

myFile.close()
