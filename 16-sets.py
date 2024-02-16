# set = collection which is unordered , unindexed , no duplicate values

utensils = {"fork", "spoon" , "knife"}
dishes={"bowl","plate", "cup","knife"}

dinner_table=utensils.union(dishes)

print(utensils.difference(dishes)) # this prints what utensils have and dishes doesn't
print(utensils.intersection(dishes)) # this prints what this two sets have in communt
utensils.update(dishes)
utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
for x in utensils:
    print(x)