from Point import Point
from Graph import Graph
from GUI import GUI
from Intersection import get_intersection_point, are_intersecting
import matplotlib.pyplot as plt

p1 = Point(1,2); p2 = Point(2,3)
p3 = Point(6,1); p4 = Point(2,1)
p5 = Point(3,9); p6 = Point(4,4)
p7 = Point(5,2); p8 = Point(2,7)
p9 = Point(0,0); p10= Point(1,4)
p11= Point(4,0); p12= Point(6,6)
p13= Point(0,9); p14= Point(4,2)
p15= Point(2,0); p16= Point(4,6)
p17= Point(8,2); p18=Point(1,9)
p19=Point(2, 8); p20=Point(4, 8)
data = [(p1,p2), (p3,p4), (p5,p6), (p7,p8), (p9,p10), (p11,p12), (p13,p14), (p15,p16), (p17,p18), (p19,p20)]


graph = Graph()
graph.setData(data)
graph.createGraphFromData()
graph.intersection()
b = graph.returnGraph()

gui = GUI()
gui.render(b)