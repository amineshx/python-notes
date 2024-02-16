name= "amine shx"

print(len(name)) #length of a string
print(name.find("a")) #printing index of the cracter and index of a = 0 , m=1 , s=6
print(name.capitalize()) # this will only capitalize the first letter result of this is = Amine shx not AMINE SHX
print(name.upper()) # uppercassing the string and result = AMINE SHX
print(name.lower()) # i think u got this one
print(name.isdigit()) # a boolean result checking if the variable is a digit or not 
number = "123"
print(number.isdigit()) # results = True cuz 123 is a digit
print(name.isalpha()) #a boolean result checking if the variable is an alphabatic caracters results = False .......eh ? false why ? cuz there is space in amine shx ...
name1= "amine"
print(name1.isalpha()) # results = True
print(number.isalpha()) # resuts = False
print(name.count("a")) # count how many given caracters in a string so here results = 1
print(name.replace("a","k")) # replacing a in string with k so results = kmine sh
print(name*3) # displaying a variable 3 times its like loop lol 