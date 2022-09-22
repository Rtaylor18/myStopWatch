import PySimpleGUI as sg
from time import time

font_def= 'Ubuntu 15'

sg.theme('DarkBlue1')

layout = [[sg.Text('Num Laps:'), sg.Text('',key = '-LAP-')],[sg.Text('time',font = 'Ubuntu 50',justification = 'center', expand_x= True,key = '-OUTPUT-')],
          [sg.Button('Start/Stop', font= font_def), sg.Button('Lap', font=font_def, visible = False)]]

window = sg.Window('Stoppit', layout, element_justification= 'center', size = (200,150))

start_time = 0
active=False
lap_amount = 0
while True:
    event, values = window.read(timeout = 10)

    if event == sg.WIN_CLOSED:
        break


    if event == 'Start/Stop':
        if active:
            #from active to stop
            active = False
            window['Start/Stop'].update('Reset')
            window['Lap'].update(visible = False)
        else:
            #from stop to reset
            if start_time > 0:
                window['-OUTPUT-'].update('0.00')
                window['-LAP-'].update('')
                lap_amount = 0
                start_time = 0
                window['Start/Stop'].update('Start/Stop')
            #from start to active
            else:
                start_time = time()
                active=True
                window['Start/Stop'].update('Stop')
                window['Lap'].update(visible = True)

    if event  == 'Lap':
        lap_amount= lap_amount +1
        window['-LAP-'].update(lap_amount)           

    
    if active:
        elasped_time = round(time() - start_time, 1)
        window['-OUTPUT-'].update(elasped_time)
    
window.close()