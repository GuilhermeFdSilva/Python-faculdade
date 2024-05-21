# count = 0

# while (count < 5):
#     count += 1
#     print(count)

names = ""

while True:
    text = input("Digite um nome ou '0' para encerrar o programa: ")

    if (text == "0"):
        print("Programa finalizado")
        break
    else:
        names = names + text + "\n"

print("--- Lista de nomes ---")
print(names)

count = 0

while count < 10:
    if (count == 1 or count == 3):
        count += 1
        continue

    print(count)
    count += 1
