
# text = "this is a text\nthis is some text\n have a good one!\n"

# with open('31-write-a-file.txt','w') as file:
#     file.write(text)

text = "have a nice day! see ya"

with open('31-write-a-file.txt','a') as file:
    file.write(text)