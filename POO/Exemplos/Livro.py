#Crie uma classe Livro contendo titulo, autor e numero_paginas. Crie um método que exiba uma descrição completa do livro.
class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def descricao(self):
        print(f'O livro: {self.titulo} do(a) {self.autor} com {self.numero_paginas} páginas.')


l1 = Livro("Cronicas da Terra", "Tamires", "75")
l1.descricao()