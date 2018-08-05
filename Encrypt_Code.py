# ////Author: P Vinay krishna//////////////

# Steps Included
#  1. Generate a Secret Key
#  2. Encrypt the Text-File with Secret key
#  3. Encrypt the Secret key with RSA Public key
#  4. Save the encrypted Text to files.

# Methods Used:
# 1. encryptTextFileandFernetKey():
# 2. WriteToFile():



# ////  import necessary libraries/////
from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet

#  Give the path to encrypt the textfile
path="C:\\Users\\vpanampilly\\Desktop\\FileEncryption\\Checks.txt"
key=Fernet.generate_key()
# print(key)
cipher_suite=Fernet(key)
private_key=RSA.generate(1024)
public_key = private_key.publickey()

#  Write the key to  file
with open("privKey.pvt",'wb') as pb:
    pb.write(private_key.exportKey())

def encryptTextFileandFernetKey():
    lists=[]
#encrypt the fernet key and save to a file
    encryptFernet=public_key.encrypt(key,None)
    print(type(encryptFernet))
    
    with open("FernetKey.txt","wb") as fp:
        for i in encryptFernet:
            fp.write(i)
    fp.close()
    with open(path) as p:
        while(True):
            line=p.readline()
            if(line==""):
                break
            cipher_text=cipher_suite.encrypt(line.encode())
            cipher_text = str(cipher_text)
            cipher_text = cipher_text[2:-1]
            lists.append(str(cipher_text))
    return lists

# encrypt the textfile and save to a file
def writeToFile():
    with open("maxs.txt","w") as ds:
        for i in encryptTextFileandFernetKey():
            ds.write(str(i)+"NVIDIA")
    ds.close()
    
# call the writeToFile method
obj=writeToFile()

# we should get 
# 1.Encrypted Fernet key as fernetKey
# 2. Encrypted TextFile as maxs.txt
