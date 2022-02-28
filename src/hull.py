import numpy as np
from side import findSide
from distance import findIndexOfMaxDistance

# fungsi yang menghasilkan array yang berisi hull pada sisi tertentu
# contoh keluaran: [[2 3] [1 4]] berarti hull terbentuk dari pasangan poin pada index 2 dan 4 serta 1 dan 4
def findHull(points, p1, p2, side):
    maxDistIndex=findIndexOfMaxDistance(points, p1, p2, side)
    if maxDistIndex==-1:
        listOfPoints=points.tolist()
        index1=listOfPoints.index(p1.tolist())
        index2=listOfPoints.index(p2.tolist())
        return [[index1,index2]]
    # rekursi untuk mencari hull pada sisi di luar "segitiga" p1, p2, dan titik terjauh dengan garis yang menghubungkan p1 dan p2   
    hull1=findHull(points, p1, points[maxDistIndex], -findSide(p1,points[maxDistIndex],p2))
    hull2=findHull(points, p2, points[maxDistIndex], -findSide(p2,points[maxDistIndex],p1))
    # gabungkan array berisi hull pada sisi kiri dan kanan di luar "segitiga" p1, p2, dan titik terjauh dengan garis p1p2  
    return np.concatenate((hull1,hull2))