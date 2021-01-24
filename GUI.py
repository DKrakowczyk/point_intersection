import PySimpleGUI as sg

class GUI:

    def __init__(self):
        self.title = []
        self.layout = []
        self.frame_layout = []
        self.pointsColumn = []
        self.graphColumn = []
        self.primaryWindow = []

    def render(self, graph):
        self.setTitle()
        self.setFrameLayout()
        self.setPointsColumn()
        self.setGraphColumn(graph)
        self.setPrimaryWindow()
        self.setLayout()
        self.renderWindow()

    def setTitle(self):
        self.title = [
            [sg.Text("Intersection", justification='center', size=(100, 1), font=('Arial', 16))]
        ]

    def setFrameLayout(self):
        self.frame_layout = [
            [sg.Text('Points in format x,y', size=(30, 1), justification='center')],
            [sg.Text('Point 1', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 2', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 3', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 4', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 5', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 6', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 7', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 8', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 9', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
            [sg.Text('Point 10', size=(10, 1), justification='center'), sg.Text("( X:", pad=(0, 0)),
             sg.InputText(size=(4, 1), key='-IN-', enable_events=True),
             sg.Text("Y:", pad=(0, 0)), sg.InputText(size=(4, 1)), sg.Text(")", pad=(0, 0))],
        ]

    def setPrimaryWindow(self):
        self.primaryWindow = [
            [sg.Column(self.pointsColumn), sg.VSeparator(), sg.Column(self.graphColumn)]
        ]

    def setPointsColumn(self):
        self.pointsColumn = [
            [
                sg.Frame('Points', self.frame_layout, font='Any 14')],
            [sg.Button('Update', size=(20, 1)), sg.Button('Clear', size=(9, 1))]
        ]

    def setGraphColumn(self, graph):
        self.graphColumn = [
            [sg.Image(data=graph, key="-IMAGE-")],
        ]

    def setLayout(self):
        self.layout = [
        [sg.Column(self.title)],
        [sg.HSeparator()],
        [sg.Column(self.primaryWindow)]
        ]

    def renderWindow(self):
        window = sg.Window('Intersection', self.layout, size=(750, 450))
        # Event Loop to process "events" and get the "values" of the inputs
        while True:  # Event Loop
            event, values = window.read()
            if event in (None, 'Exit'):
                break
            if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in ('-0123456789.'):
                window['-IN-'].update(values['-IN-'][:-1])
        window.close()