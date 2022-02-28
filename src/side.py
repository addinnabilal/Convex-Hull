# fungsi untuk mengecek sisi titik pToCheck relatif terhadap garis yang menghubungkan p1 dan p2
# mengembalikan -1 bila pToCheck berada di kanan garis yang menghubungkan p1 dan p2
# mengembalikan 1 bila pToCheck berada di kiri garis yang menghubungkan p1 dan p2
def findSide(p1,p2,pToCheck):
    # menggunakan rumus determinan
    det=p1[0]*p2[1] + pToCheck[0]*p1[1] + p2[0]*pToCheck[1] -pToCheck[0]*p2[1] - p2[0]*p1[1] - p1[0]*pToCheck[1]
    # hasil determinan positif berarti pToCheck berada di kiri garis yang menghubungkan p1 dan p2
    if det>0: return -1
    # hasil determinan negatif berarti pToCheck berada di kanan garis yang menghubungkan p1 dan p2
    elif det<0: return 1
    # bila pToCheck berarti pToCheck berada pada garis yang menghubungkan p1 dan p2
    else: return 0