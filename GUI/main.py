import PySimpleGUIQt as sg
layout = [
    [sg.Text("Minha primeira interfacezinha")],
    [sg.Button("Sair")],
]
window = sg.Window("Minha primeira janelinha", layout)

while True:
    event, values = window.read()
    if event == "Sair" or event == sg.WINDOW_CLOSED:
        break
window.close()