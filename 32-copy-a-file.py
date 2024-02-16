#copyfile()= copies contents of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2()= copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('32-copy-a-file.txt','32-copy-a-file1.txt')   #src,dst