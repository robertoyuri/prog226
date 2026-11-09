# Criar e gravar no arquivo
arquivo = open("file.txt", "w", encoding="utf8")
arquivo.write("Hello World")
arquivo.close()

# Abrir e ler
arquivo = open("file.txt", "r", encoding="utf8")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

#Abrir, ler, gravar
arquivo = open("file.txt", "a", encoding="utf8")
arquivo.write("\n")
arquivo.write("Nova linha")
arquivo.close()

#Salvar Nome;idade
arquivo = open("db.csv", "w", encoding="utf8")
linhas = [
    "ID,Nome;Idade;\n",
    "1;Nicolas;23;\n",
    "2;Nikolas;20;\n",
    "3;Tamires;42;\n",
    "4;Millena;18;\n",
]
arquivo.writelines(linhas)
arquivo.close()

#modificar uma linha
arquivo = open("db.csv", "r", encoding="utf8")
linhas = arquivo.readlines()
arquivo.close()
linha = linhas[3]
linha = linha.split(";")
print(linha[0])
print(linha[1])
print(linha[2])
linhas[3] = str(linha[0])+";"+str(linha[1])+";"+str(19)+";\n"
arquivo = open("db.csv", "w", encoding="utf8")
arquivo.writelines(linhas)
arquivo.close()