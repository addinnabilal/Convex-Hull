from side import findSide
from angle import findAngle

# fungsi untuk mencari jarak dari pToCheck terhadap garis yang menghubungkan p1 dan p2
def findDistance(p1,p2,pToCheck):
    return abs((pToCheck[1]-p1[1])*(p2[0]-p1[0])-(p2[1]-p1[1])*(pToCheck[0]-p1[0]))
    
# fungsi untuk mencari index pada array of point dari titik terjauh dari garis yang menghubungkan p1 dan p2
# pada sisi tertentu
def findIndexOfMaxDistance(points, p1, p2, side):
    maxDist=0
    maxAngle=0
    maxDistIndex=-1
    n=len(points)
    # iterasi di setiap titik pada kumpulan titik
    for i in range(n):
        tempDist=findDistance(p1,p2,points[i])
        tempAngle=findAngle(p1,points[i],p2)
        # hanya memperhitungkan titik-titik pada sisi yang sedang ditinjau
        if findSide(p1,p2,points[i])==side and tempDist>=maxDist:
            # bila jarak sama, cari titik yang membentuk sudut terbesar dengan p1 dan p2
            if tempDist==maxDist:
                if tempAngle>maxAngle:
                    maxAngle=tempAngle
                    maxDist=tempDist
                    maxDistIndex=i
            else:
                maxAngle=tempAngle
                maxDist=tempDist
                maxDistIndex=i
    return maxDistIndex