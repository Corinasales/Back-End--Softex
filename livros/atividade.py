livros= ["o direito penal", "a vida é bela", "pele negra"]
print(livros)
print(livros[0], "e", livros[2])
livros.append("a garota do lago")
livros.append ("silencio dos inocentes")
print(livros)
livros.insert(1,"duna")
print(livros)
if "silencio dos inocentes" in livros:
    livros.remove("silencio dos inocentes")
    print(livros)
else:
    print("livro não encontrado")
numeros=[1,2,3,3,2,5]
print(numeros.count(2))




