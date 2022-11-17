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
        if all(x.isspace or x.isalpha for x in values[0]):
            print("correct name")
        else:
            print("incorrect name")
        if "@gmail.com" in values[1]:
            print("correct email")
        else:
            print("incorrect email")
        if len(values[2]) == 8:
            print("correct phone number")
        else:
            print("incorrect phone number")
        if all(x.isalnum or x.isnumeric for x in values[3]):
            print("correct adress")
        else:
            print("incorrect adress")
        if all(len(str(y)) > 1 for y in values):
            print("your fields were not empty good job!")
        else:
            print("one of your input fields are empty")
        with open('Brugerfile.txt', 'a') as f:
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
