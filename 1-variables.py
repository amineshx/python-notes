
        #string 
'''
name = "amine"
print("hello"+name)   #printing + concatinating 
print(type(name))     #type of the variable = <class str>

first_name = "Amine"
last_name ="shx"
full_name = first_name +" "+  last_name      #concatinating strings + space between
print (full_name)

'''
        # int data type

'''
age= 21
age= age +1 # incriment the age by one 
print(age) 
print(type(age)) #<class int>
#print("your age is:"+age) # error cuz can only concatenate str (not "int") to str 
print("your age is "+str(age)) # printing age along a string => the result is sting + string
print(type(str(age))) # str() turn a variable to a string 

'''

        # float data type

'''

height= 180.5
print(height)
print(type(height)) # <class float>   
print ("your height is :"+str(height)+" cm")

'''

        #boolean 

'''

smthn = False
print(smthn)
print(type(smthn))    #<class 'bool'>
print("there is smthn ?" +" "+str(smthn))         

'''

       #multiple assignment

'''

#normal assignment 
name = "amine"
age= 22
attractive= True
print(name)    
print(age) 
print(attractive)   

#multiple assignment

name,age,attractive = "shx", 22, True
print(name)    
print(age) 
print(attractive)   

X=Y=Z=A=10
print(X) 
print(Y) 
print(Z) 
print(A)
 
''' 