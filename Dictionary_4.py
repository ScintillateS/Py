thisdict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}

print(thisdict)
print(thisdict["Brand"])
print(thisdict.get("Model"))
thisdict["Year"]= 2009
print(thisdict["Year"])

for values in thisdict:
    print(values)
    print(thisdict[values])
for x,y in thisdict.items():
    print(x,y)
