import numpy as np
from hull import findHull

# fungsi utama untuk mencari convex hull dari input points
def myConvexHull(points):
    # buat kelas objHull dengan atribut
    class objHull:
        def __init__(self,simplices):
            self.simplices=simplices
    # urutkan kumpulan titik berdasarkan absis yang menaik, 
    # kemudian bila absis sama, urutkan berfasarkan ordinat yang menaik
    pointsTemp=sorted(points, key=  lambda p: (p[0],p[1]))
    # cari titik-titik ekstrim
    minX=0
    maxX=len(points)-1
    # cari hull-hull di kiri dan kanan dari garis yang menghubungkan kedua titik ekstrem
    hullLeft=findHull(points,pointsTemp[minX],pointsTemp[maxX],1)
    hullRight=findHull(points,pointsTemp[minX],pointsTemp[maxX],-1)
    # gabungkan array berisi hull pada sisi kiri dan kanan di luar "segitiga" p1, p2, dan titik terjauh dengan garis p1p2  
    hull=np.concatenate((hullLeft,hullRight))
    return objHull(hull)