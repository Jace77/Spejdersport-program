# lav et program som gemmer kontaktoplysninger i en text fil test
import PySimpleGUI as sg


layout = [[sg.Text('write your full name:', size=(20, 1)), sg.InputText()],
          [sg.Text('write your email:     ', size=(20, 1)), sg.InputText()],
          [sg.Text('write your phone nr.:', size=(20, 1)), sg.InputText()],
          [sg.Text('write your adress:   ', size=(20, 1)), sg.InputText()],
          [sg.Button('Save'), sg.Button('close')]]

window = sg.Window('Spejdersport', layout, margins=(100, 100))
window.read()

while True:
    event, values = window.read()
    if event == 'close' or event == sg.WINDOW_CLOSED:
        break
    if event == 'Save':
        with open('Brugerfile.txt', 'w') as f:
            f.write('Name: ')
            f.write(values[0])
            f.write('\n')
            f.write('Email: ')
            f.write(values[1])
            f.write('\n')
            f.write('phone nr: ')
            f.write(values[2])
            f.write('\n')
            f.write('Adress: ')
            f.write(values[3])
        break
