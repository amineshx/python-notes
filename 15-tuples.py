#tuple = collection which is order and unchangeable used to group together related data

student= ("amine",22,"male")

print(student.count("amine")) #count is how many time does that element apire in the tuple 
print(student.index("male")) #printing the index

for x in student:
    print(x)
    
if "aine" in student:
    print("yes")
else:
    print("no")    