import PySimpleGUIQt as sg

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def salvar(self):
        arquivo = open('aluno.txt', 'w')
        arquivo.write(self.nome + "\n")
        arquivo.write(self.matricula)
        arquivo.close()

    def recuperar(self):
        arquivo = open('aluno.txt', 'r')
        self.nome = arquivo.readline().strip()
        self.matricula = arquivo.readline().strip()
        arquivo.close()

layout = [
    [sg.Text('CADASTRO DE ALUNO', font=('Arial', 16))],
    [sg.Text('Nome', font=('Arial', 12)),
     sg.Input(key='nome')],
    [sg.Text('Matricula', font=('Arial', 12)),
     sg.Input(key='matricula')],
    [sg.Button('Salvar'), sg.Button('Recuperar'),
     sg.Button('Limpar'), sg.Button('Sair')],
    [sg.Text('', key='msg', font=('Arial', 14))]
]
janela = sg.Window('Aluno', layout)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED or eventos == "Sair":
        break

    if eventos == "Salvar":
        aluno = Aluno(valores['nome'], valores['matricula'])
        aluno.salvar()
        janela['msg'].Update('Aluno foi salvo!')

    if eventos == "Recuperar":
        aluno = Aluno('', '')
        aluno.recuperar()
        janela['nome'].Update(aluno.nome)
        janela['matricula'].Update(aluno.matricula)
        janela['msg'].Update('Dados atualizados.')

    if eventos == "Limpar":
        janela['nome'].Update('')
        janela['matricula'].Update('')
        janela['msg'].Update('')

janela.close()