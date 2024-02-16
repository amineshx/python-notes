import os

# file
# path = "34-delete-a-file.txt"
# try:
#     os.remove(path)
# except FileNotFoundError :
#     print("file doesn't exist")

# folder empty 
    
# path = "empty_folder"  #folder to delete's path

# try:
#     os.rmdir(path)
# except FileNotFoundError:
#     print("that folder or file was not found")
# except PermissionError:
#     print("you do not have permission to delete that")
# except OSError:
#     print("you cant delete that using that function")
# else :
#     print(path+" was deleted")



# not empty folder
import shutil
path = 'empty_folder' # folder to delete path

try:
    shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("that folder or file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cant delete that using that function")
else :
    print(path+" was deleted")