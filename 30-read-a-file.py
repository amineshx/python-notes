

# with open('30-read-a-file.txt') as file:
#     print(file.read())

# print(file.closed)

try :
    with open('30-read-a-file.tx') as file:
        print(file.read())
except Exception as e :
    print(e)
    print("file doesn't exist")