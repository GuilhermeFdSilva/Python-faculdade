a = 5
b = 5
c = 2
d = 1

if (a == b) and (c > d):
    print("A primeira e a segunda expressão retornam 'verdadeiro'")
    
a = 5
b = 2
c = 2
d = 1
if (a == b) or (c > d):
    print("A primeira expressão retornam 'falso', porém a segunda expressão retorna 'verdadeiro'"),
    
a = 5
b = 5
if not (a != b):
    print("A expressão retorna 'falso', porém o operador NOT inverte o resultado")