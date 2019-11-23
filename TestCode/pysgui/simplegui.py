'''
PySimpleGUI
https://github.com/PySimpleGUI/PySimpleGUI
'''

import PySimpleGUI as sg
# All the stuff inside your window.
layout = [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()] ]
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()