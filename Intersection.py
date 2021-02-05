from Point import Point
import math

def calculate_vector(p1, p2, p3):
    x1 = p3.x - p1.x
    y1 = p3.y - p1.y
    x2 = p2.x - p1.x
    y2 = p2.y - p1.y
    return x1*y2 - x2*y1

def check_assignment(p1, p2, p3):
    check_x_axis = min(p1.x, p2.x) <= p3.x and p3.x <= max(p1.x, p2.x)
    check_y_axis = min(p1.y, p2.y) <= p3.y and p3.y <= max(p1.y, p2.y)
    return check_x_axis and check_y_axis

def are_intersecting(A, B, C, D):
    v1 = calculate_vector(C, D, A)
    v2 = calculate_vector(C, D, B)
    v3 = calculate_vector(A, B, C)
    v4 = calculate_vector(A, B, D)

    if(v1*v2 < 0 and v3*v4 < 0):
        return 1
	
    if((v1>0 and v2<0 or v1<0 and v2>0) and (v3>0 and v4<0 or v3<0 and v4>0)):
        return 1
	
    if(v1 == 0 and check_assignment(C, D, A)): return 1
    if(v2 == 0 and check_assignment(C, D, B)): return 1
    if(v3 == 0 and check_assignment(A, B, C)): return 1
    if(v4 == 0 and check_assignment(A, B, D)): return 1
    else: return 0


def get_intersection_point(A,B,C,D):
    t0 = (C.x-A.x)*(D.y-C.y)-(C.y-A.y)*(D.x-C.x)
    t1 =(B.x-A.x)*(D.y-C.y)-(B.y-A.y)*(D.x-C.x)

    if(t0 == 0 and t1 == 0):
        v1 = calculate_vector(C, D, A)
        v2 = calculate_vector(C, D, B)
        v3 = calculate_vector(A, B, C)
        v4 = calculate_vector(A, B, D)

        arr = []
        if(v1 == 0 and check_assignment(C, D, A)): arr.append(A)
        if(v2 == 0 and check_assignment(C, D, B)): arr.append(B)
        if(v3 == 0 and check_assignment(A, B, C)): arr.append(C)
        if(v4 == 0 and check_assignment(A, B, D)): arr.append(D)
        return arr
    try:
        t = t0/t1
        x = A.x +t*(B.x-A.x)
        y = A.y +t*(B.y-A.y)
        return Point(x,y)
    except:
        return None

