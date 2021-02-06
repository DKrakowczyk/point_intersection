import base64
from Point import Point
import matplotlib.pyplot as plt
import random
import numpy as np
import io
from Intersection import are_intersecting, get_intersection_point

class Graph:

    def __init__(self):
        plt.figure(figsize=(8, 6), facecolor="#e9ecef")
        plt.subplot(111)
        plt.grid(True)
        self.data = []
        self.gui = []

    def setData(self, data):
        self.data = data

    def setGui(self, gui):
        self.gui = gui
    
    # Metoda rysująca odcinki
    def createLine(self, point1, point2, label):
        plt.plot([point1.x, point2.x], [point1.y, point2.y], label=f'Ocinek {label}')

    # Metoda rysująca odcinki zawierające się w sobie
    def createOverridingLine(self, point1, point2):
        plt.plot([point1.x, point2.x], [point1.y, point2.y], '-o')

    # Metoda rysująca punkt przecięcia odcinków
    def createPoint(self, point):
        plt.scatter(point.x, point.y, s=15, marker='o', c='r', zorder=200)

    def createGraphFromData(self):
        for line in self.data:
            self.createLine(line[1], line[2], line[0])

    # Główna pętla pozwalająca na obliczanie punktów przecięć odcinków
    def intersection(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if(j > i and (len(self.data) > j)):
                    line1 = self.data[i]
                    line2 = self.data[j]
                    if are_intersecting(line1[1], line1[2], line2[1], line2[2]):
                        point = get_intersection_point(line1[1], line1[2], line2[1], line2[2])
                        print(point)
                        if point is not None:
                            if type(point) == Point and point is not None:
                                self.createPoint(point)
                                point_x = point.x
                                point_y = point.y
                                self.gui.addIntersectionValue(f'Znaleziono punkt przecięcia pomiędzy: Odcinek {line1[0]}, Odcinek {line2[0]} w punkcie (x:{point_x} y:{point_y})')
                            else:
                                point1_x = point[0].x
                                point1_y = point[0].y
                                point2_x = point[1].x
                                point2_y = point[1].y
                                self.gui.addIntersectionValue(f'Linie: Odcinek {line1[0]}, Odcinek {line2[0]} zawieraja sie w sobie, wspolrzedne odcinka: [(x:{point1_x} y:{point1_y}), (x:{point2_x} y:{point2_y})]')
                                self.createOverridingLine(point[0], point[1])
                        
    def returnGraph(self):
        buffer = io.BytesIO()
        plt.legend()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        return graphic