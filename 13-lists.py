

food = ["pizza","hamberger","hotdog","spaghetti"]

food[0]="sushi"
food.append("ice cream") #adding an elemnt to a list
food.remove("hotdog") #removing an element
food.pop() #removing the last element
food.insert(0,"cake") #inserting an element to the list with an index
food.sort() #will sort the list alphabitcaly 
food.clear() #removing all the element 

for x in food :
    print(x)