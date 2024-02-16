

rows= int(input("give me the number of rows"))
columns= int(input("give me the number of columns"))

for i in range(rows):
    for j in range(columns):
        print("@", end="") #printing in same ligne
    print()     