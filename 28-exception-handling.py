# exception = events detected during exwcution that interrupt the flow of a program

try:
    numerator = int(input("Entre a number to divide: "))
    denominator = int(input("enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("u cant divide by 0")
except ValueError as e:
    print(e)
    print("enter only numbers pls")
except Exception as e:
    print(e)
    print("something went wrong:( ")
else:
    print(result)
finally:
    print("this will always execute")
