class Funcionario:
    def __init__(self, nome, tempo_servico, salario_base):
        self.nome = nome
        self.tempo_servico = tempo_servico
        self.salario_base = salario_base
    def calcular_salario(self):
        return self.salario_base * (1+(0.05 * self.tempo_servico))

class Professor(Funcionario):
    def __init__(self, nome, tempo_servico, salario_base, ch):
        super().__init__(nome, tempo_servico, salario_base)
        self.ch = ch

    def __str__(self):
        return f'{self.nome} {self.tempo_servico} {self.salario_base} {self.ch}'

    def calcular_salario(self):
        return (self.salario_base + (self.ch * 50)) * (1+(0.05 * self.tempo_servico))

class Tecnico(Funcionario):
    def __init__(self, nome, tempo_servico, salario_base, gratificacao):
        super().__init__(nome, tempo_servico, salario_base)
        self.gratificacao = gratificacao

    def calcular_salario(self):
        return (self.salario_base + self.gratificacao) * (1+(0.05 * self.tempo_servico))

    def __str__(self):
        return f'{self.nome} {self.tempo_servico} {self.salario_base} {self.gratificacao}'


roberto = Professor('Roberto', 8, 100000, 40)
joao = Tecnico('João', 25, 5000, 2000)

print(roberto)
print(roberto.calcular_salario())

print(joao)
print(joao.calcular_salario())