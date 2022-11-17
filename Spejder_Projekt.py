# lav et program som gemmer kontaktoplysninger i en text fil test
import PySimpleGUI as sg


layout = [[sg.Text('Skriv dit fulde navn:', size=(20, 1)), sg.InputText()],
          [sg.Text('Skriv din email:     ', size=(20, 1)), sg.InputText()],
          [sg.Text('Skriv dit telefon nr:', size=(20, 1)), sg.InputText()],
          [sg.Text('Skriv din adresse:   ', size=(20, 1)), sg.InputText()],
          [sg.Button('Save'), sg.Button('Luk')]]

window = sg.Window('Spejdersport', layout, margins=(100, 100))
window.read()

while True:
    event, values = window.read()
    if event == 'Luk' or event == sg.WINDOW_CLOSED:
        break
    if event == 'Save':
        with open('Brugerfile.txt', 'w') as f:
            f.write('Navn: ')
            f.write(values[0])
            f.write('\n')
            f.write('Email: ')
            f.write(values[1])
            f.write('\n')
            f.write('Tlf nr: ')
            f.write(values[2])
            f.write('\n')
            f.write('Adresse: ')
            f.write(values[3])
        break
