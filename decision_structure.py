a = int(input("Nota A1: "))
b = int(input("Nota A2: "))
attendance_rate = float(input("Qual a porcentagem de frequência do aluno? "))

grade = a + b

# if (grade > 6):
#     print("Aluno aprovado!")

# if (grade > 6):
#     print("Aluno aprovado!")
# else:
#     print("Aluno reprovado!")

# if (grade > 6):
#     print("Aluno aprovado!")
# elif (grade > 2):
#     print("Aluno deve realizar a prova de recuperação!")
# else:
#     print("Aluno reprovado!")

if (attendance_rate > 75):
    if (grade > 6):
        print("Aluno aprovado!")
    elif (grade > 2):
        print("Aluno deve realizar a prova de recuperação!")
    else:
        print("Aluno reprovado!")
else:
    print("Aluno reprovado!")
