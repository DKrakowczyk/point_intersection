from Point import Point
import math

def calculate_vector(p1, p2, p3):
    x1 = p3.x - p1.x
    y1 = p3.y - p1.y
    x2 = p2.x - p1.x
    y2 = p2.y - p1.y
    return x1*y2 - x2*y1

def round_val(val):
    if(val % 1 >= 0.5):
        return val
    else:
        return val

def check_assigment(p1, p2, p3):
    first_condition = min(p1.x, p2.x) <= p3.x and p3.x <= max(p1.x, p2.x)
    second_condition = min(p1.y, p2.y) <= p3.y and p3.y <= max(p1.y, p2.y)
    return first_condition and second_condition

def are_intersecting(A, B, C, D):
    v1 = calculate_vector(C, D, A)
    v2 = calculate_vector(C, D, B)
    v3 = calculate_vector(A, B, C)
    v4 = calculate_vector(A, B, D)

	# sprawdzenie czy się przecinają - dla niedużych liczb
    if(v1*v2 < 0 and v3*v4 < 0):
        return 1
	
	# sprawdzenie czy się przecinają - dla większych liczb
    if((v1>0 and v2<0 or v1<0 and v2>0) and (v3>0 and v4<0 or v3<0 and v4>0)):
        return 1
	
	# sprawdzenie, czy koniec odcinka leży na drugim
    if(v1 == 0 and check_assigment(C, D, A)): return 1
    if(v2 == 0 and check_assigment(C, D, B)): return 1
    if(v3 == 0 and check_assigment(A, B, C)): return 1
    if(v4 == 0 and check_assigment(A, B, D)): return 1
    else: return 0


def get_intersection_point(A,B,C,D):
    s1_x = B.x - A.x
    s2_x = D.x - C.x
    s1_y = B.y - A.y
    s2_y = D.y - C.y

    t_up = (C.x-A.x)*(D.y-C.y)-(C.y-A.y)*(D.x-C.x)
    t_down =(B.x-A.x)*(D.y-C.y)-(B.y-A.y)*(D.x-C.x)


    if(t_up == 0 and t_down == 0):
        v1 = calculate_vector(C, D, A)
        v2 = calculate_vector(C, D, B)
        v3 = calculate_vector(A, B, C)
        v4 = calculate_vector(A, B, D)

        arr = []
        if(v1 == 0 and check_assigment(C, D, A)): arr.append(A)
        if(v2 == 0 and check_assigment(C, D, B)): arr.append(B)
        if(v3 == 0 and check_assigment(A, B, C)): arr.append(C)
        if(v4 == 0 and check_assigment(A, B, D)): arr.append(D)
        
        for o in arr:
            print(o.x)
        
        return arr
    try:
        
        t = t_up/t_down
        x = A.x +t*(B.x-A.x)
        y = A.y +t*(B.y-A.y)
        return Point(x,y)
        
        # s = (-s1_y * (A.x - C.x) + s1_x * (A.y - C.y)) / (-s2_x * s1_y + s1_x * s2_y)
        # t = (s2_x * (A.y - C.y) - s2_y * (A.x - C.x)) / (-s2_x * s1_y + s1_x * s2_y)

        # if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
        #     intersection_x = round_val(A.x + (t * s1_x))
        #     intersection_y = round_val(A.y + (t * s1_y))
        #     #print("Punkt przecięcia w x:", intersection_x)
        #     #print("Punkt przecięcia w y:", intersection_y)
        #     return Point(intersection_x, intersection_y)s
    except:
        return None

