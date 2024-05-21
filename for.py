#sum = 0

# for i in (0, 1, 2, 3, 4):
#     sum += 3
#     print(sum)

# for i in "ABCDEFG":
#     print(i)

# for i in range(0, 5, 1):
#     sum += 3
#     print(sum)

# for i in range(0, 15, 2):
#     print(i)

multiplesCount = 0

for i in range(1, 30):
    if (i % 3 == 0):
        multiplesCount += 1
        print(i)

print("A quantidade de números divisíveis por 3 entre 1 e 30 é", multiplesCount)
