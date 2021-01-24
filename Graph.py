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

    def setData(self, data):
        self.data = data

    def createLine(self, point1, point2):
        plt.plot([point1.x, point2.x], [point1.y, point2.y], '-k')

    def createPoint(self, point):
        plt.scatter(point.x, point.y)

    def createGraphFromData(self):
        for line in self.data:
            self.createLine(line[0], line[1])

    def intersection(self):
        for line1 in self.data:
            for line2 in self.data:
                if are_intersecting(line1[0], line1[1], line2[0], line2[1]):
                    point = get_intersection_point(line1[0], line1[1], line2[0], line2[1])
                    if point is not None:
                        self.createPoint(point)

    def returnGraph(self):
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        return graphic