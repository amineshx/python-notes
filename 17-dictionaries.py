# dictionary = A changeable, unordered collection of unique  key:value  pairs
#             fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'china':'Beijing',
            'Russia':'moscow'}

print(capitals['USA']) # printing the value is th dictionary[key]
print(capitals.get('Germany')) # get('germany')= None
print(capitals.keys()) #printing keys
print(capitals.items()) #printing all the dictionary

for key,value in capitals.items():
    print(key,value)
    
    
capitals.update({'Germany':'berlin'})    #adding a new key and value
capitals.update({'USA':'Las Vegas'})    #changing the value
capitals.pop('china') # clearing a pair with china key
capitals.clear() #clearing every thing