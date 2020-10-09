#! python3

import math

def tempConversion(degree,unit="F"):
    if unit=="F":
        answer=(float(degree)-float(32))*float(5)/float(9)
    if unit!="F":
        answer=(float(degree)*(float(9)/float(5)))+float(32)
    return answer


def factorPair(num,factor):
    answer=float(num)/float(factor),str(factor)
    return answer

def cosineLaw(a,b,,C):
    answer=math.sqrt(float(a)**2+float(b)**2-2*float(a)*float(b)*cos(c))


def convertAngle():

def solution(a,b,c):
    x1=(-float(b)+math.sqrt(float(b)**2-4*float(a)*float(c)))/2*float(a)
    x2=(-float(b)-math.sqrt(float(b)**2-4*float(a)*float(c)))/2*float(a)
    answer=[x1,x2]
    answer.sort()
    return answer

#def quadratic():

