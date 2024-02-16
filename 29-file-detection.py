import os

#path = "C:\\Users\\cakow\\Desktop\\test.txt"

path = "~/Desktop/py-code-bro"
expanded_path = os.path.expanduser(path)
print(expanded_path)
if os.path.exists(expanded_path):
    print("yes")
    if os.path.isfile(expanded_path):
        print("that is a file")
    elif os.path.isdir(expanded_path):
        print("that is a directory")
else:
    print("no")
