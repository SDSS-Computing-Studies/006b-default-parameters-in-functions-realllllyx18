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
    angle = math.pi*float(degree)/180
    return angle

def quadratic(a,b,c):
    x1 = round((-float(b) + math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a)),2)
    x2 = round((-float(b) - math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a)),2)
    solution = [x1,x2]
    solution.sort()
    return solution

def solution(List):
    if List[0] > 0:
        answer = List[0]
    elif List[1] > 0:
        answer = List[1]
    return answer


print(convertAngle(30))
print(solution([-8.9, 5.3]))
print(quadratic(3,5,-8))

