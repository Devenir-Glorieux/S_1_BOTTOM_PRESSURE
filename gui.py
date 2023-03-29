import PySimpleGUI as sg
layout = [
    [sg.Text('Глубина перфорации TVD (м)     '), sg.InputText(size=(8, 0.5))
     ],
    [sg.Text('Диаметр лифта НКТ (мм)            '), sg.InputText(size=(8, 0.5))
     ],
    [sg.Text('Длина лифта НКТ (м)                  '), sg.InputText(size=(8, 0.5))
     ],
    [sg.Text('Расход/дебет (м3/мин)               '), sg.InputText(size=(8, 0.5)), sg.Checkbox ('Нагнетательная')
     ],
    [sg.Text('Плотность флюида (кг/м3)           '), sg.InputText(size=(8, 0.5)), sg.Checkbox ('Ньютоновская жидкость')
     ],
    [sg.Text('Значения вискозиметра 300rpm  '), sg.InputText(size=(8, 0.5))
     ],
    [sg.Text('Значения вискозиметра 3rpm      '), sg.InputText(size=(8, 0.5)), 
     ],
    [sg.Output(size=(88, 2))],
    [sg.Submit('Расчет')]
]
window = sg.Window('Расчет забойного давления', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break



