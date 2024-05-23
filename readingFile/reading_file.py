# data = open("readingFile/data.txt", "r");

# content = data.read();

# print(content);

# data.close();

# data = open("readingFile/data.txt", "w");

# data.write("\nEscrevendo no arquivo de texto!\n");

# data.close();

# data = open("readingFile/data.txt", "r");

# line = data.readline();

# print(line);

data = open("readingFile/data.txt", "r+");

content = data.read();

print(content);

data.write("\nOla, mundo!\n");

data.close();
