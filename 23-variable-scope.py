# scope = the region that a variable is recognized 
#       A variable is only available from inside the region it is created 
#       A global and locally scoped versions of a variable can be created

# L = local E = enclosing G = Global B= Built-in

name = "bambam"  #global scope (available only inside & outside function)

def display_name():
    #name = "bimbim"      # local scope (available only inside this function)
    print(name)


display_name()
print(name)