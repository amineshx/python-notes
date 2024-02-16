#keyword argument = arguments preceded by an identifier when we pass them to a function 
#                   the order of the arguments doesn't matter, unlike positional arguments
#                   python knows the names of the arguments that our function receives

       #when order matters 
 
''' 
       
def hello(first,middle,last):
    print("hello "+first+" "+middle+" "+last)
           
hello("amine","shx","cv")           
       
'''
       
        #when order doesn't matter

'''

def hello(first,middle,last):
    print("hello "+first+" "+middle+" "+last)
           
hello(middle="shx",last="cv",first="amine")        

'''