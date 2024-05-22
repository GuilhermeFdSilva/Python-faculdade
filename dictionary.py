myDictionary = {"name" : "Guilherme", "age" : 23}

print(myDictionary["name"])

myDictionary["age"] = 24

print(myDictionary["age"])

myDictionary["email"] = "gui.franca@email.com"

print(myDictionary["email"])

myDictionary.popitem()

print(myDictionary)

myDictionary.pop("name")

print(myDictionary)

del myDictionary
