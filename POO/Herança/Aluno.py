class aluno:
    def __init__(self,nome,nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f'Nome: {self.nome}, Nota: {self.nota}'

class alunoposgraduacao(aluno):
    def __init__(self,nome,nota,formacao):
        super().__init__(nome,nota)
        self.formacao = formacao

    def __str__(self):
        return super().__str__() + (f' Formação: {self.formacao}')

al=alunoposgraduacao("roberto", "8", "dna")

print(al)