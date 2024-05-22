# myList = [1,  2, 3, 4, 5]

# myList2 = [1, "Silva", 4.5]

# myList2.append("Guilherme")
# myList2.append(24)
# myList2.append(1.69)

nameList = []

while True: 
    name = input("Digite um nome: ")

    nameList.append(name)

    persist = input("Deseja continuar? Digite S ou N ")

    if (persist.upper() == "N"):
        break

# print(nameList)

for name in nameList:
    print(name)
