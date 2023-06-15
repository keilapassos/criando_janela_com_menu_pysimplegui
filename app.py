import PySimpleGUI as sg

# tema da janela
sg.theme('Reddit')

# layout do menu
menu_layout = [
    ['File', ['New File', 'Save', 'Save As']],  # [abamenu, [item1, item2...]]
    # [abamenu, [item[subitem...]]]
    ['Edit', ['Size', ['Change Resolution', 'Change Height', 'Change Width']]],
    ['About', ['About Author']]
]

# layout completo
full_layout = [
    [sg.Menu(menu_layout)],  # chama o layout menu
    [sg.Text('Bem-vindo a este aplicativo!')],  # texto
    [sg.Output(size=(40, 15))]  # texto de saída / output
]

# nome da janela e chamada do layout completo
window = sg.Window('Desafio - Menu', layout=full_layout)

# eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # se a janela for fechada a aplicação termina
        break
    elif event == 'About Author':  # ao clicar em about author acontece o output com o texto da autora
        print('Criado por Keila em 15 de Junho de 2023')
