
name= ""

while len(name) == 0 :
    name = input("Enter your name ")
print("hello "+name)    

name = None 

while not name :
    name = input("Enter your name ")
    print(type(not name))
    print(name)
    print(not name)
print("hello "+name)    
print(type(None))