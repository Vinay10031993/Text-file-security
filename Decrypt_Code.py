#  Steps Included:
#  1. Inorder to use this script, please make sure FernetKey.txt and PrivKey.pvt exists in the directory
#  2. Decrypt the EncryptedKey in the FernetKey.txt 
#  3. Using the decryptedKey, decrypt the encrypted textfile and store the result to a dictionary
#  4. Create another dictionary, which consitutes checksum of all the files in a folder.
#  5. Compare all the checksums of the dictofItems() with dictofEncryptedText(). if all returns true continue, else return False.

#  Include Necessary Libraries
import Crypto
import hashlib, os, sys
import inspect, os.path
from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet

# get the privKey
with open('privKey.pvt', 'r') as pvt_file:
    pvt_key = RSA.importKey(pvt_file.read())
    
# get the secret key
with open("FernetKey.txt",'rb') as v:
    secretkey=pvt_key.decrypt(v.read())
    
cipher_suite=Fernet(secretkey)

dictsOfItems={}
#  dictionary to store the checksums from the excrypted text.
dictOfEncryptedtxt={}

#  Give the path to get the checksums of files in folder
Folder="C:/Users/vpanampilly/Desktop/checksm"

#  Get SHA1-Checksum of all the files in the directory where this script is made to run.
def checksumOfFiles():
    for root,dirs,files in os.walk(Folder,topdown=True):
        for name in files:
            FileName=os.path.join(root,name)
            with open(str(FileName),'rb') as f:
                buff=f.read()
                dictsOfItems[name]=hashlib.sha1(buff).hexdigest()
    return dictsOfItems

#  This method will save the decrypted text to a dictionary
def checksumFromtxt():
    with open("C:\\Users\\vpanampilly\\Desktop\\FileEncryption\\maxs.txt") as fp:
        lists=fp.read().split("NVIDIA")
        lists.pop()
    asd=[]
    for i in lists:
        cipher_text = cipher_suite.decrypt(i.encode("utf-8"))
        asd.append(cipher_text.decode('utf8')[0:-1])
    for ls in asd:
        if ls!="":
            var=ls.split(":")
            dictOfEncryptedtxt[var[0]]=var[1]
#     print(dictOfEncryptedtxt)
            
#  this method will compare the checksums from both the dictionaries            
def checkForEquality():
    for i,j in dictsOfItems.items():
        if i in dictsOfItems:
            if j==dictOfEncryptedtxt[i]:
                print(True)
            else:
                print(i+" : "+dictOfEncryptedtxt.get(i)+"   "+i+" : "+dictsOfItems.get(i))
                print(False)
                break
#         else:
#             print(False)


obj=checksumOfFiles()
obj=checksumFromtxt()
obj=checkForEquality()
