import PySimpleGUI as sg
from Point import Point
from Graph import Graph

class GUI:

    def __init__(self):
        self.title = []
        self.layout = []
        self.frame_layout = []
        self.pointsColumn = []
        self.graphColumn = []
        self.primaryWindow = []

    def render(self):
        self.setTitle()
        self.setFrameLayout()
        self.setPointsColumn()
        self.setGraphColumn(None)
        self.setPrimaryWindow()
        self.setLayout()
        self.renderWindow()

    def setTitle(self):
        self.title = [
            [sg.Text("Intersection", justification='center', size=(100, 1), font=('Arial', 16))]
        ]

    def setFrameLayout(self):
        self.frame_layout = []
        for i in range(1, 11):
            row = [sg.Text(f'Line {i} ->', size=(8, 1), justification='center', pad=(0,4)),
                   sg.Text('Point 1', justification='center', pad=(0,4)),
                   sg.Text("( X:", pad=(0, 4)),
             sg.InputText(size=(4, 1), key=f'-IN-p{i}_1', enable_events=True, pad=(0,4)),
             sg.Text("Y:", pad=(0, 4)),
                   sg.InputText(size=(4, 1), key=f'-IN-p{i}_2', enable_events=True, pad=(0,4)),
                   sg.Text(")", pad=(0, 4)),
             sg.Text('Point 2', size=(8, 1), justification='center', pad=(0,4)),
                   sg.Text("( X:", pad=(0, 4)),
             sg.InputText(size=(4, 1), key=f'-IN-p{i}_3', enable_events=True, pad=(0,4)),
             sg.Text("Y:", pad=(0, 4)),
                   sg.InputText(size=(4, 1), key=f'-IN-p{i}_4', enable_events=True, pad=(0,4)),
             sg.Text(")", pad=(0, 4))]
            self.frame_layout.append(row)


    def setPrimaryWindow(self):
        self.primaryWindow = [
            [sg.Column(self.pointsColumn, pad=(0, 20)), sg.VSeparator(), sg.Column(self.graphColumn)]
        ]

    def setPointsColumn(self):
        self.pointsColumn = [
            [sg.Frame('Points', self.frame_layout, font='Any 14')],
            [sg.Button('Update', size=(20, 1), key="Update", enable_events=True),
             sg.Button('Clear', size=(9, 1), key="Clear", enable_events=True)],
            [sg.Button('Example', size=(20,1), key="Example", enable_events=True)]
        ]

    def setGraphColumn(self, graph):
        self.graphColumn = [
            [sg.Image(data=graph, key="-IMAGE-", size=(250, 250))],
        ]

    def setLayout(self):
        self.layout = [
        [sg.Column(self.title)],
        [sg.HSeparator()],
        [sg.Column(self.primaryWindow)]
        ]

    def renderWindow(self):
        window = sg.Window('Intersection', self.layout, size=(900, 500))
        # Event Loop to process "events" and get the "values" of the inputs
        while True:  # Event Loop
            event, values = window.read()
            if event in (None, 'Exit'):
                break
            if '-IN-' in event:
                if values[event] and values[event][-1] not in ('-0123456789.'):
                    window[event].update(values[event][:-1])
            if event == "Example":
                p1 = Point(1, 2); p2 = Point(2, 3)
                p3 = Point(6, 1); p4 = Point(2, 1)
                p5 = Point(3, 9); p6 = Point(4, 4)
                p7 = Point(5, 2); p8 = Point(2, 7)
                p9 = Point(0, 0); p10 = Point(1, 4)
                p11 = Point(4, 0); p12 = Point(6, 6)
                p13 = Point(0, 9); p14 = Point(4, 2)
                p15 = Point(2, 0); p16 = Point(4, 6)
                p17 = Point(8, 2); p18 = Point(1, 9)
                p19 = Point(2, 8); p20 = Point(4, 8)
                data = [(p1, p2), (p3, p4), (p5, p6), (p7, p8), (p9, p10), (p11, p12), (p13, p14), (p15, p16),
                        (p17, p18), (p19, p20)]
                j = 0
                for i in range(1, 11):
                    window.find_element(f'-IN-p{i}_1').Update(data[j][0].x)
                    window.find_element(f'-IN-p{i}_2').Update(data[j][0].y)
                    window.find_element(f'-IN-p{i}_3').Update(data[j][1].x)
                    window.find_element(f'-IN-p{i}_4').Update(data[j][1].y)
                    j += 1
            if event == "Clear":
                for i in range(1, 11):
                    window.find_element(f'-IN-p{i}_1').Update("")
                    window.find_element(f'-IN-p{i}_2').Update("")
                    window.find_element(f'-IN-p{i}_3').Update("")
                    window.find_element(f'-IN-p{i}_4').Update("")
            if event == "Update":
                points = []
                graph = Graph()
                for i in range(1, 11):
                    p01 = values[f'-IN-p{i}_1']
                    p02 = values[f'-IN-p{i}_2']
                    p03 = values[f'-IN-p{i}_3']
                    p04 = values[f'-IN-p{i}_4']
                    if p01 != "" and p02 != "" and p03 != "" and p04 != "":
                        point1 = Point(float(p01), float(p02))
                        point2 = Point(float(p03), float(p04))
                        points.append((point1, point2))
                if points:
                    graph.setData(points)
                    graph.createGraphFromData()
                    graph.intersection()
                    viewGraph = graph.returnGraph()
                    window.find_element('-IMAGE-').Update(data=viewGraph)
                else:
                    window.find_element('-IMAGE-').Update(data=None)

        window.close()