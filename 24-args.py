# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments


# def add(num1,num2):
#     num = num1+ num2
#     return num

# print(add(1,2,3))  # we cant add three argument 

def add1(*args):
    sum = 0
    args = list(args)
    args[0]=0
    for i in args:
        sum += i 
    return sum

print(add1(1,2,3,4,5))