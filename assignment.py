#! python3

import math

def tempConversion(degree, unit = "C"):
    answer = round((9*float(degree)/5 + 32),1)
    if unit == "F":
        answer = round((float(degree) - 32)*5/9,1)
    return answer

def factorPair(num,a):
    b = int(num/a)
    answer = [a,b]
    answer.sort()
    return answer

def convertAngle(degree):
    angle = round(math.pi*float(degree)/180,4)
    return angle

def solution(List):
    if List[0] > 0:
        answer = List[0]
    elif List[1] > 0:
        answer = List[1]
    return answer

def quadratic(a,b,c):
    x1 = round((-float(b) + math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a)),1)
    x2 = round((-float(b) - math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a)),2)
    solution = [x1,x2]
    solution.sort()
    return solution

def cosineLaw(x,y,angle,oppositeSide = True):
    z = round(math.sqrt(float(x)**2 + float(y)**2 - 2*float(x)*float(y)*math.cos(convertAngle(angle))),1)
    if oppositeSide == False:
        a = 1
        b = -2*float(y)*math.cos(convertAngle(angle))
        c = float(y)**2 - float(x)**2
        if float(b)**2 - 4*float(a)*float(c) >= 0:
            z = solution(quadratic(a,b,c))
        else:
            a = 1
            b = -2*float(x)*math.cos(convertAngle(angle))
            c = float(x)**2 - float(y)**2
            z = solution(quadratic(a,b,c))

    return z


print(convertAngle(30))
print(solution([-8.9, 5.3]))
print(quadratic(3,5,-8))
print(cosineLaw(6,9,34))
print(cosineLaw(10,3,50,oppositeSide = False))

