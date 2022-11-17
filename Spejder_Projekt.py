# lav et program som gemmer kontaktoplysninger i en text fil test
# if values.strip(): this line of code in memoriam of strip
# Z is a impostor
import PySimpleGUI as sg


layout = [[sg.Text('write your full name:', size=(20, 1)), sg.InputText()],
          [sg.Text('write your email:     ', size=(20, 1)), sg.InputText()],
          [sg.Text('write your phone nr.:', size=(20, 1)), sg.InputText()],
          [sg.Text('write your adress:   ', size=(20, 1)), sg.InputText()],
          [sg.Text("strip", size=(50, 1), key='output', text_color="red")],
          [sg.Button('Save'), sg.Button('close')]]

window = sg.Window('Spejdersport', layout, margins=(100, 100))
window.read()

while True:
    event, values = window.read()
    if event == 'close' or event == sg.WINDOW_CLOSED:
        break
    if event == 'Save':
        if all(not y for y in values):
            print("your fields were not empty good job!")
        else:
            print("one of your input fields are empty")
            window.Element("output").update("one of your input fields are empty")
            continue
        if all(x.isspace() or x.isalpha() for x in values[0]):
            print("correct name")
        else:
            print("incorrect name")
            window.Element("output").update("incorrect name")
            continue
        if "@gmail.com" in values[1]:
            print("correct email")
        else:
            print("incorrect email")
            window.Element("output").update("incorrect email")
            continue
        if len(values[2]) == 8 and values[2].isnumeric():
            print("correct phone number")
        else:
            print("incorrect phone number")
            window.Element("output").update("incorrect phone number")
            continue
        if all(x.isalnum() or x.isnumeric() for x in values[3]):
            print("correct adress")
        else:
            print("incorrect adress")
            window.Element("output").update("incorrect adress")
            continue
        print(len(values))
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
