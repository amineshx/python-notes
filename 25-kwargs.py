# ** kwargs = parameter that will pack all arguments into a dictionary 
#             useful so that a function can accept a varying amount of keyword argumnets

# def hello(first, last):
#     print("hello "+ first +" "+last)

# hello(first="amine",last="shx")         # cant add a 3rd argument

def hello1(**kwargs):
    #print("hello "+kwargs['first']+" "+kwargs['last'])
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,"",end="")
hello1(first="amine",middle="bimbim",last="shx")