import PySimpleGUIQt as sg

def SOMAR(n1, n2):
    resultado = float(n1) + float(n2)
    return resultado

def SUBTRAIR(n1, n2):
    resultado = float(n1) - float(n2)
    return resultado

def MULTIPLICAR(n1, n2):
    resultado = float(n1) * float(n2)
    return resultado

layout = [
    [sg.Text('Calculadora', font=('Arial',18))],
    [sg.Text('Primeiro Número:', size=(15,1)),
     sg.Input(key='n1', size=(15,1))],
    [sg.Text('Segundo Número:', size=(15,1)),
     sg.Input(key='n2', size=(15,1))],
    [sg.Button('SOMAR'),
     sg.Button('SUBTRAIR'),
     sg.Button('MULTIPLICAR')],
    [sg.Text('Resultado:', size=(15,1)),
     sg.Text(key='resultado', size=(20,1))],
    [sg.Button('Limpar'),
     sg.Button('Sair')],
]

janela = sg.Window('Minha Calculadorazinha', layout)

while True:
    evento, valores = janela.Read()
    if evento == 'Sair' or evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Limpar':
        janela['n1'].Update('')
        janela['n2'].Update('')
        janela['resultado'].Update('')
        continue

    try:
        n1 = float(valores['n1'])
        n2 = float(valores['n2'])

        if evento == 'SOMAR':
            janela['resultado'].Update(str(SOMAR(n1, n2)))

        if evento == 'SUBTRAIR':
            janela['resultado'].Update(str(SUBTRAIR(n1, n2)))

        if evento == 'MULTIPLICAR':
            janela['resultado'].Update(str(MULTIPLICAR(n1, n2)))

    except:
        janela['resultado'].Update("Digite apenas números válidos!")

janela.close()