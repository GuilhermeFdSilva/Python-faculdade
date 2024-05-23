def creat_txt_file(file_name, content):
    try:
        with open("creatingFile/" + file_name, "w") as file:
            file.write(content);
        print(f"O arquivo '{file_name}' foi criado com sucesso!");
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}");

file_name = "my_file.txt";
content = "Meu arquivo criado!";

creat_txt_file(file_name, content);
