            #user input

'''            
name = input("what is your name? : \n ")
print(type(name)) # if u put your name so a sting the result of this = <class 'str'>

age = input("how old are u : \n")
print(type(age)) # u put an int but the type is always str
print("your age is :"+age) # that gives no error cuz u can concatinat strings 
#BUT
#age = age +1 # error cuz type(age)=  <class 'str'> not an int  , so lets do the folowing (as the type cast corse)

age = int(age)
age = age +1 
print(age)
print(type(age)) # see ? now its  an int

'''

#another staff

'''

name=input("what is your name?: ")
age= int(input("how old are u ?: "))
height=float(input("how tall are u ?: "))

print("hello "+name)
print("you are "+str(age)+" years old") #dont forget we must use str() cuz we are concatenating strings 
print("you are "+str(height) +"cm")

'''