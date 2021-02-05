import base64
from Point import Point
import matplotlib.pyplot as plt
import random
import numpy as np
import io
from Intersection import are_intersecting, get_intersection_point

class Graph:

    def __init__(self):
        plt.figure(figsize=(4, 4), facecolor="#e9ecef")
        plt.subplot(111)
        plt.grid(True)
        self.data = []
        self.gui = []

    def setData(self, data):
        self.data = data

    def setGui(self, gui):
        self.gui = gui
    
    def createLine(self, point1, point2):
        plt.plot([point1.x, point2.x], [point1.y, point2.y], '-k')

    def createOverridingLine(self, point1, point2):
        plt.plot([point1.x, point2.x], [point1.y, point2.y], '-o')

    def createPoint(self, point):
        plt.scatter(point.x, point.y, s=10, marker='o', c='r', zorder=200)

    def createGraphFromData(self):
        for line in self.data:
            self.createLine(line[1], line[2])

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
                                print("Wchodzi tutaj")
                                self.createPoint(point)
                                point_x = point.x
                                point_y = point.y
                                self.gui.addIntersectionValue(f'Znaleziono punkt przecięcia pomiędzy: Linia{line1[0]}, Linia{line2[0]} w punkcie (x:{point_x} y:{point_y})')
                            else:
                                point1_x = point[0].x
                                point1_y = point[0].y
                                point2_x = point[1].x
                                point2_y = point[1].y
                                self.gui.addIntersectionValue(f'Linie: Linia{line1[0]}, Linia{line2[0]} nachodza na siebie, wspolrzedne odcinka: [(x:{point1_x} y:{point1_y}), (x:{point2_x} y:{point2_y})]')
                                self.createOverridingLine(point[0], point[1])
                        
    def returnGraph(self):
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        return graphic