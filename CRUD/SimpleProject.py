from pathlib import Path


def showFile():
    path = Path("./CRUD")
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createFile():

 try:
    showFile()
    name = input("please tell your file name : -")
    p = Path(f"./CRUD/{name}")
    if not p.exists():
     with open(p, "w") as fs:

        data = input("What you want to write in this file :- ")
        fs.write(data)

     print(F"FILE CREATED SUCCESSFULLY")

    else:
     print(F"FILE CREATED SUCCESSFULLY")

 except Exception as err:
    print(f"An error occured as {err}")


def readFile():
    print("readed file")

def updateFile():
    showFile()
    name = input("Enter the file you wanna update :- ")
    p = Path(name)
    if p.exists() and p.is_file():
       print("Press 1 for changing the name of your file :- ")
       print("Press 2 for overwriting the data of your file :- ")
       print("Press 3 for appending some content in your file :- ")

       res = int(input("tell your responce :- "))

       if res == 1:
          name2 = input("tell your new file name :- ")
          p2 = Path(name2)
          p.rename(p2)

          if res == 2:
           with open(p, 'w') as fs:
             data = input("tell what you want to write this is overwrite the file")
             fs.write(data)
            
           if res == 3:
              
          

def deleteFile():
    print("delete file")



print("Press 1 for Creating the file")
print("Press 2 for Reading the file")
print("Press 3 for Updating the file")
print("Press 4 for Deleting the file")

inputTaker = int(input("Please enter your input : "))

if(inputTaker == 1):
    showFile()
    createFile()
elif(inputTaker == 2):
    showFile()
    readFile()
elif(inputTaker == 3):
    showFile()
    updateFile()
elif(inputTaker == 4):
    showFile()
    deleteFile()
else:
    print("invalid input")




