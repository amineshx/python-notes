import os

# source = "../33-move-a-file.txt"
# destination = os.path.expanduser('~/Desktop/py-code-bro/33-move-a-file.txt')


# try:
#     if os.path.exists(destination):
#         print("file already exists")
#     else:
#         os.replace(source,destination)
#         print(source+ " was moved")
# except FileNotFoundError :
#     print(source+" was not found")


source = '../33-move-a-file'
destination = os.path.expanduser('~/Desktop/py-code-bro/33-move-a-file')

try:
    if os.path.exists(destination):
        print("folder already there")
    else:
        os.replace(source,destination)
        print(source+ " was moved")
except FileNotFoundError:
    print(source+" was not found")