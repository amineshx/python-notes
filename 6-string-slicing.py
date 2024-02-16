# slicing = create a substring by extracting element from another string 
#           indexing[] or slice()
#           [start:stop:step]
      
            #indexing
'''
name = "amine shx"

first_name= name[:5] # [0:5]
last_name= name[6:]  # [6:end]
funky_name = name[::2] # [0:end:2]
reversed_name = name[::-1] #[0:end:-1]


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

'''
        # slice()

website1= "https://google.com"
website2= "https://wikipedia.com"

slice= slice(8,-4)

print(website1[slice])        
print(website2[slice])        