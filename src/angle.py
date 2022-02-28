from math import degrees, pow,sqrt
from numpy import arccos

def findAngle(p1,pToCheck,p2):
    # square of absis distance between p1 and pToCheck
    p1px=pow((p1[0]-pToCheck[0]),2)
    # square of absis distance between of p1 and p2
    p1p2x=pow((p1[0]-p2[0]),2)
    # square of absis distance between of patoCheck and p3
    pp3x=pow((pToCheck[0]-p2[0]),2)

    # square of ordinate distance betweenof p1 and pToCheck
    p1py=pow((p1[1]-pToCheck[1]),2)
    # square of ordinate distance between of p1 and p2
    p1p2y=pow((p1[1]-p2[1]),2)
    # square of coordinate distance between of patoCheck and p3
    pp3y=pow((pToCheck[1]-p2[1]),2)
    if (2*sqrt(p1px+p1py)*sqrt(pp3x+pp3y))==0:
        return 0
    # find cosine angle based on law of cosine/cosine rule
    cosineAngle=arccos((p1px+p1py+pp3x+pp3y-p1p2x-p1p2y)/(2*sqrt(p1px+p1py)*sqrt(pp3x+pp3y)))
    return degrees(cosineAngle)