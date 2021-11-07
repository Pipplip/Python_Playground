'''
pip install cryptography
'''

# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()
  
# save the key in a file (or local as variable)
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

######## ENCRYPTION ###########

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
  
# using the generated key
fernet = Fernet(key)
  
# opening the original file to encrypt
with open('Test.txt', 'rb') as file:
    original = file.read()
    file.close()
      
# encrypting the file
encrypted = fernet.encrypt(original)
  
# opening the file in write mode and 
# writing the encrypted data
with open('Test_enc.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


######## DECRYPTION ##############
# using the key
#fernet = Fernet(key)
  
# opening the encrypted file
with open('Test_enc.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
    enc_file.close()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('Test_dec.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
    dec_file.close()